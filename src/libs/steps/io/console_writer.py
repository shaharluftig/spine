from src.core.common.context.implementations.cardo_context import CardoContext
from src.core.helpers.dataframe import DataFrame
from src.libs.IStep import IStep


class ConsoleWriter(IStep):
    def process(self, cardo_context: CardoContext, *dfs: DataFrame) -> DataFrame:
        cardo_context.logger.info("Writing to console")
        for df in dfs:
            print(df)
        return df
