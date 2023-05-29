from kafka import KafkaConsumer
from kafka import serializers

# Configuración del consumidor
bootstrap_servers = 'localhost:9092'  # Dirección y puerto del servidor de Kafka
topic = 'mi_tema'                     # Tema al que se suscribe el consumidor
group_id = 'mi_grupo'                 # Identificador único para el grupo de consumidores

# Definir un serializador personalizado para la clave
def key_deserializer(key):
    # Aquí puedes implementar tu propia lógica de deserialización de la clave
    # Por ejemplo, si las claves son cadenas en formato JSON:
    return json.loads(key)

# Definir un serializador personalizado para el valor
def value_deserializer(value):
    # Aquí puedes implementar tu propia lógica de deserialización del valor
    # Por ejemplo, si los valores son cadenas en formato JSON:
    return json.loads(value)

# Crear una instancia del consumidor
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id,
    key_deserializer=key_deserializer,
    value_deserializer=value_deserializer
)

# Leer y procesar los mensajes
for mensaje in consumer:
    clave = mensaje.key        # Obtener la clave deserializada
    valor = mensaje.value      # Obtener el valor deserializado del mensaje
    print(clave, valor)        # Procesar la clave y el valor según la lógica de negocio

# Cerrar el consumidor al finalizar
consumer.close()