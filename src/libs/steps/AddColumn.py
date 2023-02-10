import pyspark.sql.functions as F
from pyspark.sql import DataFrame as SparkDataFrame

from src.executor.common.context.implementations.cardo_context import CardoContext
from src.executor.dataframe.cardo_dataframe import CardoDataFrame
from src.libs.IStep import IStep


class AddColumn(IStep):
    def process(self, cardo_context: CardoContext, df: CardoDataFrame) -> SparkDataFrame:
        pass
