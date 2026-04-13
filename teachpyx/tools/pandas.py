import hashlib
import os
import re
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse, unquote
import pandas


def _filename_from_url(url):
    parsed = urlparse(url)
    path = parsed.path
    name = unquote(path.split("/")[-1])
    name = re.sub(r"[^\w.\-]", "_", name)
    assert name, f"unable to create a filename from {url!r}"
    h = hashlib.sha1(url.encode()).hexdigest()[:8]
    return f"{os.path.splitext(name)[0]}_{h}.csv"


def read_csv_cached(
    filepath_or_buffer: str, ignore_cache: bool = False, **kwargs
) -> pandas.DataFrame:
    """
    After the data is loaded with :func:`pandas.read_csv`,
    the data is cached. This is interesting when the data is downloaded.
    The second call reuses the cached data.
    The cached dataframe is stored in
    ``.cache/teachpyx/<filename>_<hash>.csv``.

    :param filepath_or_buffer: Any valid string path is acceptable.
        The string could be a URL. Valid URL schemes include http,
        ftp, s3, gs, and file. For file URLs, a host is expected.
        See :func:`pandas.read_csv`.
    :param ignore_cache: ignore the cache, overwrites it if it exists
    :param kwargs: other argument for :func:`pandas.read_csv`
    :return: dataframe

    .. versionadded:: 0.5.0
    """
    cache_dir = Path.home() / ".cache" / "teachpyx" / "pandas"
    cache_dir.mkdir(parents=True, exist_ok=True)

    cache_name = cache_dir / _filename_from_url(filepath_or_buffer)
    if cache_name.exists() and not ignore_cache:
        return pandas.read_csv(cache_name)

    df = pandas.read_csv(filepath_or_buffer, **kwargs)
    df.to_csv(cache_name, index=False)
    return df


def plot_waterfall(
    data: pandas.DataFrame,
    value_column: str,
    label_column: Optional[str] = None,
    total_label: str = "total",
    ax=None,
    colors: Tuple[str, str, str] = ("#2ca02c", "#d62728", "#1f77b4"),
):
    """
    Draws a waterfall chart from a dataframe.

    :param data: dataframe containing increments
    :param value_column: column with increments
    :param label_column: column with labels, index is used if None
    :param total_label: label used for the final total
    :param ax: existing axis or None to create one
    :param colors: positive, negative, total colors
    :return: axis, computed dataframe used to draw the chart

    .. versionadded:: 0.6.1
    """
    if value_column not in data.columns:
        raise ValueError(f"Unable to find column {value_column!r} in dataframe.")
    if label_column is not None and label_column not in data.columns:
        raise ValueError(f"Unable to find column {label_column!r} in dataframe.")
    if len(colors) != 3:
        raise ValueError(f"colors must contain 3 values, not {len(colors)}.")

    try:
        values = pandas.to_numeric(data[value_column], errors="raise").astype(float)
    except ValueError as exc:
        raise ValueError(
            f"Column {value_column!r} cannot be converted to numeric values."
        ) from exc
    labels = data[label_column] if label_column is not None else data.index
    labels = labels.astype(str)

    starts = values.cumsum().shift(1, fill_value=0.0)
    plot_df = pandas.DataFrame(
        {
            "label": labels,
            "value": values,
            "start": starts,
            "end": starts + values,
            "kind": "variation",
        }
    )

    total = float(values.sum())
    total_row = pandas.DataFrame(
        {
            "label": [total_label],
            "value": [total],
            "start": [0.0],
            "end": [total],
            "kind": ["total"],
        }
    )
    plot_df = pandas.concat([plot_df, total_row], axis=0, ignore_index=True)

    if ax is None:
        import matplotlib.pyplot as plt

        _, ax = plt.subplots(1, 1)

    bar_colors = [
        colors[2]
        if kind == "total"
        else (colors[0] if value >= 0 else colors[1])
        for value, kind in zip(plot_df["value"], plot_df["kind"])
    ]
    ax.bar(
        plot_df["label"],
        plot_df["value"],
        bottom=plot_df["start"],
        color=bar_colors,
    )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylabel(value_column)
    ax.set_xlabel(label_column or "index")

    return ax, plot_df
