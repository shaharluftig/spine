import asyncio

from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.executors.workflow_executors.IExecutor import IExecutor
from core.src.workflows.Workflow import Workflow
from core.src.common.helpers.IStep import IStep


class AsyncWorkflowExecutor(IExecutor):
    @staticmethod
    async def __execute_step(ctx: CardoContext, step: IStep, dependencies):
        result = ctx.get_cardo_logger().log_step(step.process)
        return await result(ctx, *dependencies)

    async def __get_dependency_results(self, ctx, dependencies, steps_results: dict, workflow: Workflow):
        return [await self.__execute_step_by_dependencies(ctx, workflow, steps_results, dependency) for
                dependency in dependencies]

    async def __execute_step_by_dependencies(self, ctx: CardoContext, workflow: Workflow, steps_results: dict,
                                             step: IStep):
        if step in steps_results:
            return steps_results[step]
        else:
            dependencies = workflow.get_before(step)
            dependencies_results = await self.__get_dependency_results(ctx, dependencies, steps_results, workflow)
            steps_results[step] = await self.__execute_step(ctx, step, dependencies_results)

    async def __execute_all_steps(self, ctx: CardoContext, workflow: Workflow):
        steps_results = {}
        flat_graph = workflow.flat_graph()
        await asyncio.gather(*[self.__execute_step_by_dependencies(ctx, workflow, steps_results, step)
                               for step in flat_graph])
        return steps_results

    async def execute(self, ctx: CardoContext, workflow: Workflow):
        return await self.__execute_all_steps(ctx, workflow)
