from core import IStep, CardoContext, DataFrame


class CSVWriter(IStep):
    """Local CSV file writer"""

    def __init__(self, path: str, has_headers: bool = True, sep: str = ",", batch_size: int = 1024):
        self.headers = has_headers
        self.path = path
        self.sep = sep
        self.batch_size = batch_size

    async def process(self, cardo_context: CardoContext, df: DataFrame = None) -> DataFrame:
        cardo_context.logger.info(f"Writing CSV to {self.path} with headers={self.headers}")
        df.write_csv(self.path, has_header=self.headers, batch_size=self.batch_size, sep=self.sep)
        return df
