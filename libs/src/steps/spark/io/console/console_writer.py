from core import IStep, DataFrame, BaseContext
from core.src.common.helpers.dataframe import SparkDataFrame


class ConsoleWriter(IStep):
    """Prints dataframes to console"""

    async def process(self, ctx: SparkDataFrame, *dfs: DataFrame) -> DataFrame:
        ctx.logger.info("Writing to console")
        for df in dfs:
            df.show()
        return df
