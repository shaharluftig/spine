import asyncio

from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.executors.implementations.workflow_executor import WorkflowExecutor
from core.src.workflows.implementations.dag_workflow import DagWorkflow
from libs.src.steps.polars.io.console_writer import ConsoleWriter
from libs.src.steps.polars.io.csv_reader import CsvReader


def __setup_steps():
    rent_reader = CsvReader("../polars_exp/resources/rent.csv", has_headers=True)
    names_reader = CsvReader("../polars_exp/resources/names.csv", has_headers=True)
    console_output = ConsoleWriter()
    return rent_reader, names_reader, console_output


def workflow_factory():
    workflow = DagWorkflow()
    rent_reader, names_reader, console_output = __setup_steps()
    workflow.add_last(rent_reader, names_reader)
    workflow.add_after([console_output], [rent_reader])
    workflow.add_after([console_output], [names_reader])
    return workflow


async def main():
    ctx = CardoContext().get_context()
    workflow = workflow_factory()
    await WorkflowExecutor(ctx).execute(workflow)


if __name__ == '__main__':
    asyncio.run(main())
