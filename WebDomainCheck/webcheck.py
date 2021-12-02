#/bin/python3

# Ejecutar en Linux!
# Useful docs: https://www.w3schools.com/python/ref_requests_response.asp

import sys
import requests
import os
import subprocess
from urllib3.exceptions import InsecureRequestWarning

# Suppress warnings related to cert verify on false
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def main():
    #Check if n parameters are fine
    if len(sys.argv) >2:
        print("Demasiados parámetros")
        sys.exit(1)
    elif len(sys.argv) < 0:
        print("Introduce algún parámetro")
        sys.exit(1)
    elif len(sys.argv) == 2:
        fichero = sys.argv[1]

    #Checks if file passed from args exists
    try:
        file = open(fichero, 'r')
        lineas = file.readlines()
    except:
        print("No se encuentra el fichero: " + fichero)
        sys.exit(1)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    #Checks every domain response status code if 200 ok something else error
    for lin in lineas:

        #Lanza un ping
        ping = myping(lin)

        #En caso de que el ping responda hace la comprobación web
        if ping == 0:
            print("Ping OK: " + lin)
            web = ("http://"+lin).replace('\n','')
            web_secure = ("https://" + lin).replace('\n', '')

            try:       
                session = requests.Session()
                session.trust_env = False
                response = session.get(web, verify=False, headers=headers)
                if response.status_code == 200:
                    print(web + ": OK")
                else:
                    print(web + "Error: " + response.status_code)
            except:
                print("Error Tocho! Probablemente no exista " + web)

            try:
                session = requests.Session()
                session.trust_env = False
                response = session.get(web_secure, verify=False, headers=headers)
                if response.status_code == 200:
                    print(web_secure + ": OK")
                else:
                    print(web_secure + "Error: " + response.status_code)
            except:
                print("Error Tocho! Probablemente no exista " + web_secure)
        #En caso de que no conteste o nos de otro tipo de error mostramos esto
        else:
            print(lin + "No contesta el ping")

    
def myping(host):
    p = subprocess.Popen(["ping", "-q", "-c", "1", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response = p.wait()
    if response==0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()