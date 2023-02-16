from src.core.common.context.implementations.cardo_context import CardoContext
from src.core.executors.implementations.workflow_executor import WorkflowExecutor
from src.core.workflows.implementations.dag_workflow import DagWorkflow
from src.libs.steps.io.console_writer import ConsoleWriter
from src.libs.steps.io.csv_reader import CsvReader


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
    ctx = CardoContext().get_context()
    workflow = workflow_factory()
    WorkflowExecutor(ctx).execute(workflow)


if __name__ == '__main__':
    main()