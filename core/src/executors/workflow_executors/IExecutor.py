from core import CardoContext
from core.src.workflows.Workflow import Workflow


class IExecutor:
    async def execute(self, ctx: CardoContext, workflow: Workflow):
        raise NotImplementedError()
