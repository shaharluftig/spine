from executor.contract.IContext import IContext
from executor.contract.IWorkflow import IWorkflow


class IExecutor:
    def execute(self, workflow: IWorkflow, cardo_context: IContext):
        raise NotImplementedError()
