# -*- coding: utf-8 -*-

"""Calculate distances."""

from typing import Sequence, Union

from haversine import Unit, haversine


def seafarer_metric(
    point1: Sequence[float],
    point2: Sequence[float],
    unit: Union[Unit, str] = Unit.KILOMETERS,
) -> float:
    """Calculate an L1-metric equivalent on the sphere."""

    unit = Unit(unit)

    assert len(point1) == 2
    assert len(point2) == 2

    lat1, lng1 = point1
    lat2, lng2 = point2

    # calculate distances along latitude and longitude and return smaller value
    dis1 = haversine(point1, (lat1, lng2), unit) + haversine((lat1, lng2), point2, unit)
    dis2 = haversine(point1, (lat2, lng1), unit) + haversine((lat2, lng1), point2, unit)

    return min(dis1, dis2)
