# -*- coding: utf-8 -*-
# Для чтения русских комментов.

''' Автоматическое создание услуг Zabbix на основе узлов сети и их триггеров '''

# Import api and connect to zabbix.
from zabbix_api import ZabbixAPI

zapi = ZabbixAPI(server="http://oemcc.fors.ru/zabbix")
zapi.login("Admin", "zabbix")

def cre_master_service( master_service_name ):
    # Check if master service already exists.
    if not zapi.service.get({"output": "extend","filter":{"name":master_service_name}}):
        zapi.service.create({"name": master_service_name,"algorithm": 1,"showsla": 0,"sortorder": 1})
        print "Created Master service "+ master_service_name
    elif zapi.service.get({"output": "extend","filter":{"name":master_service_name}}):
        print "Master service " + master_service_name + " already exists."
    else:
        print "Something else."

# Create service block.
# Create parent services, based on host/agent names. Make them child of master service.
def cre_host_srv( master_service_name, zabbix_agents ):
    ''' Создание услуг на основе имен узлов сети, объявленных в массиве zabbix_agents '''
    #for i in range(0, len(a_zabbix_agents)):
    for zabbix_agent in zabbix_agents:
        # Get master service id.
        v_parent_id = zapi.service.get({"filter":{"name": master_service_name}})[0]['serviceid']
        # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
        if not zapi.service.get({"output": "extend","filter":{"name":zabbix_agent}}):
            v_service_create_result = zapi.service.create({"name": zabbix_agent,"algorithm": 1,"showsla": 0,"sortorder": 1})
            # Update parents dependencies. Get service id from preivous command result.
            zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": v_parent_id})
            print("Created service " + zabbix_agent)
        elif zapi.service.get({"output": "extend","filter":{"name":zabbix_agent}}):
            print("Service " + zabbix_agent + " already exists.")
        else:
            print("Something else.")

# Create trigger based services. Make them children of agetn/host services.
 
def cre_trig_sev(zabbix_agents):
    ''' Для каждой услуги-узла создание потомков на основе триггеров '''
    for i in range(0, len(zabbix_agents)):
        # Get triggers for given agent.
        v_host_triggs = zapi.trigger.get({"filter":{"host": zabbix_agents[i]}})
        # Get parent serviceid.
        v_parent_id =  zapi.service.get({"filter":{"name": zabbix_agents[i]}})[0]['serviceid']
        # Create service based on trigger for selected host to be run in loop.
        for i in range(0, len(v_host_triggs)):
            #check if service for this triggerid already exists
            if not zapi.service.get({"output": "extend","filter":{"triggerid":v_host_triggs[i]['triggerid']}}):
                # Variable v_service_create_result to hold service creation result. This will be used to get serviceid for dependencies update.
                v_service_create_result = zapi.service.create({"name": v_host_triggs[i]['description'],"algorithm": 1,"showsla": 0,"sortorder": 1,"triggerid": v_host_triggs[i]['triggerid']})
                # Update parents dependencies. Get service id from preivous command result.
                zapi.service.update({"serviceid": v_service_create_result['serviceids'][0],"parentid": v_parent_id})
                #print "Creating service for trigger " + v_host_tirggs[i]['triggerid']
            elif zapi.service.get({"output": "extend","filter":{"triggerid":v_host_triggs[i]['triggerid']}}):
                print "Service for trigger " + v_host_triggs[i]['triggerid'] + " already exists."
            else:
                print "Something else..."

# Delete block.
# Delete trigger-services.
def del_trig_srv(zabbix_agents):
    ''' Удаление услуг на основе триггеров'''
    for i in range(0, len(zabbix_agents)):
        # Get serviceid.
        v_parent_id =  zapi.service.get({"filter":{"name": zabbix_agents[i]}})[0]['serviceid']
        # Get his children.
        v_children =  zapi.service.get({"parentids": v_parent_id})
        for i in range(0, len(v_children)):
            # Get child id.
            v_child_id = v_children[i]["serviceid"]
            # Array mast be used to service.delete.
            zapi.service.delete([v_child_id])

# Delete host-services. -- to be fixed, and error handling added    
def del_host_srv(zabbix_agents):
    ''' Удаление услуг на основе узлов сети '''
    for i in range(0, len(zabbix_agents)):
        # Get serviceid.
        v_service_id =  zapi.service.get({"filter":{"name": zabbix_agents[i]}})[0]['serviceid']
        zapi.service.delete([v_service_id])

def main():
    # Master service. Here based on IT product name.
    master_service_name = raw_input("Enter master service name: ")
    
    #global a_zabbix_agents
    # Set parent it-service name. In this setup its the same as agent's/host name.
    zabbix_agents = raw_input("Enter space separated list of zabbix agents: ")
    zabbix_agents = zabbix_agents.split()
        
    cre_master_service(master_service_name)
    cre_host_srv(master_service_name,zabbix_agents)
    cre_trig_sev(zabbix_agents)
    
if __name__ == '__main__':
    main()
