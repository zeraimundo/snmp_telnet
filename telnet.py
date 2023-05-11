import getpass
import telnetlib

# Switch S1 - 192.168.0.211
# Switch S2 - 192.168.0.212
# Switch S3 - 192.168.0.213
# Switch S4 - 192.168.0.214

HOST = "10.0.4.95"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"conf t\n")
tn.write(b"snmp-server community raimundo ro\n")
tn.write(b"do wr\n")
tn.write(b"exit\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))