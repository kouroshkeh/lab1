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

github_raw_url = "https://raw.githubusercontent.com/kouroshkeh/lab1/master/test.py"

try:
    response = requests.get(github_raw_url)
    response.raise_for_status()

    print(response.text)
except requests.exceptions.RequestException as e:
    print(e)