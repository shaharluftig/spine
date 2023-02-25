from typing import Union

# TODO: Make optional imports
from pandas import DataFrame as PandasDataFrame
from polars import DataFrame as PolarsDataFrame
from polars import LazyFrame as LazyPolarsDataFrame
from pyspark.sql import DataFrame as SparkDataFrame

DataFrame = Union[SparkDataFrame, PandasDataFrame, PolarsDataFrame, LazyPolarsDataFrame, None]
