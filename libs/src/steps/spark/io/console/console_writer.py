from core import IStep, DataFrame, CardoContext


class ConsoleWriter(IStep):
    """Prints dataframes to console"""

    async def process(self, ctx: CardoContext, *dfs: DataFrame) -> DataFrame:
        ctx.logger.info("Writing to console")
        for df in dfs:
            df.show()
        return df
