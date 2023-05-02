from kafka import KafkaProducer
import json

# Crear un objeto KafkaProducer con la dirección del servidor de Kafka
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Definir el tópico al que se enviarán los mensajes
topic = 'mi-topico'

# Crear un mensaje para enviar como diccionario de Python
mensaje = {'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez'}

# Convertir el mensaje a formato JSON
mensaje_json = json.dumps(mensaje).encode('utf-8')

# Enviar el mensaje al tópico especificado
producer.send(topic, value=mensaje_json)

# Forzar el envío de todos los mensajes pendientes en la cola del producer
producer.flush()

# Cerrar la conexión del producer
producer.close()