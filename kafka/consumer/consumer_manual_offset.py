from kafka import KafkaConsumer
from kafka import TopicPartition

# Configuración del consumidor
bootstrap_servers = 'localhost:9092'  # Dirección y puerto del servidor de Kafka
topic = 'mi_tema'                     # Tema al que se suscribe el consumidor
group_id = 'mi_grupo'                 # Identificador único para el grupo de consumidores

# Crear una instancia del consumidor
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    enable_auto_commit=False  # Desactivar el auto commit
)

# Asignar particiones al consumidor
particiones = consumer.partitions_for_topic(topic)
asignaciones = [TopicPartition(topic, particion) for particion in particiones]
consumer.assign(asignaciones)

# Leer y procesar los mensajes
try:
    while True:
        registros = consumer.poll(timeout_ms=100)  # Leer registros con un tiempo de espera
        for particion, registros_particion in registros.items():
            for registro in registros_particion:
                clave = registro.key
                valor = registro.value
                offset = registro.offset

                # Procesar la clave, valor y offset según la lógica de negocio

        consumer.commit()  # Confirmar el procesamiento exitoso de los registros
except KeyboardInterrupt:
    pass
finally:
    consumer.close()