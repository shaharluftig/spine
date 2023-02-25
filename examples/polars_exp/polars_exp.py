import asyncio
import os

from core import DagWorkflow, CardoContext, execute
from examples.polars_exp.steps.migrations_parser import MigrationsParser
from libs.src.steps.polars.io.console.console_writer import ConsoleWriter
from libs.src.steps.polars.io.csv.csv_reader import CsvReader
from libs.src.steps.polars.io.csv.csv_writer import CSVWriter
from libs.src.steps.polars.io.sql.sql_reader import SQLReader


def __setup_steps():
    db_path = os.path.dirname(os.path.realpath("../polars_exp/db/exp.db"))
    sqlite_conn = f"sqlite:{db_path}\\exp.db"
    migrations_reader = CsvReader("../polars_exp/resources/migrations.csv", has_headers=True)
    migrations_parser = MigrationsParser()
    users_reader = SQLReader("SELECT * FROM users", sqlite_conn)
    csv_writer = CSVWriter("./resources/output.csv")
    return migrations_reader, migrations_parser, users_reader, csv_writer


def workflow_factory():
    workflow = DagWorkflow("PolarsExample")
    migrations_reader, migrations_parser, users_reader, csv_writer = __setup_steps()
    workflow.add_after([ConsoleWriter()], [migrations_reader, users_reader])
    workflow.add_after([migrations_parser], [migrations_reader])
    workflow.add_after([csv_writer], [migrations_parser])
    return workflow


async def main():
    ctx = CardoContext.get_context(lazy_polars=True)
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
