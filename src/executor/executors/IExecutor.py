from src.executor.common.context.IContext import IContext
from src.executor.workflows.IWorkflow import IWorkflow


class IExecutor:
    def execute(self, workflow: IWorkflow, cardo_context: IContext):
        raise NotImplementedError()
