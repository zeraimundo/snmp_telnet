
import getpass
import telnetlib


routers = ["192.168.0.201", "192.168.0.202", "192.168.0.203"]

snmpCommunities = ["community-r01", "community-r02", "community-r03"]

user = input("Enter your remote account: ")
password = getpass.getpass()

for i, rt in enumerate(routers):
    tn = telnetlib.Telnet(rt)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"conf t\n")

    tn.write(
        b"snmp-server community " + 
        snmpCommunities[i].encode('ascii') + 
        b" ro\n"
    )
    
       
    tn.write(b"do wr\n")
    tn.write(b"exit\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))

   