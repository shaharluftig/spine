from core import CardoContext
from core.src.executors.workflow_executors.IExecutor import IExecutor
from core.src.executors.workflow_executors.implementations.async_workflow_executor import AsyncWorkflowExecutor
from core.src.workflows import Workflow


async def execute(ctx: CardoContext, workflow: Workflow, executor: IExecutor = AsyncWorkflowExecutor()):
    return await executor.execute(ctx, workflow)
