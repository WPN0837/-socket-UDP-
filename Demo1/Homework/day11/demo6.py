import requests
def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
print(get('https://www.csdn.net/'))