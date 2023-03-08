from abc import ABC
from typing import List

import networkx as nx

from spinecore.common.helpers.contract.IStep import IStep
from spinecore.common.helpers.graphs import topological_pos, default_dag_style


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
        try:
            from matplotlib import pyplot as plt
            style = style if style else default_dag_style
            ax1 = plt.subplot()
            ax1.margins(0.15)
            nx.draw_networkx(self.graph, ax=ax1,
                             pos=topological_pos(self.graph), **style)
            plt.show()
        except ImportError:
            raise ImportError("matplotlib must be installed in order to show graph")
