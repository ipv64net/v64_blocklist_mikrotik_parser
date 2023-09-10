# v64_blocklist_mikrotik_parser
These Script Read die Mikrotik Firewall IP Address List and sent it to v64_Blocklist.

# 1. Install requirements

pip3 install -r requirements.txt

# 2. Edit global variables

Edit the global variables in the python file

# 3. Test it

run /usr/bin/python3 v64_blocklist_mikrotik_parser.py and see if everything is working correctly

# 4. Crontab
*/15 * * * * cd /root/v64_blocklist_mikrotik_parser && /usr/bin/python3 v64_blocklist_mikrotik_parser.py

## Mikrotik Example Rules to Detect something.....

add action=jump chain=input dst-port=22 in-interface-list=WANs jump-target=Tarpit protocol=tcp
add action=jump chain=input dst-port=21 in-interface-list=WANs jump-target=Tarpit protocol=tcp
add action=jump chain=input dst-port=3389 in-interface-list=WANs jump-target=Tarpit protocol=tcp
add action=jump chain=input dst-port=3306 in-interface-list=WANs jump-target=Tarpit protocol=tcp
add action=jump chain=input dst-port=25 in-interface-list=WANs jump-target=Tarpit protocol=tcp
add action=jump chain=input in-interface-list=WANs jump-target=Tarpit protocol=tcp psd=21,5s,10,5
add action=add-src-to-address-list address-list=v64_Blocklist_report address-list-timeout=2h chain=Tarpit
add action=tarpit chain=Tarpit in-interface-list=WANs protocol=tcp
