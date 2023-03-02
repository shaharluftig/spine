from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class HdfsReader(SparkStep):
    def __init__(self, path: str, format: str, schema=None, options=None):
        self.path = path
        self.format = format
        self.schema = schema
        self.options = options or {}

    def process(self, ctx: GarnetSparkContext, df: SparkDataFrame = None):
        df.spark.catalog.refreshByPath(self.path)
        data = df.spark.read.load(self.path, self.format, self.schema, **self.options)
        df.logger.info(f'read data from Hdfs from {self.path} successfully')
        return data
