---
sidebar_position: 1
---

# Spine

Spine is an open-source project library that helps you create production-grade ETL pipelines quickly and conveniently.

## basic terms

### Context:

* `Context` is where Spine starts. Every context has…
* There are multiply implementations of SpineContext, such as `SpineSparkContext`, and `SpinePolarsContext`

### Step:

* A `Step` is a basic unit that processes data. Each step gets a Context and a Dataframe as input, and returns a
  modified
  `Dataframe`.
* You can find many common step implementations in spinelibs, such as DB connectors.

### Workflow:

* `Workflow` represents the flow of the pipeline. Every workflow inherits from the abstract class Workflow.
  Every workflow contains multiple `Steps`.
* Currently, there is one implementation of the executor - `DagWorkflow`.

### Executor

* gets a `Workflow` and a `Context` as input, and executes the `Workflow`.
* Currently, there is one implementation of the `Executor` - `AsyncWorkflowExecutor`.