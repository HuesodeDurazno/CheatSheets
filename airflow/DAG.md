# Que es

En Apache Airflow, un DAG (Directed Acyclic Graph) es una representación de un flujo de trabajo. Un DAG está compuesto por un conjunto de tareas que se ejecutan en un orden específico, siguiendo las dependencias definidas por el usuario.

Cada tarea en un DAG es representada por un operador. Los operadores son clases de Python que definen la lógica de la tarea. En el ejemplo anterior, la tarea "start" es representada por el operador "DummyOperator", la tarea "process_data" es representada por el operador "PythonOperator" y la tarea "end" es representada por otro "DummyOperator".

```python
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    from datetime import datetime, timedelta

    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2022, 1, 1),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }

    dag = DAG(
        'my_dag',
        default_args=default_args,
        description='Un ejemplo de DAG simple',
        schedule_interval=timedelta(days=1),
    )

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag,
    )

    t2 = BashOperator(
        task_id='echo_hello',
        bash_command='echo "Hello, world!"',
        dag=dag,
    )

    t1 >> t2

```

## Operador

En Apache Airflow, un operador es una clase de Python que define una tarea en un DAG (Directed Acyclic Graph). Cada operador representa una tarea individual en el flujo de trabajo y contiene la lógica necesaria para realizar esa tarea.

Los operadores pueden ser de diferentes tipos y cada tipo de operador proporciona diferentes funcionalidades.

Los operadores son instanciados dentro de un DAG y se configuran con argumentos como el ID de la tarea, la fecha de inicio, la fecha de finalización, entre otros. La configuración de cada operador determina cómo se ejecutará la tarea que representa en el flujo de trabajo.

hay de 3 tipos:

1. Action Operators
2. Transfer Operators
3. Sensors Operator

Ejemplo

```python
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    from datetime import datetime, timedelta

    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2022, 1, 1),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }

    dag = DAG(
        'my_dag',
        default_args=default_args,
        description='Un ejemplo de DAG simple',
        schedule_interval=timedelta(days=1),
    )

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag,
    )
```

## Que es un provider

En Apache Airflow, un provider se refiere a un conjunto de paquetes de Python que contienen operadores, ganchos (hooks), conexiones (connections), variables, macros y otros componentes para interactuar con una tecnología específica de una forma estandarizada.

Los proveedores son utilizados para encapsular la lógica de integración de tecnologías específicas dentro de Airflow. Cada proveedor incluye una serie de operadores, ganchos y otros componentes que se han desarrollado y probado para interactuar con una tecnología específica, lo que simplifica la tarea de integrar Airflow con otras herramientas y servicios.

Los proveedores son mantendidos por la comunidad de Airflow y se actualizan regularmente para garantizar que sigan siendo compatibles con las últimas versiones de las tecnologías que soportan.

## Que es un sensor 

En Apache Airflow, un sensor es un tipo de operador que espera a que se cumpla una condición específica antes de continuar la ejecución del DAG. Un sensor se utiliza para esperar a que ocurra un evento o para detectar cambios en un sistema externo antes de continuar con el procesamiento del DAG.

Los sensores se implementan como subclases de la clase BaseSensorOperator. Los sensores suelen tener una condición que deben cumplir antes de que la ejecución del DAG continúe. La condición puede ser cualquier cosa, como un archivo que se crea, un mensaje que se recibe, un valor que se encuentra en una base de datos, etc.

Cuando se ejecuta un sensor, este comienza a comprobar si se ha cumplido la condición esperada. Si la condición aún no se ha cumplido, el sensor entra en un estado de espera y se programa para comprobar de nuevo después de un intervalo de tiempo determinado. Una vez que se cumple la condición esperada, el sensor sale del estado de espera y permite que la ejecución del DAG continúe.

```python
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
}

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='Un ejemplo de DAG con FileSensor',
    schedule_interval='@daily',
)

wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/path/to/my/file',
    poke_interval=60,
    dag=dag,
)

process_file = BashOperator(
    task_id='process_file',
    bash_command='process_file.sh /path/to/my/file',
    dag=dag,
)

wait_for_file >> process_file

```


