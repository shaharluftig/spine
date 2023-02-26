from typing import Union, Tuple

from core.common.context.implementations.polars_context import CardoPolarsContext
from core.common.helpers.dataframes import PolarsDataFrame
from core.common.helpers.steps.IStep import IStep


class PolarsStep(IStep):
    async def process(self, ctx: CardoPolarsContext, df: Union[PolarsDataFrame, Tuple[PolarsDataFrame]]) \
            -> Union[PolarsDataFrame, Tuple[PolarsDataFrame]]:
        raise NotImplementedError
