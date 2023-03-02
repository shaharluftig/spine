from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class HiveReader(SparkStep):
    def __init__(self, query: str):
        self.query = query

    def process(self, ctx: GarnetSparkContext, df: SparkDataFrame = None):
        df = ctx.spark.sql(self.query)
        ctx.logger.info(f'Reading query: {self.query} from Hive MetaStore')
        return df
