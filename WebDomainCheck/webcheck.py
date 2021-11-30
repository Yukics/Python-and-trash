#/bin/python3

import sys
import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress warnings related to cert verify on false
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Check if n parameters are fine
if len(sys.argv) >2:
    print("Demasiados parámetros")
    exit
elif len(sys.argv) < 0:
    print("Introduce algún parámetro")
    exit
elif len(sys.argv) == 2:
    fichero = sys.argv[1]

#Checks if file passed from args exists
try:
    file = open(fichero, 'r')
    lineas = file.readlines()
except:
    print("No se encuentra el fichero: " + fichero)
    sys.exit(1)

#Checks every domain response status code if 200 ok something else error
for lin in lineas:
    web = ("http://"+lin).replace('\n','')
    web_secure = ("https://" + lin).replace('\n', '')

    try:
        response = requests.get(web, verify=False)
        if response.status_code == 200:
            print(web + ": OK")
        else:
            print(web + "Error: " + response.status_code)
    except:
        print("Error Tocho! Probablemente no exista " + web)

    try:
        response = requests.get(web_secure, verify=False)
        if response.status_code == 200:
            print(web_secure + ": OK")
        else:
            print(web_secure + "Error: " + response.status_code)
    except:
        print("Error Tocho! Probablemente no exista " + web_secure)
        