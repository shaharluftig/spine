from typing import Union, Tuple

from core import IStep
from core.src.common.context.implementations.polars_context import CardoPolarsContext
from core.src.common.helpers.dataframe import PolarsDataFrame


class PolarsStep(IStep):
    async def process(self, ctx: CardoPolarsContext, df: Union[PolarsDataFrame, Tuple[PolarsDataFrame]]) \
            -> Union[PolarsDataFrame, Tuple[PolarsDataFrame]]:
        raise NotImplementedError
