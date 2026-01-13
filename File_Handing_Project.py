from pathlib import Path #read path from sys
import os

def ReadallFiles():
    p = Path('.')
    items = list(p.rglob("*")) #it will search through all subdirectories of the given path.
    for i ,items in enumerate(items): #when we print index or values we use enumerate
        print(f"Item {i} : {items}")

def Createfile():
    name = input("Enter a File name : ")
    p = Path(name)
    if p.exists() or p.is_file():
        print("File is Already Exists")
    else:
        create = open(name,"x")
        print("File Created")

def Writefile():
    name  = input("Enter a File name : ")
    p = Path(name)
    if p.exists() or p.is_file():
        write = open(name,"w")
        content = input("Enter content : ")
        write.write(content)
        write.close()

def Readfile():
    name = input("Enter a File name : ")
    p = Path(name)
    if p.exists() or p.is_file():
        read = open(name ,"r")
        read.read()
    else:
        print("File Not Found or First create file ")

def Overwritefile():
    name = input("Enter a file name : ")
    p = Path(name)
    if p.exists() or p.is_file():
        write = open(name,"a")
        content = input("Enter content : ")
        write.write(content)
        write.close()
    else:
        print("File Not Found or First create file")

def Deletefile():
    ReadallFiles()
    name = input("Enter a file name : ")
    p =Path(name)
    if p.exists() or p.is_file():
        os.remove(name)




def filehanding():
    print("-----------------WELCOME-----------------")
    print("-----------------------------------------")
    print("Press 0 : To Display All Files")
    print("Press 1 : To Create a New File ")
    print("Press 2 : To Write in Existing file  ")
    print("Press 3 : To Read the File")
    print("Press 4 : To OverWrite the File")
    print("Press 5 : To Delete the File")
    print("Press 6 : To Exit")
    print("------------------------------------------")
    Choice = int(input(f"\n"+"Enter Choice : "))


    if Choice == 0 :
        ReadallFiles()
    elif Choice == 1 :
        Createfile()
    elif Choice == 2 :
        Writefile()
    elif Choice == 3 :
        Readfile()
    elif Choice == 4 :
        Overwritefile()
    elif Choice == 5 :
        Deletefile()
    elif Choice == 6 :
        exit()

filehanding()

while True:
    ans = input("\n"+"Do you want to continue? (y/n) : ")
    if ans == "y" or ans == "Y" or ans == "yes" or ans == "Yes":
        filehanding()
    else:
        exit()
