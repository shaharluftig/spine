import polars as pl

from core.common.context.polars_context import GarnetPolarsContext
from core.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from core.common.helpers.steps.polars_step import PolarsStep


class MigrationsParser(PolarsStep):
    """Example for custom step"""

    async def process(self, ctx: GarnetPolarsContext, df: PolarsDataFrame) -> PolarsDataFrame:
        df = df.select(["company", "year", "from", "to"])
        df = df.filter(pl.col("company") != "Bing")
        return df
