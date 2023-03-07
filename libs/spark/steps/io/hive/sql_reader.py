from core.common.context.spark_context import GarnetSparkContext
from core.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from core.common.helpers.steps.spark_step import SparkStep


class SqlReader(SparkStep):
    def __init__(self, table_name: str):
        self.table_name = table_name

    async def process(self, ctx: GarnetSparkContext, df: SparkDataFrame = None):
        df = ctx.spark.table(self.table_name)
        ctx.logger.info(f'Reading table: {self.table_name} from Hive MetaStore')
        return df
