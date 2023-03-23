from typing import Union, Tuple, List

import pyspark.sql.functions as F

from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.steps.spark_step import SparkStep


class FilterCountry(SparkStep):

    def __init__(self, country_to_remove: List[str]):
        self.country_to_remove = country_to_remove

    async def process(self, ctx: SpineSparkContext, df: Union[SparkDataFrame, Tuple[SparkDataFrame]]) -> Union[
        SparkDataFrame, Tuple[SparkDataFrame]]:
        return df.where(~F.col("country").isin(self.country_to_remove))
