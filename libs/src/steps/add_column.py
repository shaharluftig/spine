from core.src.common.context.implementations.cardo_context import CardoContext
from core.src.common.helpers.dataframe import DataFrame
from libs.src.IStep import IStep


class AddColumn(IStep):
    def process(self, cardo_context: CardoContext, df: DataFrame) -> DataFrame:
        return df
