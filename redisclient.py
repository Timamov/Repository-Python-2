"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-13152.c300.eu-central-1-1.ec2.redns.redis-cloud.com',
    port=13152,
    decode_responses=True,
    username="default",
    password="6BLQQz7Rnq4YdWzXMx0N7YtwTzAK7TB1",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar
r.set('myKey', 'ww3efrhb')

# string
# r.set('myKey', 'secret data')
# r.set('myKeyTTL23', 'secret dataTTL32', ex=15)
# r.set('myKeyTTL236666666666', 'secret dataTTL32', exat=datetime.datetime(year=2025, month=5, day=15, hour=3))

# lists
'''r.lpush('myList', 'elem1left0')
r.rpush('myList', 'elem right')
r.expire('myList', 3500)

r.delete('myList')

r.hset('user:1235654', mapping={'city': 'Odesa'})
r.expire('1234564', time=200)
r.incr('views', 6)
print(r.get('views'))

pubsub.subscribe('news')
pubsub.subscribe('weather')
for message in pubsub.listen():
    print(message)


r.set('favouriteCar', 'Audi q7 e-tron 2025')
r.set('favouritePet', 'Golden rethryver dog')
r.expire('favouritePet', 7200)
'''
'''r.lpush('products', 'Milk', 'eggs', 'fruits', 'vegetables')
r.expire('products', 604800)'''
r.hset('recipes', mapping={'flour': 250, 'milk': 500, 'cream': 1000, 'cherry': 25, 'lemon': 89})
r.hset('recipes', 'sugar', '300')
r.hset('recipes', 'sugar', '500')
r.delete('recipes')

pubsub = r.pubsub()
pubsub.subscribe('school')

