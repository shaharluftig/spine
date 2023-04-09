from typing import Tuple, Union

from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame
from spinecore.common.helpers.steps.pandas_step import PandasStep


class ConsoleWriter(PandasStep):
    """Prints dataframes to console"""

    async def process(self, ctx: SpinePandasContext, *dfs: Union[PandasDataFrame, Tuple[PandasDataFrame]]) \
            -> Union[PandasDataFrame, Tuple[PandasDataFrame]]:
        ctx.logger.info("Writing to console")
        for df in dfs:
            print(df)
        return dfs
