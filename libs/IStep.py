from typing import Union

from pyspark.sql import DataFrame as SparkDataFrame

from executor.common.context.cardo_context import CardoContext


class IStep:
    def process(self, cardo_context: CardoContext, df: Union[SparkDataFrame, None]) -> Union[SparkDataFrame]:
        raise NotImplementedError
