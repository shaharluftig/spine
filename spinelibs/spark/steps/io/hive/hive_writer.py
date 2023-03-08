import pyspark.sql.functions as F
from pyspark.sql import Window

from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.common.helpers.dataframes.spark_dataframe import SparkDataFrame
from spinecore.common.helpers.steps.spark_step import SparkStep

TMP_COL = '___tmp___'
ROW_NUM_COL = '___row_num___'


class HiveWriter(SparkStep):
    def __init__(
            self, table_name: str, file_format: str = 'parquet',
            mode: str = 'overwrite', partition_by: str = None, overwrite_partition: str = False,
            num_partitions: str = None,
            is_new_partitions: str = False,
            **kwargs):
        self.table_name = table_name
        self.file_format = file_format
        self.mode = mode
        self.partition_by = partition_by
        self.kwargs = kwargs
        self.overwrite_partition = overwrite_partition
        self.num_partitions = num_partitions
        self.is_new_partitions = is_new_partitions

    async def process(self, ctx: SpineSparkContext, df: SparkDataFrame):
        try:
            if self.overwrite_partition:
                self._handle_partition_overwriting(ctx, df)
            else:
                df.write.saveAsTable(self.table_name, mode=self.mode, format=self.file_format,
                                     partitionBy=self.partition_by, **self.kwargs)
                ctx.logger.info(
                    f"Wrote table: {self.table_name} to Hive MetaStore. mode: {self.mode}, format: {self.file_format}")
        except Exception as e:
            ctx.logger.error(
                f'Failed to write table {self.table_name} to Hive. {type(e)}: {str(e)}')
            raise

        return df

    def _handle_partition_overwriting(self, ctx: SpineSparkContext, df: SparkDataFrame):
        self._validate_overwrite_partitions_params()
        ctx.spark.conf.set('spark.sql.sources.partitionOverwriteMode', 'dynamic')
        ctx = ctx.repartition(self.num_partitions)
        ctx.logger.info('set partitionOverwriteMode to dynamic')
        if self.is_new_partitions:
            self._write_one_row_per_partitions(df)
        df.select(self._get_target_table_columns(ctx)).write.insertInto(self.table_name, True)

    def _get_target_table_columns(self, cardo_context):
        return cardo_context.spark.table(self.table_name).columns

    def _validate_overwrite_partitions_params(self):
        if self.mode != 'overwrite_partitions':
            raise Exception("In order to overwrite partitions you must set mode to 'overwrite_partitions'")
        if self.num_partitions is None or self.partition_by is None:
            raise Exception("You must specify num partitions and partitions columns in partitionOverwriteMode")

    def _write_one_row_per_partitions(self, df):
        w = Window.partitionBy(self.partition_by).orderBy(TMP_COL)
        df.persist()
        tmp_df = df.withColumn(TMP_COL, F.lit(1)).withColumn(ROW_NUM_COL, F.row_number().over(w))
        tmp_df = tmp_df.where('{} = 1'.format(ROW_NUM_COL)).drop(ROW_NUM_COL).drop(TMP_COL)
        tmp_df.write.mode('append').partitionBy(self.partition_by).saveAsTable(self.table_name)
