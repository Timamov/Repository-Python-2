import time

from config import get_connection
import pika
import json

def consume_logs(channel, method, properties, body):
    load_json = json.loads(body)
    print(f'New_log: {load_json}')
    time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)

def consume_process(channel: pika.adapters.blocking_connection.BlockingChannel):
    QUEUE = 'logs'
    channel.queue_declare(queue=QUEUE)
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=consume_logs,
        # auto_ack=True
    )

    channel.start_consuming()


def main():
    with get_connection() as connection:
        with connection.channel() as channel:
            consume_process(channel)


if __name__ == "__main__":
    main()