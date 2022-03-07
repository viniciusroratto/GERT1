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
import time

def create_agent(session):

    name = session.get('sysName.0')
    uptime = session.get('sysUpTimeInstance')
    ifnumber = session.get('ifNumber.0')
    services = session.get('sysServices.0')
    sistema = session.get('sysDescr.0')
    speed = session.get('ifSpeed.2')
    #session.set('sysContact.0', 'vini@gmail.com')
    contact = session.get('sysContact.0')
    inpacks = session.get('snmpInPkts.0')
    outpacks = session.get('snmpOutPkts.0')

    ifSpeed = session.get('ifSpeed.2')
    start = time.process_time()

    ifInOctets = session.get('ifInOctets.2')
    ifOutOctets = session.get('ifOutOctets.2')

    time.sleep(3)

    ifInOctets2 = session.get('ifInOctets.2')
    ifOutOctets2 = session.get('ifOutOctets.2')

    tempo= time.process_time() - start

    delta_in = int(ifInOctets2.value) - int(ifInOctets.value)
    delta_out = int(ifOutOctets2.value) - int(ifOutOctets.value)
 
    input_utilization =  (delta_in * 8 * 100)/(tempo * int(ifSpeed.value))
    output_utilization =  (delta_out * 8 * 100)/(tempo * int(ifSpeed.value))


    #ipv6_desc = session.set('ipv6DefaultHopLimit.0', '5')
    #print(ipv6_desc)


    #ALGUMAS OIBs INTERESSANTES

    largest_pkt = session.get('ipv6IfEffectiveMtu.2')
    ipIfStatsInDiscards = session.get('ipIfStatsInDiscards.2.2')
    ipIfStatsHCInReceives = session.get('ipIfStatsHCInReceives.2.2')

    

    dictionary = {

        'Nome do Sistema' : name.value,
        'Velocidade Max de Conexao' : speed.value,
        'Tempo de Conexao' : uptime.value,
        'Interfaces Conectadas' : ifnumber.value,
        'Sistema' : sistema.value,
        'Contato' : contact.value,
        'Pacotes Recebidos': inpacks.value,
        'Pacotes Enviados' : outpacks.value,
        'Utilizacao do Input:' : input_utilization,
        'Utilizacao do Output:' : output_utilization,
        'Tamanho do Maior Pacote:': largest_pkt.value,
        'Datagramas Recebidos:': ipIfStatsHCInReceives.value,
        'Datagramas Descartados por falha no buffer:': ipIfStatsInDiscards.value
    }
    
    return dictionary



session = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session2 = Session(hostname='127.0.0.1', version=3, security_level="auth_without_privacy", security_username="MD5User",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DEFAULT", privacy_password="The Net-SNMP Demo Password")

session3 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MYUSER01",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session4 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MYUSER02",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

session5 = Session(hostname='10.0.2.15', version=3, security_level="auth_with_privacy", security_username="MYUSER03",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

sessions_list = [create_agent(session), create_agent(session2), create_agent(session3), create_agent(session4), create_agent(session5)]

data = {
    'dataType' : 'Internet data accounting',
    'clients' : sessions_list
     }

import json

json_object = json.dumps(data, indent= 3)
with open ('./accounting-viewer/src/assets/dados.json', 'w') as f:
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


