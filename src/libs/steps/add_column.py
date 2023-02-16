from src.core.common.context.implementations.cardo_context import CardoContext
from src.core.dataframe.cardo_dataframe import CardoDataFrame
from src.libs.IStep import IStep


class AddColumn(IStep):
    def process(self, cardo_context: CardoContext, cardo_dataframe: CardoDataFrame) -> CardoDataFrame:
        return cardo_dataframe
