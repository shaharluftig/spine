from core.src.workflows.Workflow import Workflow


class IExecutor:
    async def execute(self, workflow: Workflow):
        raise NotImplementedError()
