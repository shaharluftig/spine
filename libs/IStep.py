from pyspark.sql import DataFrame as SparkDataFrame

from executor.common.context.CardoContext import CardoContext


class IStep:
    def process(self, cardo_context: CardoContext, df: SparkDataFrame) -> SparkDataFrame:
        raise NotImplementedError
