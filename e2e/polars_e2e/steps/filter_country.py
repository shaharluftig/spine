from typing import Union, Tuple, List

import polars as pl
from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from spinecore.common.helpers.steps.polars_step import PolarsStep


class FilterCountry(PolarsStep):
    def __init__(self, country_to_remove: List[str]):
        self.country_to_remove = country_to_remove

    async def process(self, ctx: SpinePolarsContext, df: Union[PolarsDataFrame, Tuple[PolarsDataFrame]]) -> Union[
        PolarsDataFrame, Tuple[PolarsDataFrame]]:
        return df.filter(~pl.col("country").is_in(self.country_to_remove))
