from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://oemcc.fors.ru/zabbix321")
zapi.login("Admin", "zabbix")

#list of servicenames-hosts to be here.

#get servicename-host.
v_srv_host = zapi.service.get({"filter":{"name":'pts-dev-db.fors.ru'}})[0]["hostid"]

v_srv_host = zapi.item.get({"filter":{"name":'pts-dev-db.fors.ru'}})[0]["hostid"]

v_host_triggs = zapi.trigger.get({"filter":{"name":'pts-dev-db.fors.ru'}})[0]["hostid"]

#get list of triggers for given host.
#v_host_triggs = zapi.trigger.get({"selectHosts": v_srv_host})

# Set agent/host name. Also used as ITService name.
v_zabbix_agent_name = 'pts-tst-db2c.fors.ru'

# Get triggers for given agent.
v_host_triggs = zapi.trigger.get({"filter":{"host": v_zabbix_agent_name}})

# Get parent serviceid.
v_parent_id =  zapi.service.get({"filter":{"name": v_zabbix_agent_name}})[0]['serviceid']

# Create service based on trigger for selected host to be run in loop.
for i in range(1, len(v_host_triggs)):
    # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
    v_service_create_result = zapi.service.create({"name": v_host_triggs[i]['description'],"algorithm": 1,"showsla": 1,"goodsla": 99.99,"sortorder": 1,"triggerid": v_host_triggs[i]['triggerid']})
    # Update parents dependencies. Get service id from preivous command result.
    zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": v_parent_id})
