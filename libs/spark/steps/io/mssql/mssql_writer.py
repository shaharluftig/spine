from libs.spark.steps.io.jdbc.jdbc_writer import JDBCWriter


class MSSQLWriter(JDBCWriter):
    def __init__(self, table_name: str, connection_string: str, mode: str = "overwrite", username: str = None,
                 password: str = None, num_partitions: int = 40, batch_size: int = 50000):
        driver = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
        super().__init__(table_name, mode, connection_string, username, password, driver, num_partitions, batch_size)
