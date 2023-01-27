import requests

url = 'http://127.0.0.1:1880/test-input'
myobj = {'test': '1'}
ss = 1
x = requests.post(url, json = myobj)

print(x.text)