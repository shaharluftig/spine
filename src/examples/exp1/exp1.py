from src.executor.common.context.implementations.cardo_context import CardoContext
from src.executor.executors.implementations.workflow_executor import WorkflowExecutor
from src.executor.workflows.implementations.dag_workflow import DagWorkflow
from src.libs.steps.add_column import AddColumn
from src.libs.steps.console_output import ConsoleOutput
from src.libs.steps.csv_reader import CsvReader


def __setup_steps():
    csv_reader = CsvReader(
        """C:\\Users\\shaha\\Programming\\Projects\\cardo2\\src\\examples\\exp1\\resources\\rent.csv""""",
        has_headers=True)
    add_column = AddColumn()
    console_output = ConsoleOutput()
    return csv_reader, add_column, console_output


def workflow_factory():
    workflow = DagWorkflow()
    csv_reader, add_column, console_output = __setup_steps()
    workflow.add_last(csv_reader)
    workflow.add_after([console_output], csv_reader)
    workflow.add_last(add_column)
    workflow.add_last(console_output)
    return workflow


def main():
    ctx = CardoContext().get_context()
    workflow = workflow_factory()
    WorkflowExecutor(ctx).execute(workflow)


if __name__ == '__main__':
    main()
