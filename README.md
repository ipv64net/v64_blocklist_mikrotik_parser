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
