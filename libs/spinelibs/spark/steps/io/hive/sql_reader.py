from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.steps.spark_step import SparkStep


class SqlReader(SparkStep):
    def __init__(self, table_name: str):
        self.table_name = table_name

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame = None):
        df = ctx.spark.table(self.table_name)
        ctx.logger.info(f'Reading table: {self.table_name} from Hive MetaStore')
        return df
