from typing import List

import networkx as nx

from core.src.workflows.Workflow import Workflow
from core.src.common.helpers.IStep import IStep


class DagWorkflow(Workflow):

    def __init__(self):
        super().__init__(nx.DiGraph())

    def add_after(self, next_steps: List[IStep], prev_step: List[IStep]) -> None:
        self.graph.add_nodes_from(next_steps)
        for next_step in next_steps:
            self.graph.add_edges_from([(prev_step, next_step) for prev_step in prev_step])

    def add_last(self, *next_steps: IStep) -> None:
        leaf_nodes = self.__get_leaf_nodes()
        self.graph.add_nodes_from(next_steps)
        if leaf_nodes:
            for node in next_steps:
                self.graph.add_edges_from([(leaf_node, node) for leaf_node in leaf_nodes])

    def __get_leaf_nodes(self):
        """Returns an iterator over leaf in current graph"""
        return iter([node for node in self.graph.nodes() if self.graph.out_degree(node) == 0])

    def flat_graph(self):
        """Returns a generator of nodes in topologically sorted order"""
        return nx.algorithms.topological_sort(self.graph)

    def get_before(self, step: IStep = None):
        """Returns an iterator over predecessor nodes of n"""
        if step is None:
            return self.__get_leaf_nodes()
        else:
            return self.graph.predecessors(step)
