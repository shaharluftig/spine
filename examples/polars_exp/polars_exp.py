import asyncio
import os

from steps.migrations_parser import MigrationsParser
from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.executors import execute
from spinecore.workflows import DagWorkflow
from spinelibs.polars.steps.general.GUIDColumn import GUIDColumn
from spinelibs.polars.steps.io.console.console_writer import ConsoleWriter
from spinelibs.polars.steps.io.csv.csv_reader import CsvReader
from spinelibs.polars.steps.io.csv.csv_writer import CSVWriter
from spinelibs.polars.steps.io.sql.sql_reader import SQLReader


def __setup_steps():
    db_path = os.path.dirname(os.path.realpath("../polars_exp/db/exp.db"))
    sqlite_conn = f"sqlite:{db_path}\\exp.db"
    names_reader = SQLReader("select * FROM names", sqlite_conn)
    migrations_reader = CsvReader("../polars_exp/resources/migrations.csv", has_headers=True)
    migrations_parser = MigrationsParser()
    csv_writer = CSVWriter("./resources/output.csv")
    guid_column = GUIDColumn(["company", "year"], guid_column_name="guid")
    return migrations_reader, migrations_parser, names_reader, guid_column, csv_writer


def workflow_factory():
    workflow = DagWorkflow("PolarsExample")
    migrations_reader, migrations_parser, names_reader, guid_column, csv_writer = __setup_steps()
    workflow.add_after([migrations_parser], [migrations_reader])
    workflow.add_after([guid_column], [migrations_parser])
    workflow.add_after([csv_writer], [guid_column])
    workflow.add_after([ConsoleWriter()], [names_reader])
    return workflow


async def main():
    ctx = SpinePolarsContext.get_context(lazy=True, config={"set_tbl_rows": 20})
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
