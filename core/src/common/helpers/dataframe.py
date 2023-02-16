from typing import Union
from pyspark.sql import DataFrame as SparkDataFrame
from pandas import DataFrame as PandasDataFrame
from polars import DataFrame as PolarsDataFrame

DataFrame = Union[SparkDataFrame, PandasDataFrame, PolarsDataFrame, None]
