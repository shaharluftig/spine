from polars import LazyFrame

from core import IStep, DataFrame, CardoContext


class ConsoleWriter(IStep):
    """Prints dataframes to console"""

    async def process(self, ctx: CardoContext, *dfs: DataFrame) -> DataFrame:
        ctx.logger.info("Writing to console")
        for df in dfs:
            if isinstance(df, LazyFrame):
                df = df.collect()
            print(df)
        return dfs
