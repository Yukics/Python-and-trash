import json
import urllib.parse
import urllib.request
import os
import time

def main():
    # python 3.6

    url = 'AQUI URL WEBHOOK'
    while True:
        time.sleep(1)
        with open("hosts", "r") as hosts:        
            for single_host in hosts:
                ip=single_host.split(":")[1]
                hostname=single_host.split(":")[0]

                if ping(ip) == True:
                    print ('No problemos')
                else:
                    message=hostname+' está caido\n'+ip

                    bot_message = {'text': message}
                    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

                    byte_encoded = json.dumps(bot_message).encode('utf-8')
                    req = urllib.request.Request(url=url, data=byte_encoded, headers=message_headers)
                    response = urllib.request.urlopen(req)

                    print(response.read())


def ping(host):
    
    response = os.system("ping -c 1 " + host+ " > /dev/null")

    if response == 0:
        return True
    else:
        return False

def habia_muerto(ip):


if __name__ == '__main__':
    main()

    