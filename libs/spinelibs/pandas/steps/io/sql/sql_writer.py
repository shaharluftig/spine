from typing import Literal, Union, Tuple

from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame
from spinecore.common.helpers.steps.pandas_step import PandasStep


class SQLWriter(PandasStep):
    def __init__(self, table_name, connection,
                 if_exists: Literal["replace", "append", "fail"] = "replace"):
        self.connection = connection
        self.table_name = table_name
        self.if_exists = if_exists

    async def process(self, ctx: SpinePandasContext, df: Union[PandasDataFrame, Tuple[PandasDataFrame]]) \
            -> Union[PandasDataFrame, Tuple[PandasDataFrame]]:
        ctx.logger.info(f"Writing to table: {self.table_name}")
        df.to_sql(self.table_name, self.connection, if_exists=self.if_exists)
        return df
