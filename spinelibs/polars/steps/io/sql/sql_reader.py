from typing import Literal

import polars as pl

from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from spinecore.common.helpers.steps.polars_step import PolarsStep


class SQLReader(PolarsStep):
    """A Generic SQL Database reader"""

    def __init__(self, sql_query: list[str] | str, connection_string: str, partition_on: str = None,
                 engine: Literal["adbc", "connectorx"] = "connectorx"):
        self.engine = engine
        self.sql_query = sql_query
        self.partition_on = partition_on
        self.connection_string = connection_string

    async def process(self, ctx: SpinePolarsContext, df: PolarsDataFrame = None) -> PolarsDataFrame:
        ctx.logger.info(f"Querying: ({self.sql_query}) using: {self.connection_string}")
        df = pl.read_database(query=self.sql_query, connection_uri=self.connection_string,
                              partition_on=self.partition_on,
                              engine=self.engine)
        return df.lazy() if ctx.lazy else df
