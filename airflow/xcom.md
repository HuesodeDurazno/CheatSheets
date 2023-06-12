## Que es 
XCom (Cross Communication) es un mecanismo en Airflow que permite el intercambio de datos entre tareas dentro de un flujo de trabajo. Puedes utilizar XCom para pasar información, como resultados intermedios o variables, entre tareas de manera eficiente.

## Ejemplo de escritura y lectura de datos con XCom:
A continuación, te mostraré un ejemplo de cómo escribir y leer datos utilizando XCom:

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def _t1(ti):
    ti.xcom_push(key='my_key',value=42)

def _t2(ti):
    data = ti.xcom_pull(key='my_key')


dag = DAG(...)

with dag:
    task1 = PythonOperator(
        task_id='write_data',
        python_callable=write_data
    )

    task2 = PythonOperator(
        task_id='read_data',
        python_callable=read_data
    )

    task1 >> task2

```