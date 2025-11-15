import json
import requests
import os
from dotenv import load_dotenv  # pip install python-dotenv

# ✅ Example of a JSON-like Python dictionary
var = {
    "name": "Alice",
    "age": "25",
    "is_student": False,
    "subjects": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}

#  Dictionary with mixed key types (not all valid in JSON)
dictionary = {
    'name': 'Alice',
    "age": 25,
    "city": "New York",
    1: 'one',           # Valid in Python, not in JSON
    (3, 4): "Tuple"     # Tuples as keys are not supported in JSON
}

#  Convert Python dictionary to JSON string
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
json_data = json.dumps(data)
print(type(json_data))  # <class 'str'>

#  Convert JSON string to Python dictionary
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
python_dict = json.loads(json_string)
print(python_dict["name"])  # Output: Alice

#  Write JSON to a file
data2 = {
    "name": "Bob",
    "age": 30,
    "city": "London"
}
with open("data.json", "w") as file:
    json.dump(data2, file, indent=4)

#  Format JSON for readability
json_data = json.dumps(data, indent=4, sort_keys=True)
print(json_data)

#  GET request (Fetch data)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
data = response.json()
print(data)

#  POST request (Send data)
url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "New Post", "body": "This is a new post", "userId": 1}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
print(response.json())

#  PUT request (Update data)
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"title": "Updated Post", "body": "Bright received a strike", "userId": 1}
response = requests.put(url, json=payload)
print(response.json())

#  DELETE request (Remove data)
url = "https://jsonplaceholder.typicode.com/posts/2"
response = requests.delete(url)
print(response.status_code)  # 200 means success

#  Handling API Authentication with Bearer Token
url = "https://jsonplaceholder.typicode.com/posts/1"
headers = {"Authorization": "Bearer 568ghjji866gji897617rg"}
response = requests.get(url, headers=headers)
print(response.status_code)

#  OAuth2 Authentication (example structure)
client_id = "your_client_id"
client_secret = "your_client_secret"
token_url = "https://example.com/oauth/token"
# You would typically send a POST request to token_url with client_id and client_secret

#  Load environment variables
load_dotenv()
client_secret2 = os.getenv("CLIENT_SECRET")
print(client_secret2)
client_key = os.getenv("CLIENT_KEY")
print(client_key)
