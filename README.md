# Seafarer ⛵

Taxicab metric on the sphere! Install via

```bash
pip install seafarer
```

This library calculates the "seafarer distance" between two points on Earth:
Travel parallel to latitude and longitude instead of "as the crow flies" –
like in the old days...

## Usage

Calculate the distance between Schwerin and Helsinki:

```python
from seafarer import seafarer_metric

schwerin = (53.629722, 11.414722) # (lat, lon)
helsinki = (60.170278, 24.952222)

seafarer_metric(schwerin, helsinki)
# 1474.7398906623202 kilometres
```

You can also obtain the result in different units:

```python
seafarer_metric(schwerin, helsinki, unit="mi")
# 916.3608837507956 miles
seafarer_metric(schwerin, helsinki, unit="ft")
# 4838385.468052049 feet
```

Seafarer is using the [haversine](https://github.com/mapado/haversine) library
under the hood and you can use their `Unit` directly:

```python
from haversine import Unit
seafarer_metric(schwerin, helsinki, unit=Unit.NAUTICAL_MILES)
# 796.2958366185961 nautical miles
```

## What is this? Why Seafarer?

On a 2-dimensional plane, the metric obtained when travelling along the axes
is known as [taxicab](https://en.wikipedia.org/wiki/Taxicab_geometry),
Manhattan, or L1 metric. What is the equivalent on a 3-dimensional sphere?

We calculate the distance when travelling along the grid of longitudinal and
latitudinal lines. When travelling from Schwerin (53°N 11°E) to Helsinki
(60°N 24°E) in the example above, there are two possiblities: travel via
53°N 24°E or 60°N 11°E. Unlike the 2D case, these two distances are
(generally) different, so we use the short one.

Before navigation improved to a sufficient degree, this is how ships were
sailing: parallel to the equator until they hit the target meridian, then
North or South to their final destination. Hence seafarer metric! ⛵
