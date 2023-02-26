from typing import Tuple

from polars import LazyFrame

from core.common.context import CardoPolarsContext
from core.common.helpers.dataframes import PolarsDataFrame
from core.common.helpers.steps import PolarsStep


class ConsoleWriter(PolarsStep):
    """Prints dataframes to console"""

    async def process(self, ctx: CardoPolarsContext, *dfs: PolarsDataFrame) -> Tuple[PolarsDataFrame]:
        ctx.logger.info("Writing to console")
        for df in dfs:
            if isinstance(df, LazyFrame):
                df = df.collect()
            print(df)
        return dfs
