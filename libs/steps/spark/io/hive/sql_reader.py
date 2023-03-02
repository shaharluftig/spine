from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class SqlReader(SparkStep):
    def __init__(self, table_name: str):
        self.table_name = table_name

    def process(self, ctx: GarnetSparkContext, df: SparkDataFrame = None):
        df = ctx.spark.table(self.table_name)
        ctx.logger.info(f'Reading table: {self.table_name} from Hive MetaStore')
        return df
