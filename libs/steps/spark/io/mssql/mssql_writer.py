from typing import Dict

from libs.steps.spark.io.jdbc.jdbc_writer import JDBCWriter


class MSSQLWriter(JDBCWriter):
    properties = {"driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"}

    def __init__(self, table_name: str, connection_string: str, mode: str, properties: Dict = None,
                 batch_size: int = 50000):
        super(MSSQLWriter, self).__init__(table_name,
                                          connection_string,
                                          mode,
                                          dict(MSSQLWriter.properties, **properties or {}),
                                          batch_size)
