import requests

response = requests.get('https://www.baidu.com/')
print(response.content)
