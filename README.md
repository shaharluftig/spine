# Spine

Spine is an open-source project library that helps you create production-grade ETL pipelines quickly and conveniently.

## Quickstart

## Polars

### install

```python
pip install pyspine[polars]
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


## Spark

### install

```python
pip install pyspine[spark]
```

### Create context

```python
from spinecore.common.context.spark_context import SpineSparkContext

ctx = SpineSparkContext.get_context(spark_config={"spark.executor.memory": "1gb"})  # Example config
```

### Create Workflow

```python
from spinecore.workflows import DagWorkflow

workflow = workflow_factory()
```

### Add Steps to workflow

```python
from spinelibs.spark.steps.io.console.console_writer import ConsoleWriter
from spinelibs.spark.steps.io.csv.csv_reader import CsvReader

def __setup_steps():
    example_reader = CsvReader("./resources/exp1.csv", has_headers=True)
    example_reader2 = CsvReader("./resources/exp2.csv", has_headers=True)
    console_output = ConsoleWriter()
    return example_reader, example_reader2 ,console_output


def workflow_factory():
    workflow = DagWorkflow("SparkExample")
     example_reader, example_reader2 ,console_output= __setup_steps()
    workflow.add_after([console_output], [example_reader])
    workflow.add_after([console_output], [example_reader2])
    return workflow
```

### Execute Workflow

```python
async def main():
    ctx = SpineSparkContext.get_context(spark_config={"spark.executor.memory": "1gb"})  # Example config
    workflow = workflow_factory()
    await execute(ctx, workflow)


if __name__ == '__main__':
    asyncio.run(main())
```
License
----

Apache License 2.0

