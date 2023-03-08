from typing import Union, Tuple

from core.common.context.polars_context import GarnetPolarsContext
from core.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from core.common.helpers.contract.IStep import IStep


class PolarsStep(IStep):
    async def process(self, ctx: GarnetPolarsContext, df: Union[PolarsDataFrame, Tuple[PolarsDataFrame]]) \
            -> Union[PolarsDataFrame, Tuple[PolarsDataFrame]]:
        raise NotImplementedError
