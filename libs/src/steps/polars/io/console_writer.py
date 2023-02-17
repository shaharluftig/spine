from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.common.helpers.dataframe import DataFrame
from libs.src.IStep import IStep


class ConsoleWriter(IStep):

    async def process(self, cardo_context: CardoContext, *dfs: DataFrame) -> DataFrame:
        cardo_context.logger.info("Writing to console")
        for df in dfs:
            print(df)
        return df
