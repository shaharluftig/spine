from core.common.context import BaseContext
from core.executors.workflow_executors.IExecutor import IExecutor
from core.executors.workflow_executors.implementations.async_workflow_executor import AsyncWorkflowExecutor
from core.workflows import Workflow


async def execute(ctx: BaseContext, workflow: Workflow, executor: IExecutor = AsyncWorkflowExecutor()) -> dict:
    return await ctx.get_garnet_logger().time_function(executor.execute, f"{workflow.name} execution")(ctx, workflow)
