from typing import Union

from pandas import DataFrame as _PandasDataFrame
from polars import LazyFrame as _LazyFrame, DataFrame as _EagerDataFrame
from pyspark.sql import DataFrame as _SparkDataFrame

# TODO: Make optional imports

PolarsDataFrame = Union[_LazyFrame, _EagerDataFrame]
SparkDataFrame = _SparkDataFrame

DataFrame = Union[SparkDataFrame, PolarsDataFrame, _PandasDataFrame]
