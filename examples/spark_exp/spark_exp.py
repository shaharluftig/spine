import asyncio

from core.common.context import GarnetSparkContext
from core.executors import execute
from core.workflows import DagWorkflow
from libs.steps.spark.io.console.console_writer import ConsoleWriter
from libs.steps.spark.io.csv.csv_reader import CsvReader


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
    ctx = GarnetSparkContext.get_context(spark_config={"spark.executor.memory": "1gb"})  # Example config
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
