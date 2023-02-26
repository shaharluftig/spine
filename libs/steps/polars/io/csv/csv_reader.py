import polars as pl

from core.common.context import CardoPolarsContext
from core.common.helpers.dataframes import PolarsDataFrame
from core.common.helpers.steps import PolarsStep


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
