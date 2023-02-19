from enum import Enum


class Mode(str, Enum):
    SPARK = "spark"
    POLARS = "polars"
    PANDAS = "pandas"

    def __str__(self):
        return str(self.value)
