from core import IStep, DataFrame, CardoContext


class ConsoleWriter(IStep):
    async def process(self, cardo_context: CardoContext, *dfs: DataFrame) -> DataFrame:
        cardo_context.logger.info("Writing to console")
        for df in dfs:
            df.show()
        return df
