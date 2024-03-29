from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.steps.spark_step import SparkStep


class JDBCReader(SparkStep):
    def __init__(self, query: str, connection_string: str, username: str, password: str, driver: str,
                 num_partitions: int, fetch_size: int):
        self.num_partitions = num_partitions
        self.fetch_size = fetch_size
        self.driver = driver
        self.password = password
        self.username = username
        self.connection_string = connection_string
        self.query = query

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame = None) -> SparkDataFrame:
        ctx.logger.info(f"Reading df using query: {self.query} with connection string: {self.connection_string}")
        df = ctx.spark.read.format("jdbc").option("driver", self.driver) \
            .option("url", self.connection_string) \
            .option("query", self.query) \
            .option("user", self.username) \
            .option("password", self.password) \
            .option("numPartitions", self.num_partitions) \
            .option("fetchsize", self.fetch_size) \
            .load()
        return df
