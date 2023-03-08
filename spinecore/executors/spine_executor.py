from spinecore.common.context.base_context import BaseContext
from spinecore.common.helpers.contract.IExecutor import IExecutor
from spinecore.executors.workflow_executors.async_workflow_executor import AsyncWorkflowExecutor
from spinecore.common.helpers.contract.Workflow import Workflow


async def execute(ctx: BaseContext, workflow: Workflow, executor: IExecutor = AsyncWorkflowExecutor()) -> dict:
    return await ctx.get_spine_logger().time_function(executor.execute, f"{workflow.name} execution")(ctx, workflow)
