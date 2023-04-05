from abc import ABC
from typing import List

from spinecore.common.helpers.contract.IStep import IStep


class Workflow(ABC):
    """Abstract class that represents general spine workflow"""

    def __init__(self, name: str, graph):
        self.name = name
        self.graph = graph

    def add_after(self, next_steps: List[IStep], prev_step: List[IStep]):
        """Add step after another"""
        raise NotImplementedError()

    def add_last(self, next_step: IStep):
        """Push step to the end of the workflow"""
        raise NotImplementedError()

    def flat(self):
        """Return flatten representation of the workflow"""
        raise NotImplementedError()

    def get_before(self, step=None):
        """Get the previous step"""
        raise NotImplementedError()

    def get_all_sub_workflows(self) -> List:
        raise NotImplementedError

    def show_workflow(self, style: dict = None) -> None:
        raise NotImplementedError
