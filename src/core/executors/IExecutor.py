from src.core.common.context.IContext import IContext
from src.core.workflows.Workflow import Workflow


class IExecutor:
    def execute(self, workflow: Workflow, cardo_context: IContext):
        raise NotImplementedError()
