import requests

requests_version = requests.__version__
print(f"Requests Library Version: {requests_version}")


url = "http://www.google.com"
try:
    response = requests.get(url)
    response.raise_for_status() 
    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)