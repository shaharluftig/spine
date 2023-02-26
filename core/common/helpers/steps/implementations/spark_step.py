from typing import Union, Tuple

from core.common.context.implementations.spark_context import CardoSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps.IStep import IStep


class SparkStep(IStep):
    async def process(self, ctx: CardoSparkContext, df: Union[SparkDataFrame, Tuple[SparkDataFrame]]) \
            -> Union[SparkDataFrame, Tuple[SparkDataFrame]]:
        raise NotImplementedError
