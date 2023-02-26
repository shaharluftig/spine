from typing import Union, Tuple

from core.src.common.context.implementations.base_context import BaseContext
from core.src.common.helpers.dataframe import DataFrame


class IStep:
    async def process(self, ctx: BaseContext, df: Union[DataFrame, Tuple[DataFrame], None]) \
            -> Union[DataFrame, Tuple[DataFrame]]:
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__
