from abc import ABC
from typing import List

import networkx as nx
from matplotlib import pyplot as plt

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
        # TODO : Export this style to config
        default_style = {
            "arrows": True,
            "arrowsize": 30,
            "bbox": dict(facecolor="skyblue",
                         boxstyle="round", ec="silver", pad=0.3),
            "edge_color": "gray"
        }
        style = style if style else default_style
        nx.draw_networkx(self.graph, **style)
        plt.show()
