README (English)
# Network Attack Tool

A Python script for testing Payload and Slowloris attacks with support for Proxy and Tor.

## Features

- Payload attack with customizable size and message  
- Slowloris attack support  
- Works with Proxy and Tor  
- Random User-Agent support  
- Configurable threads and sockets  

## Usage

```
python main.py [options]
Options
Option	Description
-h, --help	Show help menu
--ip <IP>	Target IP address
-p, --port <PORT>	Target port (default: 80)
-ths, --threads <N>	Number of threads (default: 100)
-num-socks, -n-socks	Number of Socks (default: 1000)
-ra, --random-agent	Use random User-Agent

Payload Mode (works with Tor & Proxy)
Option	Description
-payloada, --payload-attack	Send a JSON payload to server
--set-size-payload, -set-p	Set payload size (default 51200)
--set-msg-payload	Set custom payload message
--random-payload	Use randomized numeric payload

Slowloris Mode (works with Tor & Proxy)
Option	Description
-slowa, --slowloris-attack	Perform Slowloris attack

Tor & Proxy (usable with Payload and Slowloris)
Tor
Option	Description
--tor-ip	Set Tor proxy IP
--tor-port	Set Tor proxy port
-c-tor-ip, --change-tor-ip	Change Tor IP during attack

Proxy
Option	Description
--proxy-ip <IP>	Set Proxy IP
--proxy-port <PORT>	Set Proxy Port
```
## Examples
```
Payload attack 100KB via Tor:
python ddos.py --ip 1.2.3.4 -p 80 -payloada --set-size-payload 102400 --tor-ip 127.0.0.1 --tor-port 9050

Slowloris attack via Proxy:
python ddos.py --ip 1.2.3.4 -p 80 -slowa --proxy-ip 192.168.1.10 --proxy-port 1080
```
## Warning
Use only for testing and educational purposes.
