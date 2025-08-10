# README (English)
# Network Attack Tool (Dos)

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
Option	                      Description
-payloada, --payload-attack	  Send a JSON payload to server
--set-size-payload, -set-p	  Set payload size (default 51200)
--set-msg-payload	            Set custom   payload message
--random-payload	            Use randomized numeric payload

Slowloris Mode (works with Tor & Proxy)
Option	                    Description
-slowa, --slowloris-attack	Perform Slowloris attack

Tor & Proxy (usable with Payload and Slowloris)
Tor
Option	                    Description
--tor-ip	                  Set Tor proxy IP
--tor-port	                Set Tor proxy port
-c-tor-ip, --change-tor-ip	Change Tor IP during attack

Proxy
Option	            Description
--proxy-ip <IP>	    Set Proxy IP
--proxy-port <PORT>	Set Proxy Port
```
## Examples
```
Payload attack 100KB via Tor:
python main.py --ip 1.2.3.4 -p 80 -payloada --set-size-payload 102400 --tor-ip 127.0.0.1 --tor-port 9050

Slowloris attack via Proxy:
python main.py --ip 1.2.3.4 -p 80 -slowa --proxy-ip 192.168.1.10 --proxy-port 1080
```
## Warning
Use only for testing and educational purposes.


---

# README (ภาษาไทย)
# เครื่องมือโจมตีเครือข่าย (Dos)

สคริปต์ Python สำหรับทดสอบการโจมตีแบบ Payload และ Slowloris โดยรองรับ Proxy และ Tor

## ฟีเจอร์หลัก

- โจมตีแบบ Payload ปรับขนาดและข้อความได้  
- รองรับการโจมตีแบบ Slowloris  
- ใช้งานร่วมกับ Proxy และ Tor ได้  
- เลือก User-Agent แบบสุ่ม  
- กำหนดจำนวน Threads และ Sockets ได้  

## วิธีใช้

```
python main.py [options]
Options
ตัวเลือก	                  คำอธิบาย
-h, --help	            แสดงเมนูช่วยเหลือ
--ip <IP>	              กำหนด IP เป้าหมาย
-p, --port <PORT>	      กำหนดพอร์ตเป้าหมาย (ค่าเริ่มต้น 80)
-ths, --threads <N>	    จำนวน Threads (ค่าเริ่มต้น 100)
-num-socks, -n-socks	  จำนวน Socks (ค่าเริ่มต้น 1000)
-ra, --random-agent	    ใช้ User-Agent แบบสุ่ม

โหมด Payload (ใช้ร่วมกับ Tor & Proxy ได้)
ตัวเลือก	                      คำอธิบาย
-payloada, --payload-attack	ส่ง JSON Payload ไปยังเซิร์ฟเวอร์
--set-size-payload, -set-p	กำหนดขนาด Payload (ค่าเริ่มต้น 51200)
--set-msg-payload	          กำหนดข้อความใน Payload
--random-payload	          ใช้ Payload แบบสุ่มตัวเลข

โหมด Slowloris (ใช้ร่วมกับ Tor & Proxy ได้)
ตัวเลือก	                      คำอธิบาย
-slowa, --slowloris-attack	เริ่มโจมตีแบบ Slowloris

โหมด Tor & Proxy (ใช้ร่วมกับ Slowloris และ Payload)
Tor
ตัวเลือก	    คำอธิบาย
--tor-ip	กำหนด IP ของ Tor Proxy
--tor-port	กำหนด Port ของ Tor Proxy
-c-tor-ip, --change-tor-ip	เปลี่ยน IP Tor ระหว่างโจมตี

Proxy
ตัวเลือก	          คำอธิบาย
--proxy-ip <IP>	กำหนด IP ของ Proxy
--proxy-port <PORT>	กำหนด Port ของ Proxy
```
## ตัวอย่าง
```
โจมตี Payload 100KB ผ่าน Tor:
python main.py --ip 1.2.3.4 -p 80 -payloada --set-size-payload 102400 --tor-ip 127.0.0.1 --tor-port 9050

โจมตี Slowloris ผ่าน Proxy:
python main.py --ip 1.2.3.4 -p 80 -slowa --proxy-ip 192.168.1.10 --proxy-port 1080
```
## คำเตือน
ใช้เพื่อการทดสอบและศึกษาเท่านั้น
การโจมตีโดยไม่ได้รับอนุญาตอาจผิดกฎหมายและมีโทษตามกฎหมาย

![Chainsaw Man](https://static.wikia.nocookie.net/chainsaw-man/images/e/e4/Volume_14_%28Textless%29.png/revision/latest/scale-to-width-down/1000?cb=20250505195335)

> **Image credit:**  
> Source: [Chainsaw Man Wiki](https://chainsawman.fandom.com)  
> Artist: Fujimoto Tatsuki

