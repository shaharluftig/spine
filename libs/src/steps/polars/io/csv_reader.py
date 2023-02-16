import polars as pl

from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.common.helpers.dataframe import DataFrame
from libs.src.IStep import IStep


class CsvReader(IStep):
    def __init__(self, path: str, has_headers: bool):
        self.headers = has_headers
        self.path = path

    def process(self, cardo_context: CardoContext, df: DataFrame = None) -> DataFrame:
        cardo_context.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = pl.read_csv(self.path, has_header=self.headers)
        return df
