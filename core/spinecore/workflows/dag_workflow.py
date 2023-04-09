from typing import List, Iterable

import networkx as nx

from spinecore.common.helpers.contract.IStep import IStep
from spinecore.common.helpers.contract.Workflow import Workflow
from spinecore.common.helpers.graphs import topological_pos, default_dag_style


class DagWorkflow(Workflow):
    """DAG (Directed Acyclic Graph) Implementation of Workflow"""

    def __init__(self, workflow_name: str, graph: nx.DiGraph = None):
        if not graph:
            graph = nx.DiGraph(name=workflow_name)
        super().__init__(workflow_name, graph=graph)

    def add_after(self, next_steps: List[IStep], prev_step: List[IStep]) -> None:
        self.graph.add_nodes_from(next_steps)
        for next_step in next_steps:
            self.graph.add_edges_from([(prev_step, next_step) for prev_step in prev_step])

    def add_last(self, *next_steps: IStep) -> None:
        leaf_nodes = self.__get_leaf_nodes()
        self.graph.add_nodes_from(next_steps)
        if leaf_nodes:
            for node in next_steps:
                self.graph.add_edges_from([(leaf_node, node)
                                           for leaf_node in leaf_nodes])

    def __get_leaf_nodes(self) -> Iterable[List]:
        """Returns an iterator over leaf in current graph"""
        return iter([node for node in self.graph.nodes()
                     if self.graph.out_degree(node) == 0])

    def flat(self) -> List:
        """Returns a generator of nodes in topologically sorted order"""
        return nx.algorithms.topological_sort(self.graph)

    def get_all_sub_workflows(self) -> Iterable:
        """Returns all the sub workflows"""
        return iter([DagWorkflow(f"{self.name}", self.graph.subgraph(c).copy()) for c in
                     nx.weakly_connected_components(self.graph)])

    def get_before(self, step: IStep = None):
        """Returns an iterator over predecessor nodes of n"""
        if step is None:
            return self.__get_leaf_nodes()
        return self.graph.predecessors(step)

    def show_workflow(self, style: dict = None) -> None:
        try:
            from matplotlib import pyplot as plt
            from matplotlib import rcParams
            rcParams.update({'figure.autolayout': True})
            style = style if style else default_dag_style
            nx.draw_networkx(self.graph, pos=topological_pos(self.graph), **style)
            plt.show()
        except ImportError:
            raise ImportError("matplotlib must be installed in order to show graph")
