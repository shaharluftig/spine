import asyncio
import os

from core.common.context import GarnetPolarsContext
from core.executors import execute
from core.workflows import DagWorkflow
from examples.polars_exp.steps.migrations_parser import MigrationsParser
from libs.steps.polars.general.GUIDColumn import GUIDColumn
from libs.steps.polars.io.console.console_writer import ConsoleWriter
from libs.steps.polars.io.csv.csv_reader import CsvReader
from libs.steps.polars.io.csv.csv_writer import CSVWriter
from libs.steps.polars.io.sql.sql_reader import SQLReader


def __setup_steps():
    db_path = os.path.dirname(os.path.realpath("../polars_exp/db/exp.db"))
    sqlite_conn = f"sqlite:{db_path}\\exp.db"
    migrations_reader = CsvReader("../polars_exp/resources/migrations.csv", has_headers=True)
    migrations_parser = MigrationsParser()
    users_reader = SQLReader("SELECT * FROM users", sqlite_conn)
    csv_writer = CSVWriter("./resources/output.csv")
    guid_column = GUIDColumn(["company", "year"], guid_column_name="guid")
    return migrations_reader, migrations_parser, guid_column, users_reader, csv_writer


def workflow_factory():
    workflow = DagWorkflow("PolarsExample")
    migrations_reader, migrations_parser, guid_column, users_reader, csv_writer = __setup_steps()
    workflow.add_after([migrations_parser], [migrations_reader])
    workflow.add_after([guid_column], [migrations_parser])
    workflow.add_after([ConsoleWriter()], [users_reader])
    workflow.add_after([csv_writer, ConsoleWriter()], [guid_column])
    return workflow


async def main():
    ctx = GarnetPolarsContext.get_context(lazy=True, config={"set_tbl_rows": 20})
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
