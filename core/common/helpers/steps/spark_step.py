from typing import Union, Tuple

from core.common.context.spark_context import GarnetSparkContext
from core.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from core.common.helpers.contract.IStep import IStep


class SparkStep(IStep):
    async def process(self, ctx: GarnetSparkContext, df: Union[SparkDataFrame, Tuple[SparkDataFrame]]) \
            -> Union[SparkDataFrame, Tuple[SparkDataFrame]]:
        raise NotImplementedError
