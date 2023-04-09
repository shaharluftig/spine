from typing import Union, Tuple

import pandas as pd
from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame
from spinecore.common.helpers.steps.pandas_step import PandasStep


class SQLReader(PandasStep):
    """A Generic SQL Database reader"""

    def __init__(self, sql_query: str, connection):
        self.sql_query = sql_query
        self.connection = connection

    async def process(self, ctx: SpinePandasContext, df: Union[PandasDataFrame, Tuple[PandasDataFrame]] = None) \
            -> Union[PandasDataFrame, Tuple[PandasDataFrame]]:
        ctx.logger.info(f"Querying: ({self.sql_query})")
        return pd.read_sql(self.sql_query, self.connection)
