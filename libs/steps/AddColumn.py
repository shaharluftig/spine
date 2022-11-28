import pyspark.sql.functions as F
from pyspark.sql import DataFrame as SparkDataFrame

from executor.common.context.cardo_context import CardoContext
from libs.IStep import IStep


class AddColumn(IStep):
    def process(self, cardo_context: CardoContext, df: SparkDataFrame) -> SparkDataFrame:
        return df.withColumn("hello", F.lit("world"))
