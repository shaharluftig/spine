import networkx as nx
from matplotlib import pyplot as plt

from executor.workflows.workflow import Workflow
from libs.steps.AddColumn import AddColumn
from libs.steps.HiveReader import HiveReader
from libs.steps.HiveWriter import HiveWriter


def workflow_factory():
    workflow = Workflow()
    hive_writer = HiveWriter()
    hive_writer2 = HiveWriter()
    hive_reader = HiveReader()
    add_column = AddColumn()
    workflow.add_last(hive_reader)
    workflow.add_after([hive_writer], hive_reader)
    workflow.add_after([add_column], hive_reader)
    workflow.add_after([hive_writer2], add_column)

    nx.draw(workflow.graph, with_labels=True)
    plt.show()
    return workflow


def main():
    # cardo_context = CardoContext().get_context("local")
    workflow = workflow_factory()


if __name__ == '__main__':
    main()
