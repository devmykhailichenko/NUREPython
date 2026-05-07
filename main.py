import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Accept": "application/json",
    "User-Agent": "Python example v 1.1"
}

params = {
    "userId": 1
}

response = requests.get(
    BASE_URL,
    headers=headers,
    params=params
)

new_post = {
    "title": "My first post",
    "body": "This is my first",
    "userId": 1
}

response_post = requests.post(
    BASE_URL,
    headers={"Content-Type": "application/json"},
    json=new_post
)


if response_post.status_code == 200:
    print(response_post, response_post.json())
else:
    print("ERROR")