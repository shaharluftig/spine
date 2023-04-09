import asyncio
import os
import sqlite3

from core.spinecore.common.context.pandas_context import SpinePandasContext
from core.spinecore.executors.spine_executor import execute
from core.spinecore.workflows.dag_workflow import DagWorkflow
from spinelibs.pandas.steps.io.console.console_writer import ConsoleWriter
from spinelibs.pandas.steps.io.csv.csv_reader import CsvReader
from spinelibs.pandas.steps.io.csv.csv_writer import CSVWriter
from spinelibs.pandas.steps.io.sql.sql_reader import SQLReader
from steps.migrations_parser import MigrationsParser


def __setup_steps():
    db_path = os.path.dirname(os.path.realpath("../polars_exp/db/exp.db"))
    sqlite_con = sqlite3.connect(f"{db_path}\\exp.db")
    names_reader = SQLReader("select * FROM names", sqlite_con)
    migrations_reader = CsvReader("../pandas_exp/resources/migrations.csv", )
    migrations_parser = MigrationsParser()
    csv_writer = CSVWriter("./resources/output.csv")
    return migrations_reader, migrations_parser, names_reader, csv_writer


def workflow_factory():
    workflow = DagWorkflow("PandasExample")
    migrations_reader, migrations_parser, names_reader, csv_writer = __setup_steps()
    workflow.add_after([migrations_parser], [migrations_reader])
    workflow.add_after([csv_writer], [migrations_parser])
    workflow.add_after([ConsoleWriter()], [names_reader])
    return workflow


async def main():
    ctx = SpinePandasContext.get_context(config={"display.max_rows": 999})
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
