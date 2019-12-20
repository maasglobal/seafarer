# seafarer

Taxicab metric on the sphere! Install via

```bash
pip install seafarer
```

This library calculates the "seafarer distance" between two points on Earth:
Travel parallel to latitude and longitude instead of "as the crow flies",
as in the old days...

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
