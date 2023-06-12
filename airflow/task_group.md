Un Task Group es una forma de agrupar tareas relacionadas en un DAG de Airflow. Puedes considerarlo como un contenedor que contiene un conjunto de tareas relacionadas que se ejecutan juntas o tienen algún tipo de relación lógica.

## Ventajas de los Task Groups:

Organización: Los Task Groups permiten agrupar tareas relacionadas en secciones lógicas dentro de un DAG, lo que facilita la comprensión y el mantenimiento del flujo de trabajo.
Legibilidad: Al agrupar tareas relacionadas en un Task Group, se mejora la legibilidad del DAG, ya que las tareas se organizan de manera más estructurada y se pueden colapsar o expandir para ocultar o mostrar detalles específicos.
Reusabilidad: Los Task Groups se pueden definir una vez y reutilizar en múltiples DAGs, lo que promueve la consistencia y la reutilización del código.

## Sintaxis y uso de los Task Groups:

```python
from airflow.decorators import task_group
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

@task_group('my_task_group', tooltip='This is my task group')
def create_task_group():
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')

    task1 >> task2 >> task3

dag = DAG(...)

with dag:
    create_task_group()


```