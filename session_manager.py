from easysnmp import Session

class SES_MGR():
    test = "HALO"
    def __init__(self, hostname = u'localhost',
                       security_level = 'authNoPriv',
                       security_username = 'SNMPUSER',
                       auth_protocol = 'DEFAULT',
                       auth_password = '123456789DEZ',
                       privacy_protocol = u'DEFAULT',
                       privacy_password = '123456789DEZ'):

        self.session = Session(hostname = hostname,
                       version = 3,
                       security_level = security_level,
                       security_username = security_username,
                       auth_password = '123456789DEZ',
                       auth_protocol = auth_protocol,
                       privacy_protocol = privacy_protocol,
                       privacy_password = privacy_password)

    def get(self, oid):
        return self.session.get(oid)




# Create an SNMP session to be used for all our requests
session = SES_MGR()

# You may retrieve an individual OID using an SNMP GET
location = session.get('sysLocation.0')

# You may also specify the OID as a tuple (name, index)
# Note: the index is specified as a string as it can be of other types than
# just a regular integer
contact = session.get(('sysContact', '0'))

# And of course, you may use the numeric OID too
description = session.get('.1.3.6.1.2.1.1.1.0')

# Set a variable using an SNMP SET
#session.set('sysLocation.0', 'The SNMP Lab')

# Perform an SNMP walk
system_items = session.walk('system')

# Each returned item can be used normally as its related type (str or int)
# but also has several extended attributes with SNMP-specific information
for item in system_items:
    print('{oid}.{oid_index} {snmp_type} = {value}'.format(oid=item.oid,oid_index=item.oid_index, snmp_type=item.snmp_type, value=item.value))





