from urllib.parse import urlparse
import requests
import socket
import threading
import pyfiglet
from colorama import Fore, Back, Style
import timeit

banner = pyfiglet.figlet_format("PyPortScanner")
print(banner)
print(Fore.RED + "Disclaimer: Usage of this tool for attacking targets without prior consent is illegal. It is user's responsibility to obey laws and developer is not responsible for misuse or damaged caused by this project!")
print(Style.RESET_ALL)
counter = 0

full_url = input("Enter target url: ")
target = urlparse(full_url).netloc

print("->Target: " + target)

r = requests.head(full_url)
status = r.status_code
if status == 200:
  print("[INFO] Target Online")
else:
  print("[INFO] Target Offline")
  exit()

start_time = timeit.default_timer()
def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect((target,port))
        print(port,"is open")
        con.close()
    except: 
        pass
r = 1 
for x in range(1,1024): 

    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start() 
time_taken = timeit.default_timer() - start_time
time  = "{:.2f}".format(time_taken)
print(Back.WHITE + Fore.BLACK + "Completed the scan in ", time + Style.RESET_ALL)