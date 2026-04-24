# coding: utf-8
"""
Script : statistiques de PR fusionnées par auteur et par semaine
================================================================

Ce script récupère, via l'API GitHub, le nombre de *pull requests* (PR) fusionnées
pour **un ou plusieurs dépôts**, les regroupe par auteur et par semaine sur l'année
écoulée, puis enregistre les graphiques sous forme d'images PNG.

Les données récupérées sont **mises en cache** localement (un fichier CSV par dépôt).
Lors des exécutions suivantes, seules les PR plus récentes que la dernière date mise
en cache sont requêtées, ce qui réduit le nombre d'appels à l'API.

**Dépendances :** ``requests``, ``pandas``, ``matplotlib``.

**Token GitHub :** définissez la variable d'environnement ``GITHUB_TOKEN`` avec un
*Personal Access Token* (PAT) GitHub pour dépasser la limite de 60 requêtes/heure :

.. code-block:: bash

    export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx

**Usage :**

.. code-block:: bash

    python github_stat_pr.py

Les images sont enregistrées dans le répertoire courant :

* ``github_stat_pr_bar.png`` — diagramme empilé (toutes repos confondues)
* ``github_stat_pr_heatmap.png`` — heatmap (toutes repos confondues)
* ``github_stat_pr_lines.png`` — graphe en lignes comparant les dépôts
* ``github_stat_pr_bar_{owner}_{repo}.png`` — diagramme empilé par dépôt
* ``github_stat_pr_heatmap_{owner}_{repo}.png`` — heatmap par dépôt
"""

import datetime
import os
import pathlib

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import requests

# ---------------------------------------------------------------------------
# Paramètres
# ---------------------------------------------------------------------------

REPOS = [
    # ("sdpython", "teachpyx"),
    # ("sdpython", "teachcompute"),
    # ("sdpython", "onnx-extended"),
    ("sdpython", "onnx-diagnostic"),
    ("sdpython", "experimental-experiment"),
    ("xadupre", "yet-another-onnx-builder"),
    ("xadupre", "mbext"),
    ("onnx", "sklearn-onnx"),
    ("onnx", "onnxmltools"),
    # ("sdpython", "onnx-extended"),  # ajoutez d'autres dépôts ici
]

# Répertoire de cache (créé automatiquement si nécessaire)
CACHE_DIR = pathlib.Path(".")

# Liste blanche d'auteurs : seuls ces auteurs seront inclus dans l'analyse.
# Laissez vide ([]) pour inclure tous les auteurs.
AUTHOR_WHITELIST: list[str] = ["xadupre", "sdpython", "Copilot", "dependabot[bot]"]

# Répertoire de sortie pour les images PNG
OUTPUT_DIR = pathlib.Path(".")

# Jeton d'authentification GitHub (optionnel mais recommandé)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

CACHE_DATE_FMT = "%Y-%m-%dT%H:%M:%S%z"


def _cache_path(cache_dir: pathlib.Path, owner: str, repo: str) -> pathlib.Path:
    safe = f"{owner}_{repo}".replace("/", "_")
    return cache_dir / f"prs_cache_{safe}.csv"


def load_cache(cache_dir: pathlib.Path, owner: str, repo: str) -> pd.DataFrame:
    path = _cache_path(cache_dir, owner, repo)
    if not path.exists():
        return pd.DataFrame(columns=["author", "merged_at", "repo"])
    df = pd.read_csv(path, parse_dates=["merged_at"])
    if df["merged_at"].dt.tz is None:
        df["merged_at"] = df["merged_at"].dt.tz_localize("UTC")
    else:
        df["merged_at"] = df["merged_at"].dt.tz_convert("UTC")
    return df


def save_cache(
    cache_dir: pathlib.Path, owner: str, repo: str, df: pd.DataFrame
) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = _cache_path(cache_dir, owner, repo)
    df.to_csv(path, index=False, date_format=CACHE_DATE_FMT)


# ---------------------------------------------------------------------------
# Récupération des PR via l'API GitHub
# ---------------------------------------------------------------------------


def fetch_merged_prs(
    owner: str,
    repo: str,
    token: str = "",
    fetch_since: datetime.datetime | None = None,
) -> list[dict]:
    """Récupère les PR fusionnées pour un dépôt à partir d'une date donnée.

    :param owner: propriétaire du dépôt GitHub
    :param repo: nom du dépôt GitHub
    :param token: jeton d'authentification GitHub (optionnel)
    :param fetch_since: date de départ de la recherche ; si ``None``, remonte
        jusqu'à 365 jours en arrière.
    :return: liste de dictionnaires ``{author, merged_at, repo}``
    """
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    cutoff = (
        fetch_since
        if fetch_since is not None
        else (
            datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=365)
        )
    )

    results = []
    page = 1
    per_page = 100

    while True:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/pulls"
            f"?state=closed&per_page={per_page}&page={page}&sort=updated&direction=desc"
        )
        response = requests.get(url, headers=headers, timeout=30)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            status = exc.response.status_code
            if status == 401:
                raise RuntimeError(
                    "Authentification refusée (401). Vérifiez votre GITHUB_TOKEN."
                ) from exc
            if status == 403:
                raise RuntimeError(
                    "Accès refusé (403). Vous avez peut-être atteint la limite de "
                    "l'API GitHub (60 requêtes/h sans token). Définissez GITHUB_TOKEN."
                ) from exc
            if status == 404:
                raise RuntimeError(
                    f"Dépôt introuvable (404) : {owner}/{repo}. "
                    "Vérifiez OWNER et REPO."
                ) from exc
            raise
        prs = response.json()

        if not prs:
            break

        stop = False
        for pr in prs:
            merged_at = pr.get("merged_at")
            if not merged_at:
                continue
            merged_dt = datetime.datetime.fromisoformat(
                merged_at.replace("Z", "+00:00")
            )
            if merged_dt <= cutoff:
                stop = True
                break
            author = (pr.get("user") or {}).get("login", "unknown")
            results.append(
                {"author": author, "merged_at": merged_dt, "repo": f"{owner}/{repo}"}
            )

        if stop:
            break

        page += 1

    return results


def load_prs_with_cache(
    owner: str,
    repo: str,
    token: str = "",
    cache_dir: pathlib.Path = pathlib.Path("."),
) -> pd.DataFrame:
    """Charge les PR fusionnées en utilisant le cache local.

    :return: DataFrame avec les colonnes ``author``, ``merged_at``, ``repo``
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff_365 = now - datetime.timedelta(days=365)

    cached_df = load_cache(cache_dir, owner, repo)

    if cached_df.empty:
        fetch_since = None
        print(f"  {owner}/{repo} : cache vide, récupération complète…")
    else:
        latest = cached_df["merged_at"].max()
        fetch_since = latest.replace(hour=0, minute=0, second=0, microsecond=0)
        print(
            f"  {owner}/{repo} : cache chargé ({len(cached_df)} entrées), "
            f"récupération des PR depuis {fetch_since.date()}…"
        )

    new_prs = fetch_merged_prs(owner, repo, token, fetch_since=fetch_since)
    print(f"    → {len(new_prs)} nouvelle(s) PR(s) récupérée(s) via l'API.")

    if new_prs:
        new_df = pd.DataFrame(new_prs)
        if cached_df.shape[0]:
            combined = pd.concat([cached_df, new_df], ignore_index=True)
        else:
            combined = new_df
    else:
        combined = cached_df.copy()

    combined.drop_duplicates(subset=["repo", "author", "merged_at"], inplace=True)
    combined = combined[combined["merged_at"] >= cutoff_365].copy()
    combined.sort_values("merged_at", inplace=True)
    combined.reset_index(drop=True, inplace=True)

    save_cache(cache_dir, owner, repo, combined)
    print(f"    → cache mis à jour ({len(combined)} entrées au total).")

    return combined


# ---------------------------------------------------------------------------
# Agrégation
# ---------------------------------------------------------------------------


def aggregate_weekly(df: pd.DataFrame) -> pd.DataFrame:
    """Regroupe les PR par (repo, author, week) et retourne un DataFrame long."""
    df = df.copy()
    df["week"] = df["merged_at"].dt.to_period("W").dt.start_time
    return df.groupby(["repo", "author", "week"]).size().reset_index(name="pr_count")


def make_pivot(weekly: pd.DataFrame) -> pd.DataFrame:
    """Construit le tableau croisé auteur x semaine trié par total décroissant."""
    pivot = weekly.pivot_table(
        index="author", columns="week", values="pr_count", aggfunc="sum", fill_value=0
    )
    return pivot.loc[pivot.sum(axis=1).sort_values(ascending=False).index]


# ---------------------------------------------------------------------------
# Visualisation
# ---------------------------------------------------------------------------


def plot_bar(pivot: pd.DataFrame, title: str, output_path: pathlib.Path) -> None:
    """Diagramme à barres empilées (auteur x semaine) enregistré en PNG."""
    fig, ax = plt.subplots(figsize=(14, 5))
    stacked_height = None
    week_nums = mdates.date2num(pivot.columns.to_pydatetime())

    for author in pivot.index:
        values = pivot.loc[author].values
        if stacked_height is None:
            ax.bar(week_nums, values, width=5, label=author)
            stacked_height = values.copy()
        else:
            ax.bar(week_nums, values, width=5, bottom=stacked_height, label=author)
            stacked_height += values

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=4))
    plt.xticks(rotation=45, ha="right")
    ax.set_xlabel("Semaine")
    ax.set_ylabel("Nombre de PR fusionnées")
    ax.set_title(title)
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1), title="Auteur")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"  → {output_path}")


def plot_heatmap(pivot: pd.DataFrame, title: str, output_path: pathlib.Path) -> None:
    """Heatmap auteur x semaine enregistrée en PNG."""
    fig, ax = plt.subplots(figsize=(14, max(3, len(pivot) * 0.5)))
    im = ax.imshow(pivot.values, aspect="auto", cmap="YlOrRd")
    plt.colorbar(im, ax=ax, label="Nombre de PR")

    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)

    step = max(1, len(pivot.columns) // 12)
    ax.set_xticks(range(0, len(pivot.columns), step))
    ax.set_xticklabels(
        [str(d)[:10] for d in pivot.columns[::step]], rotation=45, ha="right"
    )

    ax.set_title(title)
    ax.set_xlabel("Semaine")
    ax.set_ylabel("Auteur")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"  → {output_path}")


def plot_lines_by_repo(
    weekly: pd.DataFrame, title: str, output_path: pathlib.Path
) -> None:
    """Graphe en lignes : total de PR fusionnées par semaine pour chaque dépôt.

    Chaque dépôt est représenté par une ligne, ce qui permet de comparer
    visuellement l'activité entre dépôts.
    """
    repo_weekly = (
        weekly.groupby(["repo", "week"])["pr_count"].sum().reset_index()
    )
    all_weeks = sorted(repo_weekly["week"].unique())

    fig, ax = plt.subplots(figsize=(14, 5))
    for repo_name, grp in repo_weekly.groupby("repo"):
        grp_indexed = grp.set_index("week").reindex(all_weeks, fill_value=0)
        week_nums = mdates.date2num(
            pd.to_datetime(grp_indexed.index).to_pydatetime()
        )
        ax.plot(
            week_nums,
            grp_indexed["pr_count"].values,
            marker="o",
            markersize=3,
            label=repo_name,
        )

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=4))
    plt.xticks(rotation=45, ha="right")
    ax.set_xlabel("Semaine")
    ax.set_ylabel("Nombre de PR fusionnées")
    ax.set_title(title)
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1), title="Dépôt")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)
    print(f"  → {output_path}")


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Récupération des données
    print("Récupération des PR fusionnées…")
    frames = []
    for owner, repo in REPOS:
        frames.append(load_prs_with_cache(owner, repo, GITHUB_TOKEN, CACHE_DIR))
    if not frames:
        print("Aucune donnée.")
        return

    merged_prs = pd.concat(frames, ignore_index=True)
    print(f"\nTotal : {len(merged_prs)} PR(s) fusionnée(s).")

    # 2. Filtre par liste blanche
    df = merged_prs.copy()
    if AUTHOR_WHITELIST:
        df = df[df["author"].isin(AUTHOR_WHITELIST)].copy()
        if df.empty:
            print("Aucun auteur de la liste blanche trouvé dans les données.")
            return

    # 3. Agrégation
    weekly = aggregate_weekly(df)
    pivot_all = make_pivot(weekly)

    # Agrégation non filtrée pour le graphe de comparaison entre dépôts
    weekly_all = aggregate_weekly(merged_prs)

    # 4. Graphiques combinés (toutes repos)
    print("\nGénération des graphiques combinés…")
    plot_bar(
        pivot_all,
        "PR fusionnées par semaine",
        OUTPUT_DIR / "github_stat_pr_bar.png",
    )
    plot_heatmap(
        pivot_all,
        "Heatmap des PR fusionnées",
        OUTPUT_DIR / "github_stat_pr_heatmap.png",
    )

    # 4b. Graphe en lignes : une ligne par dépôt, auteurs agrégés (données non filtrées)
    if len(REPOS) > 1:
        plot_lines_by_repo(
            weekly_all,
            "PR fusionnées par semaine — comparaison entre dépôts",
            OUTPUT_DIR / "github_stat_pr_lines.png",
        )

    print("\nTerminé.")

if __name__ == "__main__":
    main()
