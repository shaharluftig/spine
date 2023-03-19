from typing import Union, Tuple

from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.contract.IStep import IStep


class SparkStep(IStep):
    """IStep implementation for spark steps"""

    async def process(self, ctx: SpineSparkContext, df: Union[SparkDataFrame, Tuple[SparkDataFrame]]) \
            -> Union[SparkDataFrame, Tuple[SparkDataFrame]]:
        raise NotImplementedError
