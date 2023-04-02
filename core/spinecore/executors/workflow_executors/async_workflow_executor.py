import asyncio
from typing import List

from spinecore.common.context.base_context import BaseContext
from spinecore.common.helpers.contract.IExecutor import IExecutor
from spinecore.common.helpers.contract.IStep import IStep
from spinecore.common.helpers.contract.Workflow import Workflow


class AsyncWorkflowExecutor(IExecutor):
    """Async implementation of workflow executor"""

    @staticmethod
    async def __execute_step(ctx: BaseContext, step: IStep, dependencies):
        result = ctx.get_spine_logger().time_function(step.process, f"Step {step.__class__.__name__}")
        return await result(ctx, *dependencies)

    async def __get_dependency_results(self, ctx, dependencies, steps_results: dict, workflow: Workflow) -> List:
        return [await self.__execute_step_by_dependencies(ctx, workflow, steps_results, dependency)
                for dependency in dependencies]

    async def __execute_step_by_dependencies(self, ctx: BaseContext, workflow: Workflow,
                                             steps_results: dict, step: IStep):
        if step in steps_results:
            return steps_results[step]
        dependencies = workflow.get_before(step)
        dependencies_results = await self.__get_dependency_results(ctx, dependencies, steps_results, workflow)
        steps_results[step] = await self.__execute_step(ctx, step, dependencies_results)

    async def __execute_all_steps(self, ctx: BaseContext, workflow: Workflow) -> dict:
        steps_results = {}
        flat_graph = workflow.flat_graph()
        await asyncio.gather(
            *[asyncio.create_task(self.__execute_step_by_dependencies(ctx, workflow, steps_results, step))
              for step in flat_graph])
        return steps_results

    async def execute(self, ctx: BaseContext, workflow: Workflow) -> dict:
        ctx.logger.info(f"Executing {workflow.name}")
        return await self.__execute_all_steps(ctx, workflow)
