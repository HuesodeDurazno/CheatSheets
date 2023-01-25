1. Instalar extension dev_containers
2. Ctrl+Ship+P y escribir  : **Remote-Containers: Attach to a Running Container…**
3. Seleccionar contenedor de airflow
4. Instalar extension de python (Se podria ver la posibilidad de agregar directamente en el config remote container.json)
5. En el menu de debug crear el siguiente archivo de launch'

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Airflow Test",
            "type": "python",
            "request": "launch",
            "program": "/usr/local/bin/airflow",
            "console": "integratedTerminal",
            "args": [
                "tasks",
                "test",
                "DAG_report_ad_V2",
                "run_main",
                "01-25-2022"
            ]
        }
    ]
}
```
Lo que hace el archivo launch.json es ejecutar un comando de la cli de airflow (https://airflow.apache.org/docs/apache-airflow/1.10.15/cli-ref.html?highlight=test#test) , En la version 1.10/15 solo se puede ejecutar task por task y no todo el dag completo , por lo que se tendra que testear por cada task.

Los parametros que tendrian que cambiar serian solamente ```DAG_report_ad_V2``` que indica el dag_id donde esta su task , ```run_main``` que es el task_id a debugear y por ultimo la fecha de ejecucion.

6. Una vez teniendo este launch.json puedes poner tus breakpoints y ejecutar el debuger y se ejecutara como un debuger normal.