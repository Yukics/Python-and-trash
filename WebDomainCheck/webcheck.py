#/bin/python3

import sys
import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress warnings related to cert verify on false
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

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
