from typing import Dict

from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class HdfsWriter(SparkStep):
    def __init__(self, path: str, mode: str, format='parquet', partitionBy: str = None, options: Dict = None):
        self.path = path
        self.format = format
        self.mode = mode
        self.partitionBy = partitionBy
        self.options = options or {}

    async def process(self, ctx: GarnetSparkContext, df: SparkDataFrame):
        try:
            ctx.spark.catalog.refreshByPath(self.path)
            df.write.save(self.path, self.format, self.mode, self.partitionBy, **self.options)
            ctx.logger.info(f"wrote datfaframe to {self.path}")
            return df
        except Exception as e:
            ctx.logger.error(f"failed to write dataframe to {self.path}. {type(e)}: {str(e)}")
