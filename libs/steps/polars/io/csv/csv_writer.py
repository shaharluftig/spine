from core.common.context import GarnetPolarsContext
from core.common.helpers.dataframes import PolarsDataFrame
from core.common.helpers.steps import PolarsStep


class CSVWriter(PolarsStep):
    """Local CSV file writer"""

    def __init__(self, path: str, has_headers: bool = True, sep: str = ",", batch_size: int = 1024):
        self.headers = has_headers
        self.path = path
        self.sep = sep
        self.batch_size = batch_size

    async def process(self, ctx: GarnetPolarsContext, df: PolarsDataFrame = None) -> PolarsDataFrame:
        ctx.logger.info(f"Writing CSV to {self.path} with headers={self.headers}")
        writer = df.collect().write_csv if ctx.lazy else df.write_csv
        writer(self.path, has_header=self.headers, batch_size=self.batch_size, sep=self.sep)
        return df
