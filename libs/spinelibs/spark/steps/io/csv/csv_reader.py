from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.steps.spark_step import SparkStep


class CsvReader(SparkStep):
    """Local CSV file reader"""

    def __init__(self, path: str, has_headers: bool):
        self.headers = has_headers
        self.path = path

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame = None) -> SparkDataFrame:
        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = ctx.spark.read.csv(self.path, header=self.headers)
        return df
