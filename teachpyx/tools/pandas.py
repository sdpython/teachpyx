import hashlib
import os
import re
from pathlib import Path
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
    """
    cache_dir = Path.home() / ".cache" / "teachpyx" / "pandas"
    cache_dir.mkdir(parents=True, exist_ok=True)

    cache_name = cache_dir / _filename_from_url(filepath_or_buffer)
    if cache_name.exists() and not ignore_cache:
        return pandas.read_csv(cache_name)

    df = pandas.read_csv(filepath_or_buffer, **kwargs)
    df.to_csv(cache_name, index=False)
    return df
