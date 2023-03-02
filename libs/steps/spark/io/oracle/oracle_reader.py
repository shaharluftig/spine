from typing import Dict

from libs.steps.spark.io.jdbc.jdbc_reader import JDBCReader


class OracleReader(JDBCReader):
    properties = {"driver": "oracle.jdbc.OracleDriver"}

    def __init__(self, table_name: str, connection_string: str, properties: Dict = None, parallel_col: str = None,
                 lower_bound: str = None,
                 upper_bound: str = None, num_parallel: int = None, fetch_size: int = 50000):
        super(OracleReader, self).__init__(table_name,
                                           connection_string,
                                           dict(OracleReader.properties, **properties or {}),
                                           parallel_col, lower_bound, upper_bound, num_parallel, fetch_size)
