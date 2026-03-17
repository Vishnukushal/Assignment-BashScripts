Network Scanning Automation Tools

this project is used to automate network scanning which is useful during network network Reconnaissance

Tools Used

- Python 3.13
- Nmap
- Linux Networking Commands (ping, arp)

Installation

Install Nmap 

sudo apt update
sudo apt install nmap

Install net-tools (for arp)

sudo apt install net-tools

We can run the  Programs using

Ping Scanner

python3 ping_scanner.py

Enter hostname or IP (Example: 127.190.35.16)

ARP Scanner

python3 arp_scanner.py

Displays IP-MAC mappings from ARP table.

Nmap Scanner

python3 nmap_scanner.py

Enter target and select scan type.

Example Targets

- 127.168.59.12
- Router IP (example: 192.168.1.1)
- scanme.nmap.org

## Bonus Feature

Unified Network Scanner (network_scanner.py) combines Ping, ARP and Nmap scanners into a single menu-driven tool.

## Screenshots

### Ping Scanner Output
![Ping Output](screenshots/ping_output.png)

### ARP Scanner Output
![ARP Output](screenshots/arp_output.png)

### Nmap Scanner Output
![Nmap Output](screenshots/nmap_output.png)

### Unified Scanner Output
![Unified Tool](screenshots/unified_tool.png)
