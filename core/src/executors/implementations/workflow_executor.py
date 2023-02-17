import asyncio

from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.common.helpers.logging.cardo_logger import cardo_logger
from core.src.executors.IExecutor import IExecutor
from core.src.workflows.Workflow import Workflow
from libs.src.IStep import IStep


# TODO: Make this async real
class WorkflowExecutor(IExecutor):
    def __init__(self, ctx: CardoContext):
        self.ctx = ctx

    async def __execute_step(self, step: IStep, dependencies):
        result = cardo_logger.log_step(step.process)
        return await result(self.ctx, *dependencies)

    async def __get_dependency_results(self, dependencies, step: IStep, steps_results, workflow: Workflow):
        dependencies_results = []
        for dependency in dependencies:
            dependency_result = await self.__execute_step_by_dependencies(workflow, steps_results, dependency)
            if isinstance(dependency_result, list) or isinstance(dependency_result, tuple):
                if len(workflow.get_after(dependency)) > 1:
                    dependency_result = dependency_result[workflow.get_after(dependency).index(step)]
                    dependencies_results.append(dependency_result)
                else:
                    dependencies_results.extend(dependency_result)
            else:
                dependencies_results.append(dependency_result)
        return dependencies_results

    async def __execute_step_by_dependencies(self, workflow: Workflow, steps_results, step: IStep):
        if step in steps_results:
            return steps_results[step]
        else:
            dependencies = workflow.get_before(step)
            dependencies_results = await self.__get_dependency_results(dependencies, step, steps_results, workflow)
            steps_results[step] = await self.__execute_step(step, dependencies_results)

    async def __execute_all_steps(self, workflow: Workflow):
        steps_results = {}
        flat_graph = workflow.flat_graph()
        await asyncio.gather(*[self.__execute_step_by_dependencies(workflow, steps_results, step)
                               for step in flat_graph])
        return steps_results

    async def execute(self, workflow: Workflow):
        return await self.__execute_all_steps(workflow)
