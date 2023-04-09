import asyncio

import polars as pl
import pytest
from spinecore.common.context.polars_context import SpinePolarsContext
from spinecore.common.helpers.contract.IStep import IStep
from spinecore.executors import execute
from spinecore.workflows import DagWorkflow


class BlockingStep(IStep):
    async def process(self, ctx: SpinePolarsContext, df=None):
        df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "ham", "spam"]})
        await asyncio.sleep(1)  # Blocking
        return df


class NothingStep(IStep):
    async def process(self, ctx: SpinePolarsContext, df):
        return df


def workflow_factory():
    workflow = DagWorkflow("test_blocking")
    nothing_step = NothingStep()
    workflow.add_after([nothing_step], [BlockingStep()])

    return workflow, nothing_step


@pytest.mark.asyncio
async def test_blocking_step():
    """Tests IO Blocking step execution"""
    # Prepare
    ctx = SpinePolarsContext.get_context(lazy=True, config={"set_tbl_rows": 20})
    expected_df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "ham", "spam"]})
    workflow, nothing_step = workflow_factory()

    # Action
    result = await execute(ctx, workflow)
    df = result[0][nothing_step]

    # Assert
    assert df.frame_equal(expected_df)
