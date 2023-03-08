from spinelibs.spark.steps.io.jdbc.jdbc_reader import JDBCReader


class MSSQLReader(JDBCReader):
    def __init__(self, query: str, connection_string: str, username: str = None, password: str = None,
                 num_partitions: int = 40, fetch_size: int = 50000):
        driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
        super().__init__(query, connection_string, username, password, driver, num_partitions, fetch_size)
