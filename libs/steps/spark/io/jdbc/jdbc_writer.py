from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class JDBCWriter(SparkStep):

    async def process(self, ctx: GarnetSparkContext, df: SparkDataFrame) -> SparkDataFrame:
        pass
