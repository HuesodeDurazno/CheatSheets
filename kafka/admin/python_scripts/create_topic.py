
import logging
import os

from dotenv import load_dotenv

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError


logger = logging.getLogger()


load_dotenv(verbose=True)

client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
topic = NewTopic(name=os.environ['TOPICS_PEOPLE_BASIC_NAME'],
                num_partitions=int(os.environ['TOPICS_PEOPLE_BASIC_PARTITIONS']),
                replication_factor=int(os.environ['TOPICS_PEOPLE_BASIC_REPLICAS']))
try:
    client.create_topics([topic])
except TopicAlreadyExistsError as e:
    logger.warning("Topic already exists")
finally:
    client.close()

