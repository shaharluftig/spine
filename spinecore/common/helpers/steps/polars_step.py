from typing import Union, Tuple

from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from spinecore.common.helpers.contract.IStep import IStep


class PolarsStep(IStep):
    """IStep implementation for polars steps"""

    async def process(self, ctx: SpinePolarsContext, df: Union[PolarsDataFrame, Tuple[PolarsDataFrame]]) \
            -> Union[PolarsDataFrame, Tuple[PolarsDataFrame]]:
        raise NotImplementedError
