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


session = Session(hostname='192.168.0.107', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")

#session3.walk("1.3.6.1.4.1.9.9.166.1.15.1.1.2")

name = session.get('sysName.0')
uptime = session.get('sysUpTimeInstance')
ifnumber = session.get('ifNumber.0')
services = session.get('sysServices.0')
#walk = []
#walk = session.walk()
# processos = session.get('sysUpTimeInstance')
# Agora basta imprimir a variavel name
print (name,'\n')
print ("name.value",name.value,"\n")
print ('name.snmp_type',name.snmp_type,'\n')
print ('uptime: ',uptime,'\n')
print ('services: ',services,'\n')
print ('ifnumber: ',ifnumber,'\n')
print ('ifnumber.value: ',int(ifnumber.value),'\n')
#print ('walk: ',walk,'\n')
