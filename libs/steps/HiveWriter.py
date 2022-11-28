from pyspark.sql import DataFrame as SparkDataFrame

from executor.common.context.cardo_context import CardoContext
from libs.IStep import IStep


class HiveWriter(IStep):
    def process(self, cardo_context: CardoContext, df: SparkDataFrame = None) -> SparkDataFrame:
        print("Written to hive")
        return None
