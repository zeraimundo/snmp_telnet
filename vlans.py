import getpass
import telnetlib


switches = ["192.168.0.211", "192.168.0.212"]
vlans = [(2, "Alunos"), (3, "Professores"), (4, "Tecnicos")]

user = input("Enter your remote account: ")
password = getpass.getpass()

for sw in switches:
    tn = telnetlib.Telnet(sw)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"conf t\n")

    for vlan in vlans:
        vlanNum = str(vlan[0]).encode('ascii')
        vlanName = vlan[1].encode('ascii')

        tn.write(b"int vlan " + vlanNum + b"\n")
        tn.write(b"lan-name " + vlanName + b"\n")
        tn.write(b"exit\n")
       
    tn.write(b"do wr\n")
    tn.write(b"exit\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))