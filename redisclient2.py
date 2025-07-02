import redis

r = redis.Redis(
    host='redis-13152.c300.eu-central-1-1.ec2.redns.redis-cloud.com',
    port=13152,
    decode_responses=True,
    username="default",
    password="6BLQQz7Rnq4YdWzXMx0N7YtwTzAK7TB1",
)
pubsub = r.pubsub()
pubsub.subscribe('school')
r.publish('school', 'math')
r.publish('school', 'physics')
r.publish('school', 'Test: math')
for message in pubsub.listen():
    if message["type"] == "message":
        data = message["data"]
        if 'Test' in data:
            with open('mathtest.txt', mode='a', encoding='utf-8') as f:
                f.write(data + '\n')
