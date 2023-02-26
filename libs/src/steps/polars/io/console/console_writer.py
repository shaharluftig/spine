from typing import Tuple

from polars import LazyFrame

from core.src.common.context.implementations.polars_context import CardoPolarsContext
from core.src.common.helpers.steps.polars_step import PolarsStep, PolarsDataFrame


class ConsoleWriter(PolarsStep):
    """Prints dataframes to console"""

    async def process(self, ctx: CardoPolarsContext, *dfs: PolarsDataFrame) -> Tuple[PolarsDataFrame]:
        ctx.logger.info("Writing to console")
        for df in dfs:
            if isinstance(df, LazyFrame):
                df = df.collect()
            print(df)
        return dfs
