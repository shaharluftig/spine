from pyspark.sql import SparkSession

from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.executors.implementations.workflow_executor import WorkflowExecutor
from core.src.workflows.implementations.dag_workflow import DagWorkflow
from libs.src.steps.spark.io.console_writer import ConsoleWriter
from libs.src.steps.spark.io.csv_reader import CsvReader


def __setup_steps():
    rent_reader = CsvReader("./resources/rent.csv", has_headers=True)
    names_reader = CsvReader("./resources/names.csv", has_headers=True)
    console_output = ConsoleWriter()
    return rent_reader, names_reader, console_output


def workflow_factory():
    workflow = DagWorkflow()
    rent_reader, names_reader, console_output = __setup_steps()
    workflow.add_last(rent_reader, names_reader)
    workflow.add_after([console_output], [rent_reader, names_reader])

    return workflow


def main():
    spark = SparkSession.builder.master("local").getOrCreate()
    ctx = CardoContext(spark_session=spark).get_context()
    workflow = workflow_factory()
    WorkflowExecutor(ctx).execute(workflow)


if __name__ == '__main__':
    main()
