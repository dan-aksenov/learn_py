from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://oemcc.fors.ru/zabbix321")
zapi.login("Admin", "zabbix")
#zapi.host.create({ "host": "Linux server", "interfaces": [ { "type": 1, "main": 1, "useip": 1, "ip": "192.168.3.1", "dns": "", "port": "10050" } ], "groups": [ { "groupid": "1" } ], "templates": [ { "templateid": "10001" } ], "inventory_mode": 0, "inventory": { "macaddress_a": "01234", "macaddress_b": "56768" } })

#list of servicenames-hosts to be here.

#get servicename-host.
v_srv_host = zapi.service.get({"filter":{"name":'pts-dev-db.fors.ru'}})[0]["hostid"]

v_srv_host = zapi.item.get({"filter":{"name":'pts-dev-db.fors.ru'}})[0]["hostid"]

v_host_triggs = zapi.trigger.get({"filter":{"name":'pts-dev-db.fors.ru'}})[0]["hostid"]

#get list of triggers for given host
#v_host_triggs = zapi.trigger.get({"selectHosts": v_srv_host})

#set agent/host
v_zabbix_agent_name = 'pts-tst-db2c.fors.ru'

# Get triggers for given agent
v_host_triggs = zapi.trigger.get({"filter":{"host": zabbix_agent_name}})

# Create service based on trigger for selected host to be run in loop.
for i in range(1, len(v_host_triggs)):
    # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
    v_service_create_result = zapi.service.create({"name": v_host_triggs[i]['description'],"algorithm": 1,"showsla": 1,"goodsla": 99.99,"sortorder": 1,"triggerid": v_host_triggs[i]['triggerid']})
    # Update parents dependencies. Get service id from preivous command result.
    zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": "24"})
