from typing import Union, Tuple

from core import IStep
from core.src.common.context.implementations.spark_context import CardoSparkContext
from core.src.common.helpers.dataframe import SparkDataFrame


class SparkStep(IStep):
    async def process(self, ctx: CardoSparkContext, df: Union[SparkDataFrame, Tuple[SparkDataFrame]]) \
            -> Union[SparkDataFrame, Tuple[SparkDataFrame]]:
        raise NotImplementedError
