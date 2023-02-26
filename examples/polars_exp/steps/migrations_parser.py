import polars as pl

from core.common.context import CardoPolarsContext
from core.common.helpers.dataframes import PolarsDataFrame
from core.common.helpers.steps import PolarsStep


class MigrationsParser(PolarsStep):

    async def process(self, ctx: CardoPolarsContext, df: PolarsDataFrame) -> PolarsDataFrame:
        df = df.select(["company", "year", "from", "to"])
        df = df.filter(pl.col("company") != "Bing")
        return df
