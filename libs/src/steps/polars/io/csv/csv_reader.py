import polars as pl

from core import IStep, CardoContext, DataFrame


class CsvReader(IStep):
    """Local CSV file reader"""

    def __init__(self, path: str, has_headers: bool, lazy: bool = True):
        self.lazy = lazy
        self.headers = has_headers
        self.path = path

    async def process(self, ctx: CardoContext, df: DataFrame = None) -> DataFrame:
        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        reader = pl.scan_csv if ctx.lazy_polars else pl.read_csv
        df = reader(self.path, has_header=self.headers)
        return df