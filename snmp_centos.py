from snmp_cmds import snmpwalk


addr = '192.168.0.68'
port = 161
community = 'jr'

oids = [
    ('Processador', '1.3.6.1.2.1.25.3.2.1.3'), # Ficou feio mas não consegui fazer de outra forma
    ('Hostname', '1.3.6.1.2.1.1.5.0'),
    ('Uptime', '1.3.6.1.2.1.1.3.0'),
    ('Cpu utilization (%)', '1.3.6.1.4.1.2021.11.9.0'),
    ('Memmory used (bytes)', '1.3.6.1.4.1.2021.4.6.0'),
    ('Memmory free (bytes)', '1.3.6.1.4.1.2021.4.11.0'),
    ('IPs', '1.3.6.1.2.1.4.20.1.1'),
    ('Interface MAC', '1.3.6.1.2.1.2.2.1.6'),
    ('Network Interface names', '1.3.6.1.2.1.2.2.1.2'),
    ('Interface RX bits', '1.3.6.1.2.1.2.2.1.10'),
    ('Interface TX bits', '1.3.6.1.2.1.2.2.1.16'),
  
]

for oid in oids:
    if oid[1]:
        query = snmpwalk(
            ipaddress=addr,
            oid=oid[1],
            community=community,
            port=port
        )

        query = [q[1] for q in query]
        query = ', '.join(query)

        print(f'\033[1m{oid[0]}:\033[0m \033[2m{query}\033[0m')