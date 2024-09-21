import requests

url = 'https://www.pudim.com.br/'

try:
    requests.get(url)
except:
    print('Site offline ')
else:
    print('Site online')
