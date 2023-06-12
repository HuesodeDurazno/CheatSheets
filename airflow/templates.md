## Que son 

los templates se utilizan para parametrizar y reutilizar código en las tareas. Permiten definir valores dinámicos que se pueden pasar a través de variables o argumentos al momento de ejecutar las tareas.

## Definir un template: 

Puedes definir un template utilizando el formato Jinja, que es el motor de plantillas utilizado por Airflow. Los templates se definen utilizando doble llave ({{ }}) para indicar los campos variables. Por ejemplo, si quieres parametrizar una consulta SQL en una tarea de Airflow, puedes definirlo de la siguiente manera:

    sql_template = "SELECT * FROM my_table WHERE date = '{{ ds }}'"

## Pasar templates a una tarea: 

Puedes pasar templates a una tarea utilizando el argumento templates_dict en la definición de la tarea. Por ejemplo:

    my_task = BashOperator(
        task_id='my_task',
        bash_command='echo {{ my_param }}',
        templates_dict={'my_param': 'Hello, {{ name }}'}
    )

## Usar templates en macros y operadores: 

Además de pasar templates directamente a una tarea, puedes utilizar templates en las macros y operadores de Airflow. Por ejemplo, puedes usar el template {{ ds }} para acceder a la fecha de ejecución en una expresión:

    my_task = BashOperator(
        task_id='my_task',
        bash_command='echo {{ ds }}',
    )

## Configurar variables: 
Airflow también proporciona las variables de Airflow, que son valores dinámicos almacenados en la base de datos de metadatos. Puedes definir y configurar variables utilizando la interfaz de línea de comandos de Airflow o la API. Estas variables se pueden acceder en los templates utilizando el formato {{ var.value.my_variable_name }}.

## Pasar templates como argumentos: 

Además de utilizar templates_dict para pasar templates a una tarea, también puedes utilizar el argumento params para pasar templates a través de variables. Por ejemplo:

    my_task = PythonOperator(
        task_id='my_task',
        python_callable=my_function,
        params={'my_param': 'Hello, {{ name }}'}
    )

