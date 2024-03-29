import asyncio

from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.executors import execute
from spinecore.workflows import DagWorkflow
from spinelibs.spark.steps.io.console.console_writer import ConsoleWriter
from spinelibs.spark.steps.io.csv.csv_reader import CsvReader


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
    ctx = SpineSparkContext.get_context(spark_config={"spark.executor.memory": "1gb"})  # Example config
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
