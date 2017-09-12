# This script template used to automatically create child services based on host triggers.

# Import api and connect to zabbix.
from zabbix_api import ZabbixAPI
zapi = ZabbixAPI(server="http://oemcc.fors.ru/zabbix321")
zapi.login("Admin", "zabbix")

# Set parent it-service name. In this setup its the same as agent's/host name.
a_zabbix_agents = [	
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

v_master_service = 'ODS_PROD'

# Create service block.
# Create parent services, based on host/agent names. Make them child of master service.
for i in range(0, len(a_zabbix_agents)):
   # Get master service id.
   v_parent_id = zapi.service.get({"filter":{"name": v_master_service}})[0]['serviceid']
   # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
   v_service_create_result = zapi.service.create({"name": a_zabbix_agents[i],"algorithm": 1,"showsla": 1,"goodsla": 99.99,"sortorder": 1})
   # Update parents dependencies. Get service id from preivous command result.
   zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": v_parent_id})

# Create trigger based services. Make them children of agetn/host services.
# todo: convert to function   	
for i in range(0, len(a_zabbix_agents)):
   # Get triggers for given agent.
   v_host_triggs = zapi.trigger.get({"filter":{"host": a_zabbix_agents[i]}})
   # Get parent serviceid.
   v_parent_id =  zapi.service.get({"filter":{"name": a_zabbix_agents[i]}})[0]['serviceid']
   # Create service based on trigger for selected host to be run in loop.
   for i in range(0, len(v_host_triggs)):
       # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
       v_service_create_result = zapi.service.create({"name": v_host_triggs[i]['description'],"algorithm": 1,"sortorder": 1,"showsla": 1,"goodsla": 99.99,"triggerid": v_host_triggs[i]['triggerid']})
       # Update parents dependencies. Get service id from preivous command result.
       zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": v_parent_id})

# Delete block.
# todo: convert to function
# Delete trigger-services.
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

# Delete host-services.
for i in range(0, len(a_zabbix_agents)):
   # Get serviceid.
   v_service_id =  zapi.service.get({"filter":{"name": v_master_service}})[0]['serviceid']
   zapi.service.delete([v_service_id])
