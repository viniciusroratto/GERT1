# !/usr/local/bin/python3

'''
snmp-server view SV_EASYSNMP interfaces included
snmp-server view SV_EASYSNMP ciscoCdpMIB included
snmp-server view SV_EASYSNMP ciscoCBQosMIB included
 
ip access-list standard ACL_SNMP
 permit 192.168.2.89
 
snmp-server group SG_EASYSNMP v3 auth read SV_EASYSNMP access ACL_SNMP
 
snmp-server user EASYSNMP SG_EASYSNMP v3 auth sha AUTHPASS priv aes 128 PRIVPASS
'''


from easysnmp import Session
import json

def create_agent(session):

    name = session.get('sysName.0')
    uptime = session.get('sysUpTimeInstance')
    ifnumber = session.get('ifNumber.0')
    services = session.get('sysServices.0')
    sistema = session.get('sysDescr.0')
    speed = session.get('ifSpeed.1')
    #session.set('sysContact.0', 'vini@gmail.com')
    contact = session.get('sysContact.0')
    inpacks = session.get('snmpInPkts.0')
    outpacks = session.get('snmpOutPkts.0')

    dictionary = {

        'Nome do Sistema' : name.value,
        'Tempo de Conexao' : uptime.value,
        'Conections' : ifnumber.value,
        'Sistema' : sistema.value,
        'Velocidade de Conexao' : speed.value,
        'Contato' : contact.value,
        'inPacks': inpacks.value,
        'outPacks' : outpacks.value
    }
    
    return dictionary



session = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session2 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session3 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session4 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session5 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

sessions_list = [create_agent(session), create_agent(session2), create_agent(session3), create_agent(session4), create_agent(session5)]

data = {
    'dataType' : 'Internet data accounting',
    'clients' : sessions_list
     }

import json

json_object = json.dumps(data, indent= 3)
with open ('data2.json', 'w') as f:
    f.write(json_object)


print(json_object)

'''
# Agora basta imprimir a variavel name
print ("name.value",name.value,"\n")
print ('uptime: ',uptime.value,'\n')
print ('ifnumber.value: ',int(ifnumber.value),'\n')
print ('Sistema: ', sistema.value, '\n')
print ('Speed:  ', int(speed.value)/1000000, 'Mb/s\n')
print ('Contact:  ', contact.value, '\n')
print ('In:  ', inpacks.value, '\n')
print ('out: ', outpacks.value, '\n')

walk = []
walk = session.walk()

oidlist = []
for each in walk:
    oidlist.append(each.oid)

valuelist = []
for each in walk:
    valuelist.append([each.value])

indexlist = []
for each in walk:
    indexlist.append(each.oid_index)

import csv
with open('oid_list.csv', 'w') as f:
    write= csv.writer(f)
    write.writerows(zip(oidlist, valuelist, indexlist))
'''


