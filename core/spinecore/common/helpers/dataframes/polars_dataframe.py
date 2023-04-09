from typing import Union

try:
    from polars import LazyFrame as _LazyFrame, DataFrame as _EagerDataFrame

    PolarsDataFrame = Union[_LazyFrame, _EagerDataFrame]
except ImportError:
    raise ImportError("Polars must be installed")
