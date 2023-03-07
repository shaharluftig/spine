from typing import Tuple

from core.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from core.common.helpers.steps.spark_step import SparkStep


class ConsoleWriter(SparkStep):
    """Prints dataframes to console"""

    async def process(self, ctx: SparkDataFrame, *dfs: SparkDataFrame) -> Tuple[SparkDataFrame]:
        ctx.logger.info("Writing to console")
        for df in dfs:
            df.show()
        return dfs
