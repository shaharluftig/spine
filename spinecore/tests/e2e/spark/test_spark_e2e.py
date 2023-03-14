import pkg_resources
import pytest
from pyspark.sql.types import Row

from spinecore.common.context.spark_context import SpineSparkContext
from spinecore.executors import execute
from spinecore.tests.e2e.spark.steps.filter_country import FilterCountry
from spinecore.workflows import DagWorkflow
from spinelibs.spark.steps.io.csv.csv_reader import CsvReader


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
    workflow, last_step = workflow_factory()

    # Action
    result: dict = await execute(ctx, workflow)

    # Assert
    df = result.get(last_step).collect()

    data = [Row("shahar", 23, "israel"),
            Row("josef", 55, "israel"),
            Row("sang", 55, "china")]
    expected_df = ctx.spark.createDataFrame(data=data, schema=["name", "age", "country"])

    assert sorted(df) == sorted(expected_df)
