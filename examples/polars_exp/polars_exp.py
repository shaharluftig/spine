import asyncio
import os

from core import DagWorkflow, CardoContext, execute
from libs.src.steps.polars.io.console_writer import ConsoleWriter
from libs.src.steps.polars.io.csv_reader import CsvReader
from libs.src.steps.polars.io.sql_reader import SQLReader


def __setup_steps():
    db_path = os.path.dirname(os.path.realpath("../polars_exp/db/exp.db"))
    rent_reader = CsvReader("../polars_exp/resources/rent.csv", has_headers=True)
    users_reader = SQLReader("SELECT * FROM users", f"sqlite:{db_path}\\exp.db")
    console_output = ConsoleWriter()
    return rent_reader, users_reader, console_output


def workflow_factory():
    workflow = DagWorkflow()
    rent_reader, users_reader, console_output = __setup_steps()
    workflow.add_last(rent_reader, users_reader)
    workflow.add_after([console_output], [rent_reader])
    workflow.add_after([console_output], [users_reader])
    return workflow


async def main():
    ctx = CardoContext.get_context()
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
