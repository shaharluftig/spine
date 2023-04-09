from typing import Union, Tuple

from spinecore.common.context.pandas_context import SpinePandasContext
from spinecore.common.helpers.dataframes.pandas_dataframe import PandasDataFrame
from spinecore.common.helpers.steps.pandas_step import PandasStep


class CSVWriter(PandasStep):
    """Local CSV file writer"""

    def __init__(self, path: str, has_headers: bool = True, sep: str = ",", index: bool = False):
        self.headers = has_headers
        self.path = path
        self.sep = sep
        self.index = index

    async def process(self, ctx: SpinePandasContext, df: Union[PandasDataFrame, Tuple[PandasDataFrame]]) \
            -> Union[PandasDataFrame, Tuple[PandasDataFrame]]:
        ctx.logger.info(f"Writing CSV to {self.path} with headers={self.headers}, index={self.index}")
        df.to_csv(self.path, header=self.headers, sep=self.sep, index=self.index)
        return df
