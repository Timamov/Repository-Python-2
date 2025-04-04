import requests

url='https://moemisto.ua/img/cache/blog_show_photo/blog/0004/75/fe2a5835d6d62a84d64cc357061c8186a244a1a8.jpeg?hash=2020-03-02-20-38-21'

response = requests.get(url)

with open('spring.jpeg', mode='wb') as file:
    file.write(response.content)

with open('spring.jpeg', mode='rb') as f:
    print(f.read())
pass