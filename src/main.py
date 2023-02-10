from src.executor.common.context.implementations.cardo_context import CardoContext
from src.executor.executors.implementations.async_executor import AsyncExecutor
from src.executor.workflows.implementations.dag_workflow import DagWorkflow

from src.libs.steps.AddColumn import AddColumn
from src.libs.steps.HiveReader import HiveReader
from src.libs.steps.HiveWriter import HiveWriter


def __setup_steps():
    hive_writer = HiveWriter()
    hive_writer2 = HiveWriter()
    hive_reader = HiveReader()
    add_column = AddColumn()
    add_column2 = AddColumn()
    return hive_reader, add_column, add_column2, hive_writer, hive_writer2


def workflow_factory():
    workflow = DagWorkflow()
    hive_reader, add_column, add_column2, hive_writer, hive_writer2 = __setup_steps()
    workflow.add_last(hive_reader)
    workflow.add_after([hive_writer], hive_reader)
    workflow.add_after([add_column], hive_reader)
    workflow.add_after([add_column2], add_column)
    workflow.add_after([hive_writer2], add_column2)
    return workflow


def main():
    ctx = CardoContext().get_context()
    workflow = workflow_factory()
    workflow.show_graph()
    # AsyncExecutor().execute(workflow, ctx)



if __name__ == '__main__':
    main()
