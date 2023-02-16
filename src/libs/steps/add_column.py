from src.core.common.context.implementations.cardo_context import CardoContext
from src.core.helpers.dataframe import DataFrame
from src.libs.IStep import IStep


class AddColumn(IStep):
    def process(self, cardo_context: CardoContext, df: DataFrame) -> DataFrame:
        return df
