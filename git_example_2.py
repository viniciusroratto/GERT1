#!/usr/local/bin/python3
from easysnmp import Session

hostname = "192.168.0.25"
security_username = "testuser"
auth_password = "shaToken"
privacy_password = "aesToken"

session3 = Session(hostname=hostname, version=3, security_level="auth_with_privacy", security_username=security_username, auth_protocol="SHA", auth_password=auth_password, privacy_protocol="AES", privacy_password=privacy_password)

print(session3.walk("1.3.6.1.2.1.1.1"))
