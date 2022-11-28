import uuid

from pyspark.sql import SparkSession

from executor.contract.IContext import IContext


class CardoContext(IContext):
    def __init__(self):
        self.spark = None
        self.run_id = uuid.uuid1()

    def get_context(self, master: str, spark_config=None):
        if not self.spark:
            self.spark = SparkSession.builder.master(master).getOrCreate()
        return self.spark
