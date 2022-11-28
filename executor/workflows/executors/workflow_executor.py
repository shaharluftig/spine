from executor.common.context.cardo_context import CardoContext
from executor.contract.IExecutor import IExecutor
from executor.workflows.dag_workflow import DagWorkflow


class WorkflowExecutor:
    def __init__(self, executor: IExecutor):
        self.executor = executor

    def process(self, workflow: DagWorkflow, context: CardoContext):
        return self.executor.execute(workflow, context)
