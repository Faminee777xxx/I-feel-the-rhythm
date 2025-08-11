# Attack Tool - Usage and Options

## English Version

### Options and What They Do:

| Option                         | Description                                   | Default        |
|--------------------------------|-----------------------------------------------|----------------|
| `-h`, `--help`                 | Show this help menu                           |                |
| `--ip <IP>`                   | Target IP address                            |                |
| `-p`, `--port <PORT>`          | Target Port                                  | 80             |
| `-ths`, `--threads <N>`        | Number of threads                            | 100            |
| `-num-socks`, `-n-socks`       | Number of Socks proxies                       | 1000           |
| `-ra`, `--random-agent`        | Use random User-Agent header                  | Off            |

---

### Mode: Payload (Can use with Tor & Proxy)

| Option                         | Description                                   | Default        |
|--------------------------------|-----------------------------------------------|----------------|
| `-payloada`, `--payload-attack` | Send a JSON payload file to the server       |                |
| `--set-size-payload`, `-set-p`  | Set size of payload in bytes                   | 51200 (50 KB)  |
| `--set-msg-payload`             | Set custom message as payload                  |                |
| `--random-payload`              | Use randomized payload data (number-based)    |                |

---

### Mode: Slowloris (Can use with Tor & Proxy)

| Option                         | Description                                   |                |
|--------------------------------|-----------------------------------------------|----------------|
| `-slowa`, `--slowloris-attack` | Perform Slowloris attack                       |                |

---

### Mode: Tor & Proxy (Can use with Slowloris and Payload Modes)

#### TOR

| Option                         | Description                                   |                |
|--------------------------------|-----------------------------------------------|----------------|
| `--tor-ip`                     | TOR IP address to use                         |                |
| `--tor-port`                   | TOR port to use                              |                |
| `--change-tor-ip`, `-c-tor-ip` | Change TOR IP during attack                    |                |

#### Proxy

| Option                         | Description                                   |                |
|--------------------------------|-----------------------------------------------|----------------|
| `--proxy-ip <IP>`              | Proxy IP address to use                       |                |
| `--proxy-port <PORT>`          | Proxy port to use                            |                |
| `--proxy-lists <proxy_lists.txt>` | Use multiple proxies from a list file       |                |
| `--check-proxy-list`           | Check proxies in the proxy list file          |                |

---

## เวอร์ชันภาษาไทย (Thai Version)

### ตัวเลือกและคำอธิบาย:

| ตัวเลือก                      | คำอธิบาย                                    | ค่าเริ่มต้น     |
|-------------------------------|---------------------------------------------|-----------------|
| `-h`, `--help`                | แสดงเมนูช่วยเหลือ                          |                 |
| `--ip <IP>`                  | กำหนด IP เป้าหมาย                          |                 |
| `-p`, `--port <PORT>`         | กำหนดพอร์ตเป้าหมาย                         | 80              |
| `-ths`, `--threads <N>`       | จำนวนเธรดที่ใช้                             | 100             |
| `-num-socks`, `-n-socks`      | จำนวน SOCKS proxy ที่ใช้                     | 1000            |
| `-ra`, `--random-agent`       | ใช้ User-Agent แบบสุ่ม                      | ปิดใช้งาน       |

---

### โหมด Payload (ใช้ร่วมกับ Tor และ Proxy ได้)

| ตัวเลือก                      | คำอธิบาย                                    | ค่าเริ่มต้น     |
|-------------------------------|---------------------------------------------|-----------------|
| `-payloada`, `--payload-attack` | ส่งไฟล์ JSON เป็น payload ไปยังเซิร์ฟเวอร์   |                 |
| `--set-size-payload`, `-set-p`  | กำหนดขนาด payload (หน่วยไบต์)               | 51200 (50 KB)   |
| `--set-msg-payload`            | กำหนดข้อความสำหรับ payload                   |                 |
| `--random-payload`             | ใช้ payload แบบสุ่ม (ตัวเลข)                 |                 |

---

### โหมด Slowloris (ใช้ร่วมกับ Tor และ Proxy ได้)

| ตัวเลือก                      | คำอธิบาย                                    |                 |
|-------------------------------|---------------------------------------------|-----------------|
| `-slowa`, `--slowloris-attack` | ทำการโจมตีแบบ Slowloris                     |                 |

---

### โหมด Tor & Proxy (ใช้ร่วมกับ Slowloris และ Payload ได้)

#### TOR

| ตัวเลือก                      | คำอธิบาย                                    |                 |
|-------------------------------|---------------------------------------------|-----------------|
| `--tor-ip`                    | กำหนด IP ของ Tor ที่จะใช้                    |                 |
| `--tor-port`                  | กำหนดพอร์ตของ Tor                            |                 |
| `--change-tor-ip`, `-c-tor-ip` | เปลี่ยน IP ของ Tor ระหว่างการโจมตี            |                 |

#### Proxy

| ตัวเลือก                      | คำอธิบาย                                    |                 |
|-------------------------------|---------------------------------------------|-----------------|
| `--proxy-ip <IP>`             | กำหนด IP ของ Proxy ที่จะใช้                   |                 |
| `--proxy-port <PORT>`         | กำหนดพอร์ตของ Proxy                          |                 |
| `--proxy-lists <proxy_lists.txt>` | ใช้ Proxy หลายตัวจากไฟล์รายชื่อ                |                 |
| `--check-proxy-list`          | ตรวจสอบ Proxy ที่อยู่ในไฟล์รายชื่อ              |                 |

---

### Notes:

- Always use this tool responsibly and with permission.  
- Unauthorized attacks are illegal in many countries.

---
# Old read me V.3
> https://github.com/Faminee777xxx/I-feel-the-rhythm/blob/main/README.md


![Chainsaw Man](https://static.wikia.nocookie.net/chainsaw-man/images/e/e4/Volume_14_%28Textless%29.png/revision/latest/scale-to-width-down/1000?cb=20250505195335)

> **Image credit:**  
> Source: [Chainsaw Man Wiki](https://chainsawman.fandom.com)  
> Artist: Fujimoto Tatsuki

