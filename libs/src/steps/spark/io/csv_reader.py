from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.common.helpers.dataframe import DataFrame
from libs.src.IStep import IStep


class CsvReader(IStep):
    def __init__(self, path: str, has_headers: bool):
        self.headers = has_headers
        self.path = path

    async def process(self, ctx: CardoContext, df: DataFrame = None) -> DataFrame:
        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = ctx.spark.read.csv(self.path, header=self.headers)
        return df
