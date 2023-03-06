import asyncio
import os

from core.common.context import GarnetPolarsContext
from core.executors import execute
from core.workflows import DagWorkflow
from examples.polars_exp.steps.migrations_parser import MigrationsParser
from libs.polars.steps.general.GUIDColumn import GUIDColumn
from libs.polars.steps.io.csv.csv_reader import CsvReader
from libs.polars.steps.io.csv.csv_writer import CSVWriter
from libs.polars.steps.io.sql.sql_writer import SQLWriter


def __setup_steps():
    db_path = os.path.dirname(os.path.realpath("../polars_exp/db/exp.db"))
    sqlite_conn = f"{db_path}\\exp.db"
    migrations_reader = CsvReader("../polars_exp/resources/migrations.csv", has_headers=True)
    migrations_parser = MigrationsParser()
    csv_writer = CSVWriter("./resources/output.csv")
    guid_column = GUIDColumn(["company", "year"], guid_column_name="guid")
    mssql_writer = SQLWriter("hello_polars", connection_string="sqlite:///" + sqlite_conn, if_exists="replace",
                             engine="sqlalchemy")
    return migrations_reader, migrations_parser, guid_column, csv_writer, mssql_writer


def workflow_factory():
    workflow = DagWorkflow("PolarsExample")
    migrations_reader, migrations_parser, guid_column, csv_writer, mssql_writer = __setup_steps()
    workflow.add_after([migrations_parser], [migrations_reader])
    workflow.add_after([guid_column], [migrations_parser])
    workflow.add_after([csv_writer, mssql_writer], [guid_column])
    return workflow


async def main():
    ctx = GarnetPolarsContext.get_context(lazy=True, config={"set_tbl_rows": 20})
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
