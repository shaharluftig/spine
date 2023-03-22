try:
    from pyspark.sql import DataFrame
    SparkDataFrame = DataFrame
except ImportError:
    raise ImportError("Pyspark must be installed")
