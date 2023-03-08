from core.common.context.spark_context import GarnetSparkContext
from core.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from core.common.helpers.steps.spark_step import SparkStep


class HdfsReader(SparkStep):
    def __init__(self, path: str, format: str, schema=None, options=None):
        self.path = path
        self.format = format
        self.schema = schema
        self.options = options or {}

    async def process(self, ctx: GarnetSparkContext, df: SparkDataFrame = None):
        df.spark.catalog.refreshByPath(self.path)
        data = df.spark.read.load(self.path, self.format, self.schema, **self.options)
        df.logger.info(f'Reading data from HDFS from {self.path}')
        return data
