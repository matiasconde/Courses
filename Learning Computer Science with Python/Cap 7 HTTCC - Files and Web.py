"""
with open("Lalalang.txt","r") as myfile:
    all_lines = myfile.readlines()
    print(all_lines)
    all_lines.sort()
    print(all_lines[:])
with open("Lalalang - copia.txt","w") as mynewfile:
    for line in all_lines:
        mynewfile.write(line)

print(mynewfile)

# RECORDAR QUE LOS DIRECTORIOS EN WINDOWS VAN CON DOBLE \\ PORQUE EL \ SOLO ES UNA KEYWORD


import urllib.request as geturl

URL = "https://www.clarin.com/"

destination_ = "que loca página.txt"

geturl.urlretrieve(URL,destination_)

import urllib.request

#1
with open("C:\\Users\\Uso familiar\\Documents\\Matias\\Estudios Maty\\Matemática y Física Moderna\\fisica moderna\\fisica teorica 2\\Readme_Book-share.txt","r") as oldfile:
    contenido = oldfile.readlines()
print(len(contenido))
print(contenido[1])

with open("Readme_Book-share - alverre.txt","w") as newfile:
    loopeador = len(contenido)
    while loopeador >0:
        newfile.write(contenido[loopeador-1])
        loopeador -= 1

print(newfile)

#2
with open("Lalalang.txt","r") as the_file, open("Lalalang con SNAKE.txt","w") as new_file:
    content = the_file.readlines()
    for line in content:
        if "snake" in line:
            new_file.write(line)

print(new_file)


#3
with open("test_file.txt","r") as test_file, open("test_file_numbered.txt","w") as new_file:
    all_lines = test_file.readlines()
    for i,line in enumerate(all_lines):
        new_file.write("{0:>4} ".format(i)+line)

#3 BIS
import copy
with open("test_file.txt","r") as test_file, open("test_file_numbered.txt","w") as new_file:
    all_lines = test_file.readlines()
    new_lines = copy.deepcopy(all_lines)
    for i,line in enumerate(new_lines):
        new_file.write("{0:>4} ".format(i) + line)


#4
with open("test_file_numbered.txt", "r") as test_file, open("test_file_unnumbered.txt", "w") as new_file:
    all_lines = test_file.readlines()
    for i,line in enumerate(all_lines):
        new_file.write(line[5:])

#4 BIS
with open("test_file_numbered.txt", "r") as test_file, open("test_file_unnumberedBIS.txt", "w") as new_file:
    all_lines = test_file.readlines()
    for i,line in enumerate(all_lines):
        cont = 0
        while True:
            if line[cont] in " 0123456789":
                cont += 1
            else:
                print(cont)
                break
        new_file.write(line[cont:])

#5
dictionary_for_1337sp34k = {" ":" ","4":"a","8":"b","(":"c","[)":"d","3":"e","]]=":"f","&":"g","#":"h","!":"i",".l":"j","]{":"k","1":"l","|\/|":"m","|\|":"n","()":"o","[]D":"p","(,)":"q","1²":"r","5":"s","']'":"t","(_)":"u","\/":"v","\/\/":"w","%":"x","'/":"y",'"/_':"z"}
dictionary_to_1337sp34k = {" ":" ","a":"4","b":"8","c":"(","d":"[)","e":"3","f":"]]=","g":"&","h":"#","i":"!","j":".l","k":"]{","l":"1","m":"|\/|","n":"|\|","o":"()","p":"[]D","q":"(,)","r":"1²","s":"5","t":"']'","u":"(_)","v":"\/","w":"\/\/","x":"%","y":"'/","z":'"/_'}

print(dictionary_for_1337sp34k)
print(dictionary_to_1337sp34k)

with open("file_to_traduct.txt","r") as test_file, open("file_traducted.txt","w") as file_traducted:
    all_file1 = test_file.read()
    all_file = all_file1.lower()

    new_string = ""
    for letter in all_file:
        if letter in dictionary_to_1337sp34k.keys():

            new_string += dictionary_to_1337sp34k[letter]
    file_traducted.write(new_string)

"""
