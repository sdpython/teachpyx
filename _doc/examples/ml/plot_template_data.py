"""
Données parcours-sup 2021-2025
==============================

"""

import pandas
from teachpyx.tools.pandas import read_csv_cached
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import HistGradientBoostingRegressor

# from skrub import TableReport


def get_data():
    urls = {
        "2021": "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup_2021/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
        "2022": "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup_2022/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
        "2023": "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup_2023/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
        "2024": "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup_2024/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
        "2025": "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-parcoursup/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
    }

    dfs = {}
    for k, url in urls.items():
        print(f"loading {k!r}")
        dfs[k] = read_csv_cached(url, sep=";")

    return pandas.concat(dfs.values(), axis=0)


def select_variables_and_clean(df):
    keys = [
        "Région de l’établissement",
        "Session",
        "Statut de l’établissement de la filière de formation (public, privé…)",
        "Sélectivité",
        "Code UAI de l'établissement",
        "Établissement",
        "Filière de formation détaillée bis",
        "Filière de formation très agrégée",
        "Filière de formation.1",
        "Académie de l’établissement",
        "Code départemental de l’établissement",
        "Commune de l’établissement",
        "Concours communs et banque d'épreuves",
    ]
    cible = "Effectif total des candidats pour une formation"
    columns = set(df.columns)
    assert set(keys) & set(columns) == set(
        keys
    ), f"Missing columns {set(keys) - set(keys) & set(columns)} in {sorted(df.columns)}"
    groups = df[[*keys, cible]].groupby(keys).count()
    filtered = groups[groups[cible] > 1].reset_index(drop=False)

    mask = filtered.duplicated(subset=keys, keep=False)
    return filtered[~mask][[*keys, cible]], cible


def compute_oracle(table, cible):
    vars = [c for c in table.columns if c != cible]
    f2025 = table["Session"] == 2025
    f2024 = table["Session"] == 2024
    ftwo = table[f2025 | f2024]
    piv = (
        pandas.pivot_table(
            ftwo,
            index=[c for c in vars if c != "Session"],
            columns="Session",
            values=cible,
        )
        # .dropna(axis=0)  # fails
        .sort_index()
    )
    return mean_absolute_error(piv[2025], piv[2024])


def split_train_test(table, cuble):
    X, y = table.drop(cible, axis=1), table[cible]

    train_test = X["Session"] < 2025

    drop = ["Session", "Code UAI de l'établissement", "Établissement"]

    train_X = X[train_test].drop(drop, axis=1)
    train_y = y[train_test]
    test_X = X[train_test].drop(drop, axis=1)
    test_y = y[train_test]
    return train_X, test_X, train_y, test_y


def make_pipeline(table, cible):
    vars = [c for c in table.columns if c != "cible"]
    num_cols = ["Capacité de l’établissement par formation"]
    cat_cols = [c for c in vars if c not in num_cols]

    model = Pipeline(
        [
            (
                "preprocessing",
                ColumnTransformer(
                    [
                        ("num", StandardScaler(), num_cols),
                        ("cats", OneHotEncoder(handle_unknown="ignore"), cat_cols),
                    ]
                ),
            ),
            ("regressor", HistGradientBoostingRegressor()),
        ]
    )
    return model


data = get_data()
table, cible = select_variables_and_clean(data)
# oracle = compute_oracle(table, cible)
# print(f"oracle : {oracle}")

# train_X, test_X, train_y, test_y = split_train_test(table, cible)
# model = make_pipeline(table, cible)
# model.fit(train_X, train_y)
