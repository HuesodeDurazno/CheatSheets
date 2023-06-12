## Que es

Las trigger rules son reglas que se aplican a una tarea para determinar si debe ser ejecutada o no, en función del estado de las tareas predecesoras.

## Tipos de trigger rules:

Airflow ofrece varios tipos de trigger rules que puedes asignar a una tarea. Algunos de los tipos más comunes son:

"all_success" (predeterminado): La tarea se ejecuta si todas las tareas predecesoras han finalizado correctamente.

"all_failed": La tarea se ejecuta si todas las tareas predecesoras han fallado.

"one_success": La tarea se ejecuta si al menos una tarea predecesora ha finalizado correctamente.

"one_failed": La tarea se ejecuta si al menos una tarea predecesora ha fallado.

"none_failed": La tarea se ejecuta si todas las tareas predecesoras han finalizado (ya sea correctamente o con fallas), o si no hay tareas predecesoras.

"none_skipped": La tarea se ejecuta si no hay tareas predecesoras o si todas las tareas predecesoras han sido omitidas.

```python
    from airflow import DAG
    from airflow.operators.dummy_operator import DummyOperator

    dag = DAG(...)

    with dag:
        task1 = DummyOperator(task_id='task1')
        task2 = DummyOperator(task_id='task2', trigger_rule='all_success')
        task3 = DummyOperator(task_id='task3', trigger_rule='one_failed')

        task1 >> task2 >> task3

```