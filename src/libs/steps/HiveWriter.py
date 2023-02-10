from pyspark.sql import DataFrame as SparkDataFrame

from src.executor.common.context.implementations.cardo_context import CardoContext
from src.executor.dataframe.cardo_dataframe import CardoDataFrame
from src.libs.IStep import IStep


class HiveWriter(IStep):
    def process(self, cardo_context: CardoContext, df: CardoDataFrame = None) -> SparkDataFrame:
        print("Written to hive")
