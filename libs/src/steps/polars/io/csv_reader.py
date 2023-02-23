import polars as pl

from core import IStep, CardoContext, DataFrame


class CsvReader(IStep):
    def __init__(self, path: str, has_headers: bool):
        self.headers = has_headers
        self.path = path

    async def process(self, cardo_context: CardoContext, df: DataFrame = None) -> DataFrame:
        cardo_context.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = pl.read_csv(self.path, has_header=self.headers)
        return df
