# v64_blocklist_mikrotik_parser
These Script Read die Mikrotik Firewall IP Address List and sent it to v64_Blocklist.

# Crontab
*/15 * * * * cd /root/v64_blocklist_mikrotik_parser && /usr/bin/python3 v64_blocklist_mikrotik_parser.py
