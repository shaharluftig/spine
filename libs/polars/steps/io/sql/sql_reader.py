from typing import Literal

import polars as pl

from core.common.context.polars_context import GarnetPolarsContext
from core.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from core.common.helpers.steps.polars_step import PolarsStep


class SQLReader(PolarsStep):
    """A Generic SQL Database reader"""

    def __init__(self, sql_query: list[str] | str, connection_string: str, partition_on: str = None,
                 engine: Literal["adbc", "connectorx"] = "connectorx"):
        self.engine = engine
        self.sql_query = sql_query
        self.partition_on = partition_on
        self.connection_string = connection_string

    async def process(self, ctx: GarnetPolarsContext, df: PolarsDataFrame = None) -> PolarsDataFrame:
        ctx.logger.info(f"Querying: ({self.sql_query}) using: {self.connection_string}")
        df = pl.read_database(query=self.sql_query, connection_uri=self.connection_string,
                              partition_on=self.partition_on,
                              engine=self.engine)
        return df.lazy() if ctx.lazy else df
