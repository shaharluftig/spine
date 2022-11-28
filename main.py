from executor.common.context.cardo_context import CardoContext
from executor.workflows.dag_workflow import DagWorkflow
from executor.workflows.executors.async_executor import AsyncExecutor
from executor.workflows.executors.workflow_executor import WorkflowExecutor
from libs.steps.AddColumn import AddColumn
from libs.steps.HiveReader import HiveReader
from libs.steps.HiveWriter import HiveWriter


def __setup_steps():
    hive_writer = HiveWriter()
    hive_writer2 = HiveWriter()
    hive_reader = HiveReader()
    add_column = AddColumn()
    return hive_reader, add_column, hive_writer, hive_writer2


def workflow_factory():
    workflow = DagWorkflow()
    hive_reader, add_column, hive_writer, hive_writer2 = __setup_steps()
    workflow.add_last(hive_reader)
    workflow.add_after([hive_writer], hive_reader)
    workflow.add_after([add_column], hive_reader)
    workflow.add_after([hive_writer2], add_column)
    return workflow


def main():
    cardo_context = CardoContext().get_context("local")
    workflow = workflow_factory()
    WorkflowExecutor(AsyncExecutor()).process(workflow, cardo_context)


if __name__ == '__main__':
    main()
