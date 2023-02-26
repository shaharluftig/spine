from core import IStep
from core.src.common.context.implementations.spark_context import CardoSparkContext
from core.src.common.helpers.dataframe import SparkDataFrame


class CsvReader(IStep):
    """Local CSV file reader"""

    def __init__(self, path: str, has_headers: bool):
        self.headers = has_headers
        self.path = path

    async def process(self, ctx: CardoSparkContext, df: SparkDataFrame = None) -> SparkDataFrame:
        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = ctx.spark.read.csv(self.path, header=self.headers)
        return df
