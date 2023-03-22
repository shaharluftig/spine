from spinecore.common.context.base_context import BaseContext


class IStep:
    async def process(self, ctx: BaseContext, df):
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__class__.__name__
