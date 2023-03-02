from typing import Dict

from core.common.context import GarnetSparkContext
from core.common.helpers.dataframes import SparkDataFrame
from libs.steps.spark.io.jdbc.jdbc_writer import JDBCWriter


class OracleWriter(JDBCWriter):
    properties = {"driver": "oracle.jdbc.OracleDriver"}

    def __init__(self, table_name: str, connection_string: str, mode: str, properties: Dict = None,
                 truncate: bool = False, batchsize: str = 50000):
        super(OracleWriter, self).__init__(table_name,
                                           connection_string,
                                           mode,
                                           dict(dict(OracleWriter.properties, **properties or {}),
                                                truncate=str(truncate).lower()),
                                           batchsize)

    @staticmethod
    def __convert_columns_to_upper_case(df: SparkDataFrame):
        columns_as_upper = map(lambda column: df[column].alias(column.upper()),
                               df.columns)
        return df.select(*columns_as_upper)

    def process(self, ctx: GarnetSparkContext, df: SparkDataFrame):
        df = self.__convert_columns_to_upper_case(df)
        super(OracleWriter, self).process(ctx, df)
        return df
