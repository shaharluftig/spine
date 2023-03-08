import polars as pl

from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from spinecore.common.helpers.steps.polars_step import PolarsStep


class CsvReader(PolarsStep):
    """Local CSV file reader"""

    def __init__(self, path: str, has_headers: bool, lazy: bool = True):
        self.lazy = lazy
        self.headers = has_headers
        self.path = path

    async def process(self, ctx: SpinePolarsContext, df: PolarsDataFrame = None) -> PolarsDataFrame:

        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        reader = pl.scan_csv if ctx.lazy else pl.read_csv
        df = reader(self.path, has_header=self.headers)
        return df
