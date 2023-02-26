import polars as pl
from polars import DataFrame
from core import IStep, BaseContext


class MigrationsParser(IStep):

    async def process(self, ctx: BaseContext, df: DataFrame) -> DataFrame:
        df = df.select(["company","year","from","to"])
        df = df.filter(pl.col("company") != "Bing")
        return df
