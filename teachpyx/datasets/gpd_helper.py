from ..tools.data_helper import download


def get_naturalearth_cities(dest: str = ".", timeout: int = 10, verbose: bool = False):
    """
    Retrieves file ``naturalearth_cities.shp``, ``naturalearth_cities.shx``,
    ``naturalearth_cities.dbf`` in
    `teachdata/geopandas/data/naturalearth_cities/
    <https://github.com/sdpython/teachdata/blob/main/geopandas/data/naturalearth_cities/>`_.
    """
    urls = [
        "https://github.com/sdpython/teachdata/raw/main/geopandas/data/naturalearth_cities/naturalearth_cities.shp",
        "https://github.com/sdpython/teachdata/raw/main/geopandas/data/naturalearth_cities/naturalearth_cities.shx",
        "https://github.com/sdpython/teachdata/raw/main/geopandas/data/naturalearth_cities/naturalearth_cities.dbf",
    ]
    return [download(url, dest=dest, timeout=timeout, verbose=verbose) for url in urls]


def get_naturalearth_lowres(dest: str = ".", timeout: int = 10, verbose: bool = False):
    """
    Retrieves files ``naturalearth_lowres.shp``, ``naturalearth_lowres.shx``,
    ``naturalearth_lowres.dbf`` in
    `teachdata/geopandas/data/naturalearth_cities/
    <https://github.com/sdpython/teachdata/blob/main/geopandas/data/naturalearth_lowres/>`_.
    """
    urls = [
        "https://github.com/sdpython/teachdata/raw/main/geopandas/data/naturalearth_lowres/naturalearth_lowres.shp",
        "https://github.com/sdpython/teachdata/raw/main/geopandas/data/naturalearth_lowres/naturalearth_lowres.shx",
        "https://github.com/sdpython/teachdata/raw/main/geopandas/data/naturalearth_lowres/naturalearth_lowres.dbf",
    ]
    return [download(url, dest=dest, timeout=timeout, verbose=verbose) for url in urls]
