import pkg_resources
import polars as pl
import pytest
from polars.testing.asserts import assert_frame_equal

from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.executors import execute
from spinecore.tests.e2e.polars.steps.filter_country import FilterCountry
from spinecore.workflows import DagWorkflow
from spinelibs.spinelibs.polars.steps.general.GUIDColumn import GUIDColumn
from spinelibs.spinelibs.polars.steps.io.csv.csv_reader import CsvReader


def __setup_steps():
    test_csv_path = pkg_resources.resource_filename(__name__, "./resources/test_data.csv")
    csv_reader = CsvReader(test_csv_path, has_headers=True)
    guid_column = GUIDColumn(["name", "age"], "guid")
    filter_country = FilterCountry(["usa"])
    return csv_reader, guid_column, filter_country


def workflow_factory():
    workflow = DagWorkflow("PolarsE2ETest")
    csv_reader, guid_column, filter_country = __setup_steps()
    workflow.add_last(csv_reader)
    workflow.add_last(guid_column)
    workflow.add_last(filter_country)
    return workflow, filter_country


@pytest.mark.asyncio
async def test_polars_e2e():
    # Prepare
    expected_df = pl.from_dicts([{'name': 'shahar', 'age': 23, 'country': 'israel', 'guid': '7768553422548966964'},
                                 {'name': 'josef', 'age': 55, 'country': 'israel', 'guid': '4412959094999199270'},
                                 {'name': 'sang', 'age': 55, 'country': 'china', 'guid': '14666928701774118983'}])

    ctx = SpinePolarsContext.get_context(lazy=True)
    ctx.logger.info("Running Polars E2E Test")
    workflow, last_step = workflow_factory()

    # Action
    result: dict = await execute(ctx, workflow)
    df = result.get(last_step).collect()

    # Assert
    assert_frame_equal(df, expected_df)