from typing import Union, Tuple, List

import polars as pl

from core.common.context import CardoPolarsContext
from core.common.helpers.dataframes import PolarsDataFrame
from core.common.helpers.steps import PolarsStep


class GUIDColumn(PolarsStep):
    def __init__(self, column_to_hash: List[str], guid_column_name: str):
        self.guid_column_name = guid_column_name
        self.column_to_hash = column_to_hash

    async def process(self, ctx: CardoPolarsContext, df: Union[PolarsDataFrame, Tuple[PolarsDataFrame]]) \
            -> Union[PolarsDataFrame, Tuple[PolarsDataFrame]]:
        return df.with_columns([pl.col(*self.column_to_hash).hash().alias(self.guid_column_name)])
