from typing import List

from libs.IStep import IStep


class IWorkflow:

    def add_after(self, next_steps: List[IStep], prev_step: IStep):
        raise NotImplementedError()

    def add_last(self, next_step: IStep):
        raise NotImplementedError()

    def to_list(self):
        raise NotImplementedError()
