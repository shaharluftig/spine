from typing import List

from executor.common.context.cardo_context import CardoContext
from executor.contract.IExecutor import IExecutor
from executor.contract.IWorkflow import IWorkflow
from libs.IStep import IStep


class AsyncExecutor(IExecutor):
    def execute(self, workflow: IWorkflow, cardo_context: CardoContext):
        graph_list: List[IStep] = workflow.to_list()
        pass
