from typing import Union, Tuple

from core.common.context.implementations.base_context import BaseContext
from core.common.helpers.dataframes import DataFrame


class IStep:
    async def process(self, ctx: BaseContext, df: Union[DataFrame, Tuple[DataFrame], None]) \
            -> Union[DataFrame, Tuple[DataFrame]]:
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__class__.__name__
