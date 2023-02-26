import polars as pl

from core.src.common.context.implementations.polars_context import CardoPolarsContext
from core.src.common.helpers.dataframe import PolarsDataFrame
from core.src.common.helpers.steps.polars_step import PolarsStep


class CsvReader(PolarsStep):
    """Local CSV file reader"""

    def __init__(self, path: str, has_headers: bool, lazy: bool = True):
        self.lazy = lazy
        self.headers = has_headers
        self.path = path

    async def process(self, ctx: CardoPolarsContext, df: PolarsDataFrame = None) -> PolarsDataFrame:
        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        reader = pl.scan_csv if ctx.lazy else pl.read_csv
        df = reader(self.path, has_header=self.headers)
        return df
