from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.common.helpers.dataframe import DataFrame


class IStep:

    def process(self, cardo_context: CardoContext, *df: DataFrame) -> DataFrame:
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__
