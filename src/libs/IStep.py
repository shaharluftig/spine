from src.core.common.context.implementations.cardo_context import CardoContext
from src.core.dataframe.cardo_dataframe import CardoDataFrame


class IStep:
    def process(self, cardo_context: CardoContext, *df: CardoDataFrame) -> CardoDataFrame:
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__
