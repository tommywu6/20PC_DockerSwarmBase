import pickle

import codecs

import pika


def run():
    credentials = pika.PlainCredentials(
        "demo",
        "demo"
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="rabbitmq-01",
            credentials=credentials,
            heartbeat_interval=60,
            socket_timeout=60,
        )
    )
    channel = connection.channel()

    arguments = dict()
    channel.queue_declare(
        queue="demo",
        auto_delete=False,
        durable=True,
        arguments=arguments
    )

    state = channel.basic_publish(
        exchange='',
        routing_key="demo",
        body=codecs.encode(
            pickle.dumps(
                {"data": "test"}
            ), "base64"
        ).decode()
    )
