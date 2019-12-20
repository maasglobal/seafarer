# -*- coding: utf-8 -*-

"""Command line and main script."""
import argparse
import logging
import sys

from haversine import Unit

from .distance import seafarer_metric

LOGGER = logging.getLogger(__name__)


def _parse_args():
    parser = argparse.ArgumentParser(description="Taxicab metric on the sphere!")
    parser.add_argument("lat1", type=float, help="latitude of first point")
    parser.add_argument("lng1", type=float, help="longitude of first point")
    parser.add_argument("lat2", type=float, help="latitude of first point")
    parser.add_argument("lng2", type=float, help="longitude of first point")
    parser.add_argument(
        "--unit",
        "-u",
        choices=[unit.value for unit in Unit],
        default=Unit.KILOMETERS,
        help="unit for distance",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="log level (repeat for more verbosity)",
    )

    return parser.parse_args()


def main():
    """Command line and main script."""
    args = _parse_args()

    logging.basicConfig(
        stream=sys.stderr, level=logging.DEBUG if args.verbose > 0 else logging.INFO,
    )

    LOGGER.debug(args)

    unit = Unit(args.unit)

    LOGGER.info(
        "Calculating seafarer distance between (%g°, %g°) and (%g°, %g°) in <%s>",
        args.lat1,
        args.lng1,
        args.lat2,
        args.lng2,
        unit,
    )

    distance = seafarer_metric(
        point1=(args.lat1, args.lng1), point2=(args.lat2, args.lng2), unit=unit
    )

    print(f"{distance:g} {unit.value}")


if __name__ == "__main__":
    main()
