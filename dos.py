import time
import os

os.system('cls')
print ("FFBIOS")
time.sleep(2)
print("BOOT OS FOUND")
time.sleep(0.2)
RAM = "4MB"
time.sleep(0.2)
ROM ="512MB"
print("RAM:" +RAM)
print("ROM:" +ROM)
time.sleep(0.7)
os.system('cls')
print ("BOOTING OS.")
time.sleep(0.5)
os.system('cls')
print ("BOOTING OS..")
time.sleep(0.6)
os.system('cls')
print ("BOOTING OS...")
time.sleep(2)
os.system('cls')
print ("BOOTING OS....")
time.sleep(4)
os.system('cls')
print ("BOOTING OS.....")
time.sleep(0.8)
os.system('cls')
print ("BOOTING OS......")
time.sleep(0.7)
os.system('cls')
print("Welcome to FFDOS FOR WINDOWS")
time.sleep(2)
os.system("cls")
print ("LOADING CONSOLE...")
time.sleep(0.3)
os.system("cls")

while True:
    com1 = input("ffdos@system:>")
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
        print ("license - BSD V3")
    if com1 == "credits":
        os.system('cls')
        while False:
            com1 = input("ffdos@root:>")
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
    if com1 == "license":
        os.system("LICENSE.txt")
