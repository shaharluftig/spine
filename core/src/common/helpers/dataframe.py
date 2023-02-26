from typing import Union

from pandas import DataFrame as PandasDataFrame
from polars import LazyFrame, DataFrame as EagerDataFrame
from pyspark.sql import DataFrame as SparkDataFrame

# TODO: Make optional imports

PolarsDataFrame = Union[LazyFrame, EagerDataFrame]

DataFrame = Union[SparkDataFrame, PolarsDataFrame, PandasDataFrame]
