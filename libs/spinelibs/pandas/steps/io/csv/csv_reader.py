from typing import Union, Tuple

import pandas as pd
from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame
from spinecore.common.helpers.steps.pandas_step import PandasStep


class CsvReader(PandasStep):
    """Local CSV file reader"""

    def __init__(self, path: str, headers: int = "infer", lazy: bool = True):
        self.headers = headers
        self.lazy = lazy
        self.path = path

    async def process(self, ctx: SpinePandasContext, df: Union[PandasDataFrame, Tuple[PandasDataFrame]] = None) -> \
    Union[
        PandasDataFrame, Tuple[PandasDataFrame]]:
        ctx.logger.info(f"Reading {self.path} with headers={self.headers}")
        df = pd.read_csv(self.path, header=self.headers)
        return df
