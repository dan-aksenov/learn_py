from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://oemcc.fors.ru/zabbix321")
zapi.login("Admin", "zabbix")

# Set agent/host name. Also used as ITService name. Any way to do in dynamically or from file.
a_zabbix_agents = ['pts-tst-zab.fors.ru',
'pts-tst-as1.fors.ru',
'pts-tst-as2.fors.ru',
'pts-tst-db1c.fors.ru',
'pts-tst-db2c.fors.ru',
'pts-tst-bi.fors.ru',
'pts-tst-brm1.fors.ru',
'pts-dev-db.fors.ru',
'pts-tst-log.fors.ru',
'pts-dev-as2.fors.ru',
'pts-dev-as1.fors.ru'
]

# Create block.
# convert to function   	
for i in range(0, len(a_zabbix_agents)):
   # Get triggers for given agent.
   v_host_triggs = zapi.trigger.get({"filter":{"host": a_zabbix_agents[i]}})
   # Get parent serviceid.
   v_parent_id =  zapi.service.get({"filter":{"name": a_zabbix_agents[i]}})[0]['serviceid']
   # Create service based on trigger for selected host to be run in loop.
   for i in range(0, len(v_host_triggs)):
       # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
       v_service_create_result = zapi.service.create({"name": v_host_triggs[i]['description'],"algorithm": 1,"showsla": 1,"goodsla": 99.99,"sortorder": 1,"triggerid": v_host_triggs[i]['triggerid']})
       # Update parents dependencies. Get service id from preivous command result.
       zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": v_parent_id})

# Delete block.
a_zabbix_agents = ['skpdi.fors.ru']

# convert to function
for i in range(0, len(a_zabbix_agents)):
   # Get serviceid.
   v_parent_id =  zapi.service.get({"filter":{"name": a_zabbix_agents[i]}})[0]['serviceid']
   # Get his children.
   v_children =  zapi.service.get({"parentids": v_parent_id})
   for i in range(0, len(v_children)):
       # Get child id.
       v_child_id = v_children[i]["serviceid"]
       # Array mast be used to service.delete.
       zapi.service.delete([v_child_id])
