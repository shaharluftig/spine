from core.common.context import BaseContext
from core.workflows.Workflow import Workflow


class IExecutor:
    async def execute(self, ctx: BaseContext, workflow: Workflow) -> dict:
        raise NotImplementedError()
