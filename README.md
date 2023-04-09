# Spine

Spine is an open-source project library that helps you create production-grade ETL pipelines quickly and conveniently.

## Quickstart

## Polars

### install

```python
pip
install
pyspine[polars]
```

### Create context

```python
from spinecore.common.context.polars_context import SpinePolarsContext

ctx = SpinePolarsContext.get_context(lazy=True, config={"set_tbl_rows": 20})
```

### Create Workflow

```python
from spinecore.workflows import DagWorkflow

workflow = workflow_factory()
```

### Add Steps to workflow

```python
from spinelibs.polars.steps.general.GUIDColumn import GUIDColumn
from spinelibs.polars.steps.io.csv.csv_reader import CsvReader
from spinelibs.polars.steps.io.csv.csv_writer import CSVWriter


def __setup_steps():
    migrations_reader = CsvReader("../polars_exp/resources/migrations.csv", has_headers=True)
    csv_writer = CSVWriter("./resources/output.csv")
    guid_column = GUIDColumn(["company", "year"], guid_column_name="guid")
    return migrations_reader, guid_column, csv_writer


def workflow_factory():
    workflow = DagWorkflow("PolarsExample")
    migrations_reader, guid_column, csv_writer = __setup_steps()
    workflow.add_after([guid_column], [migrations_reader])
    workflow.add_after([csv_writer], [guid_column])
    return workflow
```

### Execute Workflow

```python
async def main():
    ctx = SpinePolarsContext.get_context(lazy=True, config={"set_tbl_rows": 20})
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
```

##### For more examples, head to  https://spine-docs.vercel.app/docs/intro

### Building
* `git clone https://github.com/shaharluftig/spine.git` 
* `pip install pyspine[all]`
* `pip install pyspine[dev]`
* Start hacking!

### Testing
* `pytest .`


License
----

Apache License 2.0

