import requests
#import json

headers = {'Host': 'skpdi.fors.ru',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': '/',
'Accept-Language': 'ru-RU,en-US;q=0.8,ru;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Access-Control-Request-Method': 'GET',
'Access-Control-Request-Headers': 'authorization',
'Referer': 'http://skpdi.mkropachev:8082/report?1&code=InteractiveMapPanel&bk=ODH/Base/DrivewayMap',
'Origin': 'http://skpdi.mkropachev:8082',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive'}


#url = 'https://skpdi.mosreg.ru/wms/cache/?layers=m10&service=WMS&request=GetMap&layers=&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&height=256&width=256&srs=EPSG%3A3857&bbox=4346515.176408262,7452916.005917824,4348961.161313388,7455361.990822956'
url = 'http://skpdi.fors.ru/map/0/0/0.png'

#page = requests.get( url, auth=('map', '123'))
page = requests.options( url , headers=headers, auth=('map', '123') )
print('\n auth and headers')
print ('Access-Control-Allow-Origin' in ( page.headers ))
print(page.headers)
print( page.status_code )

print('\n NO auth, headers')
page = requests.options( url , headers=headers )
print ('Access-Control-Allow-Origin' in ( page.headers ))
print(page.headers)
print( page.status_code )

print('\n auth and NO headers')
page = requests.options( url,  auth=('map', '123') )
print ('Access-Control-Allow-Origin' in ( page.headers ))
print( page.status_code )

print('\n NO auth ando NO headers')
page = requests.options( url )
print ('Access-Control-Allow-Origin' in ( page.headers ))
print( page.status_code )