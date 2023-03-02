from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from core.common.helpers.steps import SparkStep


class JDBCReader(SparkStep):
    def __init__(self, table_name: str, connection_string: str, properties: {}, parallel_col: str = None,
                 lower_bound: str = None, upper_bound: str = None, num_parallel: int = None, fetch_size: int = 50000):
        self.table_name = table_name
        self.connection_string = connection_string
        self.properties = properties
        self.properties.update({"fetchsize": str(fetch_size)})
        self.parallel_col = parallel_col
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_parallel = num_parallel

    async def process(self, ctx: GarnetSparkContext, df: SparkDataFrame = None):
        df = ctx.spark.read.jdbc(
            self.connection_string,
            self.table_name,
            column=self.parallel_col,
            lowerBound=self.lower_bound,
            upperBound=self.upper_bound,
            numPartitions=self.num_parallel,
            properties=self.properties
        )
        ctx.logger.info(
            u'read data with {reader} from table {table_name} using connection string : {connection_string} properties: {properties}'.format(
                reader=self.__class__.__name__, table_name=self.table_name, connection_string=self.connection_string,
                properties=self.properties))
        return df
