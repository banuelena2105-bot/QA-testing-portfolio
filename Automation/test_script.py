import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    print("Test Passed")
else:
    print("Test Failed")
