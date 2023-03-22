import polars as pl

from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from spinecore.common.helpers.steps.polars_step import PolarsStep


class   MigrationsParser(PolarsStep):
    """Example for custom step"""

    async def process(self, ctx: SpinePolarsContext, df: PolarsDataFrame) -> PolarsDataFrame:
        df = df.select(["company", "year", "from", "to"])
        df = df.filter(pl.col("company") != "Bing")
        return df
