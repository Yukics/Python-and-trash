#Devuelve el tip_claseo de clase de la ip_clase
def Definir_Clase(ip_clase):
    ip_clase = str(ip_clase)
    posicion_clase = 0
    digito_clase = ip_clase[posicion_clase]
    while digito_clase != ".":
        posicion_clase += 1
        digito_clase = ip_clase[posicion_clase]
    primer_octeto = int(ip_clase[0:posicion_clase])
    if primer_octeto>255:
        clase = 0
    elif primer_octeto < 128:
        clase = 1
    elif primer_octeto < 192:
        clase = 2
    elif primer_octeto < 224:
        clase = 3
    return clase
#Función para pasar de decimal a binario
def conversor_decimal_a_binario(numero_binario):
    numero_binario = format(int(numero_binario), '08b')
    return numero_binario
#Funcion que convierte cualquier numero a decimal
def bin_a_dec(x):
    return int(x, 2)
#Convierte IP en Binario a IP en decimal
def conversor_binario_a_decimal(ip_binario):
    ip_decimal = str(int(ip_binario[0:8],2))+"."+str(int(ip_binario[8:16],2))+"."+str(int(ip_binario[16:24],2))+"."+str(int(ip_binario[24:32],2))
    return ip_decimal
#Funcion que combierte un numero decimal a una IP
def conversor_decimal_ip(ip_decimal):
    ip_binario = conversor_decimal_a_binario(ip_decimal)
    ip = str(int(ip_binario[0:8], 2)) + "." + str(int(ip_binario[8:16], 2)) + "." + str(int(ip_binario[16:24], 2)) + "." + str(int(ip_binario[24:32], 2))
    return ip
#Comprueba si se introducen IP posibles(con la funcion esunaip)
def introduccion_error_ip(ip):
    if esunaip(ip)==0:
        print("\nAhora vas y la cascas, vuelta a empezar, mete una IP mono espasmodico con pistola\n")
        main()
    else:
        return ip
#Comprueba si se introducen numeros posibles
def introduccion_error_redes_o_hosts(nredes):
    if nredes.isdecimal() == True:
        return nredes
    else:
        print("\nCasi cruck, esperate sentado\n")
        main()
#Introduccion de datos de la 1a selección
def Introduccion_de_datos():
    ip_introduccion_datos_1 = introduccion_error_ip(input("Dame una IP:"))
    nredes = int(introduccion_error_redes_o_hosts(input("Dame el numero de redes que necesitas:")))
    return ip_introduccion_datos_1, nredes
#Introducción de datos de la IP y hosts por red del VLSM
def Introduccion_vlsm():
    ip = introduccion_error_ip(input("Dame una IP:"))
    numero = 1
    lista_host = []
    while numero > 0:
        nhosts = input("Digame cuantos hosts tiene la red " + str(numero)+":")
        if nhosts.isdigit() == True and int(nhosts) > 0:
            lista_host.append(str(int(nhosts)+2))
            numero += 1
        else:
            print("\nNo has introducido nada o has introducido un valor erroneo\n")
            numero = 0
    print("Estas son las IP necesarias por red: ", lista_host, "\nApareceran de mayor a menor en los rangos\n")
    return ip, lista_host
#Comprueba si es una IP que existe
#Nota hacer la IP en binario y mirar si son 32 bits
def esunaip(ip):
    ip = ip + "."
    contar_puntos = ip.count(".")
    if contar_puntos != 4:
        print("ME CAGO EN TUS MUERTOS DANI X2, QUE METAS UNA IP")
        return 0
    final = 0
    principio = 0
    ip_bin = ""
    if ip[0:len(ip)-1].isdigit()==True:
        print("ME CAGO EN TUS MUERTOS DANI, NO PONGAS NUMEROS SOLOS")
        return 0
    else:
        for i in range(contar_puntos):
            letra = ""
            while letra != ".":
                final += 1
                letra = ip[final]
            octeto = ip[principio:final]
            if octeto.isnumeric()==False:
                return 0
            aux = final
            principio = aux+1
            ip_bin = ip_bin + str(conversor_decimal_a_binario(octeto))
            if int(octeto) < 0 or int(octeto) > 255:
                return 0
        if len(ip_bin) == 32:
            return 1
        else:
            return 0
#Funcion de control de errores, ej mas hosts o redes de las permitidas
def errores(nredes, clase):
    if clase == 0:
        print("\nNo existen IPs cuyo octeto sea mayor de 8 bits\n\n")
        main()
    elif clase == 1 and nredes > 8388608:
        print("\nNo pueden haber tantas redes en una IP de Clase A\n\n")
        main()
    elif clase == 2 and nredes > 32768:
        print("\nNo pueden haber tantas redes en una IP de Clase B\n\n")
        main()
    elif clase == 3 and nredes > 128:
        print("\nNo pueden haber tantas redes en una IP de Clase C\n\n")
        main()
#Funcion de control de errores si se introducen mas hosts de los permitidos
def errores_vlsm(clase, total_host):
    if len(total_host) <= 1:
        print("Debes introducir mas de un host")
        main()
    hosts = sum(total_host)
    if clase == 1 and int(hosts) > 16777216:
        print("No pueden haber tantos hosts en una IP de Clase A\n\n")
        main()
    elif clase == 2 and int(hosts) > 65536:
        print("No pueden haber tantos hosts en una IP de Clase B\n\n")
        main()
    elif clase == 3 and int(hosts) > 256:
        print("No pueden haber tantos hosts en una IP de Clase C\n\n")
        main()
#Extrae la mascara de subred a partir del nredes necesario y su clase
def Mascara(clase, nredes):
    base_2 = 2
    potencia = 0
    mascaracidr_binario = ""
    nredes = int(nredes)
    while base_2**potencia <= nredes:
        potencia += 1
    mascaracidr = (clase*8) + potencia
    mascaracidr_binario = mascaracidr_binario + ("1" * mascaracidr) + ("0" * (32-mascaracidr))
    mascara = str(int(mascaracidr_binario[0:8], 2))+"."+str(int(mascaracidr_binario[8:16], 2))+"."+str(int(mascaracidr_binario[16:24], 2))+"."+str(int(mascaracidr_binario[24:32], 2))
    return mascara, mascaracidr
#Devuelve el nº de redes a partir de la clase y del nº de hosts
def sacarnredes(clase, hosts):
    hosts += 2
    bits_hosts = 1
    bits_mascara_de_subred = 0
    while hosts > 1:
        hosts //= 2
        bits_hosts += 1
    if clase == 1:
        bits_mascara_de_subred = 24
    elif clase == 2:
        bits_mascara_de_subred = 16
    elif clase == 3:
        bits_mascara_de_subred = 8
    nredes = bits_mascara_de_subred - bits_hosts
    nredes = 2 ** nredes
    return nredes
#Devuelve una lista con las IP necesarias por red a partir del numero de hosts
def contar_hosts_vlsm(lista_host):
    lista_host_redondeada = []
    for i in range(len(lista_host)):
        potencia = 1
        numero = 0
        while numero < int(lista_host[i]):
            numero = 2 ** potencia
            potencia += 1
        lista_host_redondeada.append(numero)
    return lista_host_redondeada
#Poner los numeros de la IP en una lista
def lista_con_numeros_ip(ip_limpia):
    ip_enteros = []
    inic = 0
    fina = 0
    mierda = ""
    contador = 0
    contador_octeto = 0
    ip_limpia = ip_limpia + "."
    while contador_octeto < 4:
        while mierda != ".":
            mierda = ip_limpia[contador]
            contador += 1
            fina += 1
        ip_enteros.append(ip_limpia[inic:fina-1])
        contador_octeto += 1
        mierda = ""
        fina += 1
        inic = fina-1
        contador += 1
    return ip_enteros
#Funcion de impresión de rangos y mascaras
def vlsm(ip, clase, lista_host):
    #Devuelve la IP con 0 dependiendo de la clase
    ip_limpia = sacar_rango_suma(ip, clase)
    #Devuelve la lista con los host redondeados a la potencia de dos mas cercana por arriba en lista
    lista_host = contar_hosts_vlsm(lista_host)
    ip_binario = ""
    ip_enteros = lista_con_numeros_ip(ip_limpia)
    #Ordena la lista con los host redondeados
    lista_host.sort(reverse=True)
    #Convierte la IP a formato binario de 32b
    for i in range(len(ip_enteros)):
        ip_binario = ip_binario + str(conversor_decimal_a_binario(ip_enteros[i]))
    #Bucle para presentar rangos y mascara de subred
    posicion = 0
    numero = 1
    while posicion < len(lista_host):
        host_suma = lista_host[posicion]
        ip_sumada = int(bin_a_dec(ip_binario)) + int(host_suma) - 1
        ip_inicio = conversor_decimal_ip(bin_a_dec(ip_binario))
        ip_final = conversor_decimal_ip(ip_sumada)
        mascara, mascaracidr = Mascara(clase, sacarnredes(clase, lista_host[posicion]))
        print("Los rangos de la red", numero, "van de: ", ip_inicio, " - ", ip_final, " /",mascaracidr, " o ", mascara)
        ip_enteros = lista_con_numeros_ip(ip_final)
        ip_sumada=""
        for i in range(len(ip_enteros)):
            ip_sumada = ip_sumada + str(conversor_decimal_a_binario(int(ip_enteros[i])))
        ip_binario = conversor_decimal_a_binario(bin_a_dec(ip_sumada) + 1)
        numero += 1
        posicion += 1
#Devuelve la IP sin los digitos que sobran segun la clase
def sacar_rango_suma(ip, tipo_clase):
    end = 0
    start = 0
    digito = ""
    for i in range(tipo_clase):
        letra = ""
        while letra != ".":
            end += 1
            letra = str(ip[end])
    numero = ip[start:end]
    digito = digito + str(numero) + "."
    if tipo_clase == 1:
        ip = digito + "0.0.0"
        return ip
    elif tipo_clase == 2:
        ip = digito + "0.0"
        return ip
    elif tipo_clase == 3:
        ip = digito + "0"
        return ip
#Funcion de estructura principal con metodo de selección
def main():
    eleccion = 0
    while eleccion != 4:
        print("\nElige que quieres hacer:")
        print("         1. Sacar mascara de Subred a partir de IP y numeros de redes necesaria.")
        print("         2. Sacar mascara de Subred a partir de IP y numeros de host por red.")
        print("         3. VLSM Mascara de red de longitud variable y sus rangos.")
        print("         4. Salir.")
        eleccion = input()
        if eleccion.isdigit()==True:
            eleccion = int(eleccion)
            if eleccion > 4 or eleccion < 1:
                print("Veo que no sabes ni leer simio nazi")
            if eleccion == 1:
                ip, nredes = Introduccion_de_datos()
                clase = Definir_Clase(ip)
                errores(nredes, clase)
                mascara, mascaracidr = Mascara(clase, nredes-1)
                print("\nEsta es la máscara de subred necesaria: " + str(mascara) + ", o en notación CIDR: /" + str(mascaracidr)+"\n")
            if eleccion == 2:
                ip, hosts = Introduccion_de_datos()
                clase = Definir_Clase(ip)
                nredes = sacarnredes(clase, hosts)
                errores(nredes, clase)
                mascara, mascaracidr = Mascara(clase, nredes)
                print("\nEsta es la máscara de subred necesaria: " + str(mascara) + ", o en notación CIDR: /" + str(mascaracidr)+"\n")
            if eleccion == 3:
                ip, lista_host = Introduccion_vlsm()
                clase = Definir_Clase(ip)
                lista_host = contar_hosts_vlsm(lista_host)
                errores_vlsm(clase, lista_host)
                vlsm(ip, clase, lista_host)
    quit()
main()





