import requests
#import json

#headers = {'auth-header': 'auth-tocken'}
headers = {'Upgrade-Insecure-Requests': '0'}

url = 'https://skpdi.mosreg.ru/wms/cache/?layers=m10&service=WMS&request=GetMap&layers=&styles=&format=image%2Fjpeg&transparent=false&version=1.1.1&height=256&width=256&srs=EPSG%3A3857&bbox=4346515.176408262,7452916.005917824,4348961.161313388,7455361.990822956'
page = requests.get( url , headers=headers )
#print( page.headers )
#print( "Система контроля и планирования работ в области дорожной инфраструктуры" in page.text )

print( page.status_code )