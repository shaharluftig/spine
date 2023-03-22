from spinecore.common.context.base_context import BaseContext
from spinecore.common.helpers.contract.IExecutor import IExecutor
from spinecore.common.helpers.contract.Workflow import Workflow
from spinecore.executors.workflow_executors.async_workflow_executor import AsyncWorkflowExecutor


async def execute(ctx: BaseContext, workflow: Workflow, executor: IExecutor = AsyncWorkflowExecutor()) -> dict:
    """Executes workflow using ctx and executor"""
    return await ctx.get_spine_logger().time_function(executor.execute, f"{workflow.name} execution")(ctx, workflow)
