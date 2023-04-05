from spinecore.common.context.base_context import BaseContext
from spinecore.common.helpers.contract.Workflow import Workflow


class IExecutor:
    async def execute(self, ctx: BaseContext, workflow: Workflow) -> dict:
        raise NotImplementedError()
