import pkg_resources
import pytest
from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.executors import execute
from spinecore.workflows import DagWorkflow
from spinelibs.spark.steps.io.csv.csv_reader import CsvReader

from .steps.filter_country import FilterCountry


def __setup_steps():
    test_csv_path = pkg_resources.resource_filename(__name__, "./resources/test_data.csv")
    csv_reader = CsvReader(test_csv_path, has_headers=True)
    filter_country = FilterCountry(["usa"])
    return csv_reader, filter_country


def workflow_factory():
    workflow = DagWorkflow("SparkE2ETest")
    csv_reader, filter_country = __setup_steps()
    workflow.add_last(csv_reader)
    workflow.add_last(filter_country)
    return workflow, filter_country


@pytest.mark.asyncio
async def test_spark_e2e():
    # Prepare
    ctx = SpineSparkContext.get_context()
    ctx.logger.info("Running Spark E2E Test")
    workflow, last_step = workflow_factory()
    expected_df = ctx.spark.read.csv(pkg_resources.resource_filename(__name__, "./resources/expected_data.csv"),
                                     header=True)

    # Action
    result: dict = await execute(ctx, workflow)
    df = result.get(last_step)

    # Assert
    assert sorted(df.collect()) == sorted(expected_df.collect())
