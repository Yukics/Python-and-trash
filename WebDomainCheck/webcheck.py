#/bin/python3

# Ejecutar en Linux!
# Useful docs:  https://www.w3schools.com/python/ref_requests_response.asp
#               https://pypi.org/project/ping3/

#Modules needed
import sys
import requests
import threading
import socket
from urllib3.exceptions import InsecureRequestWarning
try:
    from ping3 import ping
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'ping3'])
    from ping3 import ping

# Suppress warnings related to cert verify on false
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Header de petición web
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def main():

    #Check if n parameters are fine

    if len(sys.argv) > 2:

        print("Demasiados parámetros")
        sys.exit(1)

    elif len(sys.argv) < 0:

        print("Introduce algún parámetro")
        sys.exit(1)

    elif len(sys.argv) == 2:
        archivo = sys.argv[1]

    #Checks if file passed from args exists

    try:
        file = open(archivo, 'r')
        lineas = file.readlines()
    except:
        print("No se encuentra el fichero: " + archivo)
        sys.exit(1)

    threads = list()
    
    for lin in lineas:
        
        ping = threading.Thread(target=myping, args=(lin,))
        threads.append(ping)
        ping.start()

        web = threading.Thread(target=myweb, args=(lin,))
        threads.append(web)
        web.start()

        secweb = threading.Thread(target=mysecweb, args=(lin,))
        threads.append(secweb)
        secweb.start()
    
    for lin, thread in enumerate(threads):
        thread.join()

def myweb(host):
    web = ("http://www."+host).replace('\n','')

    try:       
        session = requests.Session()
        session.trust_env = False
        response = session.get(web, verify=False, headers=headers, timeout=3)
        if response.status_code == 200:
            print("OK http: " + web)
        else:
            print("ERROR http: " + response.status_code + " : " + web)
    except:
        print("ERROR http: " + web)
    
def mysecweb(host):
    web_secure = ("https://www." + host).replace('\n', '')

    try:
        session = requests.Session()
        session.trust_env = False
        response = session.get(web_secure, verify=False, headers=headers, timeout=3)
        if response.status_code == 200:
            print("OK https: " + web_secure)
        else:
            print("ERROR https: " + response.status_code + " : " + web_secure)
    except:
        print("ERROR https: " + web_secure)

def myping(host):
    host = host.replace('\n','')
    res = ping(host)

    if res:
        ip=socket.gethostbyname(host)
        print("OK ping: " + host + " -> " + ip)
    else:
        print("ERROR ping: {}".format(host))

if __name__ == '__main__':
    main()