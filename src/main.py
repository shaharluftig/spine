from src.executor.common.context.implementations.cardo_context import CardoContext
from src.executor.executors.implementations.workflow_executor import WorkflowExecutor
from src.executor.workflows.implementations.dag_workflow import DagWorkflow
from src.libs.steps.add_column import AddColumn
from src.libs.steps.console_output import ConsoleOutput
from src.libs.steps.csv_reader import CsvReader


def __setup_steps():
    csv_reader = CsvReader("src/resources/rent.csv", has_headers=True)
    add_column = AddColumn()
    console_output = ConsoleOutput()

    return csv_reader, add_column, console_output


def workflow_factory():
    workflow = DagWorkflow()
    csv_reader, add_column, console_output = __setup_steps()
    workflow.add_last(csv_reader)
    workflow.add_last(add_column)
    workflow.add_last(console_output)
    return workflow


def main():
    ctx = CardoContext().get_context()
    workflow = workflow_factory()
    workflow.show_graph()
    WorkflowExecutor().execute(workflow, ctx)


if __name__ == '__main__':
    main()
