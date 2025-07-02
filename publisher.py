import time

from config import get_connection
import pika
import json

from consumer import consume_process


def produce_logs(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)
    for i in range(1, 100):
        json_message = {"event": "user registered", "user_id": i}
        dumped_json = json.dumps(json_message)
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=dumped_json
        )




def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            produce_logs(channel)


if __name__ == "__main__":
    main()