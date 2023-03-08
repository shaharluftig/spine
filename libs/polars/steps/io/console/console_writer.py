from typing import Tuple

from core.common.context.polars_context import GarnetPolarsContext
from core.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from core.common.helpers.steps.polars_step import PolarsStep


class ConsoleWriter(PolarsStep):
    """Prints dataframes to console"""

    async def process(self, ctx: GarnetPolarsContext, *dfs: PolarsDataFrame) -> Tuple[PolarsDataFrame]:
        ctx.logger.info("Writing to console")
        for df in dfs:
            df = df.collect() if ctx.lazy else df
            print(df)
        return dfs
