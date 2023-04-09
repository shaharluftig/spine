from typing import Union, Tuple

from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame
from spinecore.common.helpers.steps.pandas_step import PandasStep


class MigrationsParser(PandasStep):
    """Example for custom step"""

    async def process(self, ctx: SpinePandasContext, df: Union[PandasDataFrame, Tuple[PandasDataFrame]]) -> Union[
        PandasDataFrame, Tuple[PandasDataFrame]]:
        df = df[["company", "year", "from", "to"]]
        df = df.where(df["company"] != "Bing")
        return df
