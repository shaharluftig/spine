from core import IStep, DataFrame, CardoContext
from typing import Tuple


class ConsoleWriter(IStep):
    """Prints dataframes to console"""

    async def process(self, ctx: CardoContext, *dfs: DataFrame) -> Tuple[DataFrame]:
        ctx.logger.info("Writing to console")
        for df in dfs:
            df.show()
        return dfs
