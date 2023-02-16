from typing import List

import networkx as nx

from src.core.workflows.Workflow import Workflow
from src.libs.IStep import IStep


class DagWorkflow(Workflow):

    def __init__(self):
        super().__init__(nx.DiGraph())

    def add_after(self, next_steps: List[IStep], prev_step: IStep):
        self.graph.add_nodes_from(next_steps)
        self.graph.add_edges_from([(prev_step, next_step) for next_step in next_steps])

    def add_last(self, *next_steps: IStep):
        leaf_nodes = self._get_leaf_nodes()
        self.graph.add_nodes_from(next_steps)
        if leaf_nodes:
            for node in next_steps:
                self.graph.add_edges_from([(leaf_node, node) for leaf_node in leaf_nodes])

    def _get_leaf_nodes(self):
        return [node for node in self.graph.nodes() if self.graph.out_degree(node) == 0]

    def to_list(self):
        return list(nx.algorithms.topological_sort(self.graph))

    def get_before(self, step: IStep = None):
        if step is None:
            return self._get_leaf_nodes()
        else:
            return list(self.graph.predecessors(step))
