from typing import Dict

from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.steps.spark_step import SparkStep


class HdfsWriter(SparkStep):
    def __init__(self, path: str, mode: str, format='parquet', partitionBy: str = None, options: Dict = None):
        self.path = path
        self.format = format
        self.mode = mode
        self.partitionBy = partitionBy
        self.options = options or {}

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame):
        try:
            ctx.spark.catalog.refreshByPath(self.path)
            df.write.save(self.path, self.format, self.mode, self.partitionBy, **self.options)
            ctx.logger.info(f"Wrote dataframe to HDFS: {self.path}")
            return df
        except Exception as e:
            ctx.logger.error(f"Failed to write dataframe to HDFS: {self.path}. {type(e)}: {str(e)}")
