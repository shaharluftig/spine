from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.workflows.Workflow import Workflow


class IExecutor:
    async def execute(self, ctx: CardoContext, workflow: Workflow):
        raise NotImplementedError()
