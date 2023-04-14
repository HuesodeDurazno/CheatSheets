## Datasets

Un conjunto de datos , en airflow la clase Datasets nos va a servir para producir o actualizar cierto dataset o bien para usarlo como una ejecucion de ejecucion

Producer 

```Python
    from airflow import DAG,Dataset
    from airflow.decorators import task

    from datetime import date,datetime

    my_file=Dataset("/tmp/my_file.txt")

    with DAG(
        dag_id="producer",
        schedule="@daily",
        start_date=datetime(2022,1,1)
        catchup=False
    ):
        @task(outlets=[my_file])
        def update_dataset():
            with open(my_file.uri,"a+") as f:
                f.write("next_line")

        update_dataset()

```

Consumer , en el caso de que queramos ocupar como condicion de triger una Dataset,actualizacion o creacion

```python
    from airflow import DAG,Dataset
    from airflow.decorators import task

    from datetime import date,datetime

    my_file=Dataset("/tmp/my_file.txt")

    with DAG(
        dag_id="consumer",
        schedule=[my_file],
        start_date=datetime(2022,1,1)
        catchup=False
    ):
        
         @task
         def read_dataset():
            with open(my_file.uri,"r") as f:
                print(f.read())


        read_dataset()
```