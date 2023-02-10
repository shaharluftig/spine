from typing import List

from src.executor.common.context.implementations.cardo_context import CardoContext
from src.executor.executors.IExecutor import IExecutor
from src.executor.workflows.IWorkflow import IWorkflow
from src.libs.IStep import IStep


class AsyncExecutor(IExecutor):
    def execute(self, workflow: IWorkflow, cardo_context: CardoContext):
        dependencies = []
        graph_list: List[IStep] = workflow.to_list()
        a=1

