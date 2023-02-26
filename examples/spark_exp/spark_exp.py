import asyncio

from pyspark.sql import SparkSession

from core import DagWorkflow, execute
from core.src.common.context.implementations.spark_context import CardoSparkContext
from libs.src.steps.spark.io.console.console_writer import ConsoleWriter
from libs.src.steps.spark.io.csv.csv_reader import CsvReader


def __setup_steps():
    rent_reader = CsvReader("./resources/rent.csv", has_headers=True)
    names_reader = CsvReader("./resources/names.csv", has_headers=True)
    console_output = ConsoleWriter()
    return rent_reader, names_reader, console_output


def workflow_factory():
    workflow = DagWorkflow("SparkExample")
    rent_reader, names_reader, console_output = __setup_steps()
    workflow.add_last(rent_reader, names_reader)
    workflow.add_after([console_output], [rent_reader, names_reader])

    return workflow


async def main():
    spark_session = SparkSession.builder.master("local").getOrCreate()
    ctx = CardoSparkContext.get_context(spark_session)
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
