from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://oemcc.fors.ru/zabbix321")
zapi.login("Admin", "zabbix")
zapi.host.create({ "host": "Linux server", "interfaces": [ { "type": 1, "main": 1, "useip": 1, "ip": "192.168.3.1", "dns": "", "port": "10050" } ], "groups": [ { "groupid": "1" } ], "templates": [ { "templateid": "10001" } ], "inventory_mode": 0, "inventory": { "macaddress_a": "01234", "macaddress_b": "56768" } })