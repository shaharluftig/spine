from src.executor.executors.IExecutor import IExecutor


class WorkflowExecutor(IExecutor):
    def _execute_step(self, step, cardo_context, dependencies):
        result = step.process(cardo_context, *dependencies)
        return result

    def __get_dependency_results(self, cardo_context, dependencies, step, steps_results, workflow):
        dependencies_results = []
        for dependency in dependencies:
            dependency_result = self.__execute_step_by_dependencies(cardo_context, workflow, steps_results, dependency)
            if isinstance(dependency_result, list) or isinstance(dependency_result, tuple):
                if len(workflow.get_after(dependency)) > 1:
                    dependency_result = dependency_result[workflow.get_after(dependency).index(step)]
                    dependencies_results.append(dependency_result)
                else:
                    dependencies_results.extend(dependency_result)
            else:
                dependencies_results.append(dependency_result)
        return dependencies_results

    def __execute_step_by_dependencies(self, cardo_context, workflow, steps_results, step):
        if step in steps_results:
            return steps_results[step]
        else:
            dependencies = workflow.get_before(step)
            dependencies_results = self.__get_dependency_results(cardo_context, dependencies, step, steps_results,
                                                                 workflow)
            dependencies_results = map(lambda cardo_dataframe: cardo_dataframe.deepcopy(), dependencies_results)
            steps_results[step] = self._execute_step(step, cardo_context, dependencies_results)

    def __execute_all_steps(self, cardo_context, workflow):
        steps_results = {}
        for step in workflow.to_list():
            self.__execute_step_by_dependencies(cardo_context, workflow, steps_results, step)
        return steps_results

    def execute(self, workflow, cardo_context):
        results = self.__execute_all_steps(cardo_context, workflow)
        return map(lambda step: results[step], workflow.get_before(None))
