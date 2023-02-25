import polars as pl
from polars import DataFrame
from core import IStep, CardoContext


class MigrationsParser(IStep):

    async def process(self, ctx: CardoContext, df: DataFrame) -> DataFrame:
        df = df.drop(["url"])
        df = df.filter(pl.col("company") != "Bing")
        return df
