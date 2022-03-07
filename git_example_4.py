from easysnmp import Session
import time
start = time.process_time()


session = Session(hostname='192.168.0.107', version=3, security_level="auth_with_privacy", security_username="MD5DESUser",
auth_protocol="MD5", auth_password="The Net-SNMP Demo Password",
privacy_protocol="DES", privacy_password="The Net-SNMP Demo Password")



# = session.get('')
#print('', )



#LINK RORATTO
ifSpeed = session.get('ifSpeed.2')
print('ifSpeed', ifSpeed)

start = time.process_time()

ifInOctets = session.get('ifInOctets.2')
print('ifInOctets', ifInOctets)
ifOutOctets = session.get('ifOutOctets.2')
print('ifOutOctets', ifOutOctets)

time.sleep(3)

ifInOctets2 = session.get('ifInOctets.2')
print('ifInOctets', ifInOctets)
ifOutOctets2 = session.get('ifOutOctets.2')
print('ifOutOctets', ifOutOctets)

tempo= time.process_time() - start
print('time=', tempo) 

delta_in = int(ifInOctets2.value) - int(ifInOctets.value)
print('octets delta in: ', delta_in)
delta_out = int(ifOutOctets2.value) - int(ifOutOctets.value)
print('octets delta out: ', delta_out)
input_utilization =  (delta_in * 8 * 100)/(tempo * int(ifSpeed.value))
output_utilization =  (delta_out * 8 * 100)/(tempo * int(ifSpeed.value))
print('ifspeed',int(ifSpeed.value))
print('input_utilization: ',input_utilization,'%')
print('output_utilization: ',output_utilization,'%')


#ipv6_desc = session.set('ipv6DefaultHopLimit.0', '5')
#print(ipv6_desc)


#ALGUMAS OIBs INTERESSANTES
print('ALGUMAS OIBs INTERESSANTES:')
largest_pkt = session.get('ipv6IfEffectiveMtu.2')
print('largest pkt =', largest_pkt)
ipIfStatsInDiscards = session.get('ipIfStatsInDiscards.2.2')
print('ipIfStatsInDiscards', ipIfStatsInDiscards)
ipIfStatsHCInReceives = session.get('ipIfStatsHCInReceives.2.2')
print('ipIfStatsHCInReceives', ipIfStatsHCInReceives)
ipv6_desc = session.get('ipv6DefaultHopLimit.0')
print(ipv6_desc)
