from core import IStep, DataFrame, CardoContext
from typing import Tuple


class ConsoleWriter(IStep):
    """Prints dataframes to console"""

    async def process(self, cardo_context: CardoContext, *dfs: DataFrame) -> Tuple[DataFrame]:
        cardo_context.logger.info("Writing to console")
        for df in dfs:
            df.show()
        return dfs
