from core.common.context.spark_context import SpineSparkContext
from core.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from core.common.helpers.steps.spark_step import SparkStep


class HiveReader(SparkStep):
    def __init__(self, query: str):
        self.query = query

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame = None):
        df = ctx.spark.sql(self.query)
        ctx.logger.info(f'Reading query: {self.query} from Hive MetaStore')
        return df
