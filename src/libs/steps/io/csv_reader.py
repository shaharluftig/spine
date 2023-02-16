import polars as pl

from src.core.common.context.implementations.cardo_context import CardoContext
from src.core.helpers.dataframe import DataFrame
from src.libs.IStep import IStep


class CsvReader(IStep):
    def __init__(self, path: str, has_headers: bool):
        self.headers = has_headers
        self.path = path

    def process(self, cardo_context: CardoContext, df: DataFrame = None) -> DataFrame:
        cardo_context.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = pl.read_csv(self.path, has_header=self.headers)
        return df
