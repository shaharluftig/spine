from core.common.context.spark_context import SpineSparkContext
from core.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from core.common.helpers.steps.spark_step import SparkStep


class JDBCWriter(SparkStep):
    def __init__(self, table_name: str, mode: str, connection_string: str, username: str, password: str,
                 driver: str, num_partitions: int, batch_size: int):
        self.table_name = table_name
        self.mode = mode
        self.num_partitions = num_partitions
        self.batch_size = batch_size
        self.driver = driver
        self.password = password
        self.username = username
        self.connection_string = connection_string

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame) -> SparkDataFrame:
        ctx.logger.info(f"Writing df to table: {self.table_name} with connection string: {self.connection_string}")
        df.repartition(self.num_partitions)
        df.write.format("jdbc").mode(self.mode) \
            .option("url", self.connection_string) \
            .option("numPartitions", self.num_partitions) \
            .option("batchsize", self.batch_size) \
            .option("driver", self.driver) \
            .option("dbtable", self.table_name) \
            .option("user", self.username) \
            .option("password", self.password) \
            .save()

        return df
