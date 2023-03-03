from abc import ABC
from typing import List

import networkx as nx
from matplotlib import pyplot as plt

from core.common.helpers.graphs import topological_pos, default_dag_style
from core.common.helpers.steps.IStep import IStep


class Workflow(ABC):
    def __init__(self, name: str, graph):
        self.name = name
        self.graph = graph

    def add_after(self, next_steps: List[IStep], prev_step: List[IStep]):
        raise NotImplementedError()

    def add_last(self, next_step: IStep):
        raise NotImplementedError()

    def flat_graph(self):
        raise NotImplementedError()

    def get_before(self, step=None):
        raise NotImplementedError()

    def show_graph(self, style: dict = None) -> None:
        style = style if style else default_dag_style
        ax1 = plt.subplot()
        ax1.margins(0.15)
        nx.draw_networkx(self.graph, ax=ax1,
                         pos=topological_pos(self.graph), **style)
        plt.show()
