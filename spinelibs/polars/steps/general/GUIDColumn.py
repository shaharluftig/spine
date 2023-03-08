from typing import List

import polars as pl

from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from spinecore.common.helpers.steps.polars_step import PolarsStep


class GUIDColumn(PolarsStep):
    def __init__(self, column_to_hash: List[str], guid_column_name: str):
        self.guid_column_name = guid_column_name
        self.column_to_hash = column_to_hash

    async def process(self, ctx: SpinePolarsContext, df: PolarsDataFrame) -> PolarsDataFrame:
        ctx.logger.info(f"Creating GUID Coulmn ['{self.guid_column_name}'] using {self.column_to_hash}")
        return df.with_columns([pl.concat_str(*self.column_to_hash).hash().cast(pl.Utf8).alias(self.guid_column_name)])
