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
            from matplotlib import rcParams
            rcParams.update({'figure.autolayout': True})
            style = style if style else default_dag_style
            nx.draw_networkx(self.graph, pos=topological_pos(self.graph), **style)
            plt.show()
        except ImportError:
            raise ImportError("matplotlib must be installed in order to show graph")
