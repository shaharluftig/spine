from src.executor.common.context.IContext import IContext
from src.executor.workflows.Workflow import Workflow


class IExecutor:
    def execute(self, workflow: Workflow, cardo_context: IContext):
        raise NotImplementedError()
