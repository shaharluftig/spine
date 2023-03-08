from core.common.context.base_context import BaseContext
from core.common.helpers.contract.Workflow import Workflow


class IExecutor:
    async def execute(self, ctx: BaseContext, workflow: Workflow) -> dict:
        raise NotImplementedError()
