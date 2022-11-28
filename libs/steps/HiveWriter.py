from pyspark.sql import DataFrame as SparkDataFrame

from executor.common.context.CardoContext import CardoContext
from libs.IStep import IStep


class HiveWriter(IStep):
    def process(self, cardo_context: CardoContext, df: SparkDataFrame) -> SparkDataFrame:
        print("Written to hive")
