from core.src.common.context.IContext import IContext
from core.src.workflows.Workflow import Workflow


class IExecutor:
    def execute(self, workflow: Workflow, cardo_context: IContext):
        raise NotImplementedError()
