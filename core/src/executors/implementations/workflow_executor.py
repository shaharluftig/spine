from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.executors.IExecutor import IExecutor
from core.src.workflows.Workflow import Workflow


# TODO: Make Async Executor
class WorkflowExecutor(IExecutor):
    def __init__(self, ctx: CardoContext):
        self.ctx = ctx

    def _execute_step(self, step, dependencies):
        result = step.process(self.ctx, *dependencies)
        return result

    def __get_dependency_results(self, dependencies, step, steps_results, workflow):
        dependencies_results = []
        for dependency in dependencies:
            dependency_result = self.__execute_step_by_dependencies(workflow, steps_results, dependency)
            if isinstance(dependency_result, list) or isinstance(dependency_result, tuple):
                if len(workflow.get_after(dependency)) > 1:
                    dependency_result = dependency_result[workflow.get_after(dependency).index(step)]
                    dependencies_results.append(dependency_result)
                else:
                    dependencies_results.extend(dependency_result)
            else:
                dependencies_results.append(dependency_result)
        return dependencies_results

    def __execute_step_by_dependencies(self, workflow, steps_results, step):
        if step in steps_results:
            return steps_results[step]
        else:
            dependencies = workflow.get_before(step)
            dependencies_results = self.__get_dependency_results(dependencies, step, steps_results, workflow)
            steps_results[step] = self._execute_step(step, dependencies_results)

    def __execute_all_steps(self, workflow: Workflow):
        steps_results = {}
        for step in workflow.to_list():
            self.__execute_step_by_dependencies(workflow, steps_results, step)
        return steps_results

    def execute(self, workflow: Workflow) -> None:
        self.__execute_all_steps(workflow)
