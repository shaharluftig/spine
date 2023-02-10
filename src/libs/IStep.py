from typing import Union

from pyspark.sql import DataFrame as SparkDataFrame

from src.executor.common.context.implementations.cardo_context import CardoContext


class IStep:
    def process(self, cardo_context: CardoContext, df: Union[SparkDataFrame, None]) -> SparkDataFrame:
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__
