#!/usr/local/bin/python3

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

session3 = Session(hostname='192.168.2.72', version=3,
security_level="auth_with_privacy", security_username="EASYSNMP",
auth_protocol="SHA", auth_password="AUTHPASS",
privacy_protocol="AES", privacy_password="PRIVPASS")

session3.walk("1.3.6.1.4.1.9.9.166.1.15.1.1.2")
