# Comandos base 

Listar topics

    kafka-topics --list --boostrap-server [broker:port]

Crear topics

    kafka-topics --create --boostrap-server [broker:port] --topic [name] --partitions [number of partition] --replication-factor [replication_number]

    EX:

    kafka-topics --list --bootstrap-server broker0:29092, broker1 :29093, broker2:29094

Describir topics

    kafka-topics --describe --bootstrap-server [brokers:port] --topic [name]

    EX

    kafka-topics --describe --bootstrap-server broker0:29092 --topic people

Eliminar topics

    kafka-topics --delete --bootstrap-server [brokers:port] --topic [name]

    EX

    kafka-topics --delete --bootstrap-server broker0:29092 --topic people

Crear un topic con diferente retencion

    kafka-topics --create --bootstrap-server [broker:port] --topic [name] --config retention.ms=[milisenconds]

    EX

    kafka-topics --create --bootstrap-server broker0:29092 --topic experiments --config retention.ms=30000

Cambiar la retencion deun topic

    Kafka-configs --bootstrap-server broker@:29892 --alter --entity-type topics --entity-name experiments --add-config retention.ms=500000

Crear compacted Topic

    kafka-topics --create --bootstrap-server broker0:29092 --topic experiments. latest --config cleanup.policy=compact

View Topic Configs

    kafka-configs --describe --all --bootstrap-server broker@:29092 --topic experiments

    kafka-configs --describe --all --bootstrap-server broker0:29092 --topic experiments.latest
