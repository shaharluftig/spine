from core import BaseContext
from core.src.workflows.Workflow import Workflow


class IExecutor:
    async def execute(self, ctx: BaseContext, workflow: Workflow):
        raise NotImplementedError()
