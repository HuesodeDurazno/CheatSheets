Un SubDAG es un concepto en Airflow que te permite encapsular un conjunto de tareas relacionadas dentro de un DAG más grande. Se utiliza para modularizar y reutilizar secciones de un DAG, lo que facilita la comprensión y el mantenimiento de flujos de trabajo complejos

## Estructura de un SubDAG:
Un SubDAG tiene su propio conjunto de tareas y dependencias internas. Puedes crear un SubDAG definiendo una clase que herede de la clase DAG de Airflow y agregando las tareas correspondientes a esa clase.

Ejemplo:

```python
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

def subdag(parent_dag_name, child_dag_name, args):
    dag = DAG(
        dag_id=f'{parent_dag_name}.{child_dag_name}',
        start_date =args['start_date'],
        schedule_intervale =args['schedule_intervale'],
        catchup= args['catchup']
    )

    task1 = DummyOperator(task_id='task1', dag=dag)
    task2 = DummyOperator(task_id='task2', dag=dag)

    task1 >> task2

    return dag
```

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.subdag_operator import SubDagOperator

with DAG('group_dag', 
        start_date=datetime(2022, 1, 1),
        schedule_interval='@daily', 
        catchup=False) as dag:
    
       

    args = {'start_date': dag.start_date, 
            'schedule_interval': dag.schedule_interval, 
            'catchup': dag.catchup}

     

    downloads = SubDagOperator(task_id='donwloads',
                            subdag=subdag_downloads(dag.dag_id, ‘downloads’, args))

    task3 = DummyOperator(task_id='task3', dag=dag)


    downloads >> task3

```

Esta estructura es útil cuando deseas reutilizar un DAG completo como SubDAG en múltiples DAGs principales. Además, mantiene una separación clara entre los diferentes DAGs y los hace más legibles y manejables.

### Ventajas de los SubDAGs:

Modularidad: Los SubDAGs permiten dividir un DAG grande en partes más pequeñas y manejables, lo que facilita su desarrollo y mantenimiento.

Reutilización: Puedes usar un SubDAG en múltiples DAGs, lo que evita la duplicación de código y promueve la consistencia en tus flujos de trabajo.

Claridad: Al encapsular un conjunto de tareas relacionadas en un SubDAG, mejora la legibilidad y comprensión del DAG principal.

### Consideraciones:

Los SubDAGs deben tener identificadores únicos para evitar conflictos.

Los SubDAGs deben especificar schedule_interval=None para evitar que se ejecuten de forma independiente.

Los SubDAGs no se pueden ejecutar en paralelo con otros SubDAGs en el mismo nivel.

