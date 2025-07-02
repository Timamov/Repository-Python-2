import ssl

import pika

RMQ_HOST = 'collie-01.lmq.cloudamqp.com'
RMQ_PASSWORD = 'AFb8xMRp-HM6H_huSqympjyvk8rPn-QD'
RMQ_PORT = 5671
USER = 'ittxoalt'
VHOST = 'ittxoalt'
ssl_context = ssl.create_default_context()
connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    virtual_host=VHOST,
    credentials=pika.PlainCredentials(username=USER, password=RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)
def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)