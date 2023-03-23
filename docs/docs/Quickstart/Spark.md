---
sidebar_position: 1
sidebar_label: 'Spark'

---

# Quickstart

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