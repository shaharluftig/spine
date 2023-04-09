from typing import Union, Tuple

from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.contract.IStep import IStep
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame


class PandasStep(IStep):
    """IStep implementation for pandas steps"""

    async def process(self, ctx: SpinePandasContext, df: Union[PandasDataFrame, Tuple[PandasDataFrame]]) \
            -> Union[PandasDataFrame, Tuple[PandasDataFrame]]:
        raise NotImplementedError
