from typing import Literal

from core.common.context.polars_context import GarnetPolarsContext
from core.common.helpers.dataframes.polars_dataframe import PolarsDataFrame
from core.common.helpers.steps.polars_step import PolarsStep


class SQLWriter(PolarsStep):
    """A Generic SQL Database writer
        Parameters
        ----------
        connection_string
            Connection uri, for example
            * "postgresql://username:password@server:port/database"
        if_exists : {'append', 'replace', 'fail'}
            The insert mode.
            'replace' will create a new database table, overwriting an existing one.
            'append' will append to an existing table.
            'fail' will fail if table already exists.
        engine : {'sqlalchemy', 'adbc'}
    """

    def __init__(self, table_name, connection_string: str,
                 if_exists: Literal["replace", "append", "fail"] = "replace",
                 engine: Literal["sqlalchemy", "adbc"] = "sqlalchemy"):
        self.table_name = table_name
        self.connection_string = connection_string
        self.engine = engine
        self.if_exists = if_exists

    async def process(self, ctx: GarnetPolarsContext, df: PolarsDataFrame = None) -> PolarsDataFrame:
        ctx.logger.info(f"Writing to table: {self.table_name} using: {self.connection_string}]")
        df = df.collect() if ctx.lazy else df
        df.write_database(self.table_name, self.connection_string, if_exists=self.if_exists, engine=self.engine)
        return df
