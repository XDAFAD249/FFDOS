import time
import os

os.system('cls')
print ("FFDOS")
time.sleep(2)
print("LOADING...")
time.sleep(0.2)
RAM = "4MB"
ROM ="512MB"
print("RAM:" +RAM)
print("ROM:" +ROM)
time.sleep(2)
os.system('cls')
print("Welcome to FFDOS")
while True:
    com1 = input("C:/>")
    if com1 == "test":
        print("the test")
    if com1 == "ver":
        print("FFDOS 1.0")
    if com1 == "exit":
        os.system('cls')
        break
    if com1 == "clear":
        os.system('cls')
    if com1 == "reset":
        os.system("dos.exe")
        os.system("python dos.py")
        break
    if com1 == "dir":
        os.system("dir")
    if com1 == "help":
        print ("comands:")
        print ("help - comands             dir - view files on this dir")
        print ("reset - restart the dos    clear - clear all messege on the dos")
        print ("test - test comand         exit - exit the dos")
        print ("ver - version              credits - credits of the system")
    if com1 == "credits":
        os.system('cls')
        while False:
            com1 = input("C:/>")
        time.sleep(2)
        print ("FFDOS")
        time.sleep(2)
        print ("Coders: Artem Litvincev, Seva Tretyakov, Nikita Rojdestvin(Kernel)")
        time.sleep(2)
        print ("Creative: Artem Litvincev")
        time.sleep(2)
        print("Companies that developed:MECIS, XDAFAD Software")
        time.sleep(2)
        os.system('cls')