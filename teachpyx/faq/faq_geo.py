# coding: utf-8
import math
from typing import Tuple


class constants93:
    GRS80E = 0.081819191042816
    LONG_0 = 3
    XS = 700000
    YS = 12655612.0499
    n = 0.7256077650532670
    C = 11754255.4261


def lambert93_to_WGPS(lambertE: float, lambertN: float) -> Tuple[float, float]:
    """
    Converts coordinates given in
    `Lambert 93 <https://fr.wikipedia.org/wiki/Projection_conique_conforme_de_Lambert>`_
    system, this system is used by `IGN <https://www.ign.fr/>`_
    and their :epkg:`GEOFLA` file format.

    :param lambertE: east
    :param lambertN: north
    :return: longitude, latitude

    The function is inspired from
    `lam93toLatLon.py <https://gist.github.com/flire/0a305eeec77bc84a73af8ddc8f9ec043>`_.

    .. faqref::
        :tag: geo
        :title: Les fichiers GEOFLA ne contiennent pas de longitude, latitude ?

        Les coordonnées contenues dans les fichiers :epkg:`GEOFLA`
        ne sont pas toujours des longitudes, latitudes mais des coordonnées exprimées dans un système
        de projection conique `Lambert 93 <https://fr.wikipedia.org/wiki/Projection_conique_conforme_de_Lambert>`_.
        Il faut convertir les coordonnées avant de pouvoir tracer la carte ou changer la projection
        utilisée par :epkg:`cartopy` :
        `Lambert Conformal Projection <https://scitools.org.uk/cartopy/docs/v0.15/crs/projections.html#lambertconformal>`_.
    """

    delX = lambertE - constants93.XS
    delY = lambertN - constants93.YS
    gamma = math.atan(-delX / delY)
    R = math.sqrt(delX * delX + delY * delY)
    latiso = math.log(constants93.C / R) / constants93.n
    sinPhiit0 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * math.sin(1))
    )
    sinPhiit1 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * sinPhiit0)
    )
    sinPhiit2 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * sinPhiit1)
    )
    sinPhiit3 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * sinPhiit2)
    )
    sinPhiit4 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * sinPhiit3)
    )
    sinPhiit5 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * sinPhiit4)
    )
    sinPhiit6 = math.tanh(
        latiso + constants93.GRS80E * math.atanh(constants93.GRS80E * sinPhiit5)
    )

    longRad = math.asin(sinPhiit6)
    latRad = gamma / constants93.n + constants93.LONG_0 / 180 * math.pi

    longitude = latRad / math.pi * 180
    latitude = longRad / math.pi * 180

    return longitude, latitude
