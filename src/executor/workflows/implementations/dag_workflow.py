from typing import List

import networkx as nx
from matplotlib import pyplot as plt

from src.executor.workflows.IWorkflow import IWorkflow
from src.libs.IStep import IStep


class DagWorkflow(IWorkflow):

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_after(self, next_steps: List[IStep], prev_step: IStep):
        self.graph.add_nodes_from(next_steps)
        self.graph.add_edges_from([(prev_step, next_step) for next_step in next_steps])

    def add_last(self, next_step: IStep):
        leaf_nodes = self._get_leaf_nodes()
        self.graph.add_node(next_step)
        if leaf_nodes:
            self.graph.add_edges_from([(leaf_node, next_step) for leaf_node in leaf_nodes])

    def _get_leaf_nodes(self):
        return [node for node in self.graph.nodes() if self.graph.out_degree(node) == 0]

    def to_list(self):
        return list(nx.algorithms.topological_sort(self.graph))

    def get_before(self, step: IStep = None):
        if step is None:
            return self._get_leaf_nodes()
        else:
            return list(self.graph.predecessors(step))

    def show_graph(self):
        nx.draw_networkx(self.graph,
                         bbox=dict(facecolor="skyblue",
                                   boxstyle="round", ec="silver", pad=0.3),
                         edge_color="gray")
        plt.show()
