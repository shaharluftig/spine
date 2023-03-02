from typing import Dict

from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class JDBCWriter(SparkStep):
    def __init__(self, table_name: str, connection_string: str, mode: str, properties: Dict, batchsize: int = 50000):
        self.table_name = table_name
        self.connection_string = connection_string
        self.mode = mode
        self.properties = properties
        self.properties.update({"batchsize": str(batchsize)})

    async def process(self, ctx: GarnetSparkContext, df: SparkDataFrame):
        df.write.jdbc(
            self.connection_string,
            self.table_name,
            self.mode,
            properties=self.properties
        )
        ctx.logger.info(
            'wrote dataframe data using {reader} to {table_name} using connection string: {connection_string} in mode: {mode} successfully'.format(
                reader=self.__class__.__name__, table_name=self.table_name, connection_string=self.connection_string,
                mode=self.mode))
        return df
