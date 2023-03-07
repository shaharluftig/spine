try:
    from pandas import DataFrame

    PandasDataFrame = DataFrame
except ImportError:
    raise ImportError("Pyspark must be installed")
