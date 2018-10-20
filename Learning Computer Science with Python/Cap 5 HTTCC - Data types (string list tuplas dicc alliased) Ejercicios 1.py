
"""

import string

#function find

a = str(input("ingrese texto donde está la URL: ",))

def extract_URL(text):
    i = text.find("https://")
    url = ""
    for index,value in enumerate(text):
        if i<=index:
            if index != "":
                url +=text[index]
    return url

print(extract_URL(a))

# probar con sadsadddddddsd sdadasdasd a dasdasd https://www.google.com.ar/search?q=sueldo+decano+utn&oq=sueldo+decano+utn&aqs=chrome..69i57.2191j0j7&sourceid=chrome&ie=UTF-8 .

b = str(input("ingrese texto con <...>: ",))

def extract_(text):
    i = text.find("<")
    j = text.find(">")
    extraction = ""
    for index, value in enumerate(text):
        if i < index < j:
            extraction += text[index]
    return extraction

print(extract_(b))

#probar con dasdasdsjonjsdoncpjm<wally>asdopfmpcdskmcsdñcmsdñlcsdasdcssdcsd


import string

a="jklmnopq"
suffix = "ack"

for index,p in enumerate(a):
    a=a.upper()
    if p != "q":
        print(a[index]+suffix)
    else:
        print(a[index]+"u"+suffix)



import string

letter = "sadsssadsd {0} asdsadasdasds, adasds{1}"

print(letter.format("AAA","BBB"))

PI = "Pi hasta 3 decimales es {0:.20f}"  #MIRÁ ESTO MATY, .3f es .3float

import math

print(PI.format(math.pi+0.2222222222222222222222222222222222222222222222222222222222222222))

print(math.pi)

print("|||| {0:>20} |||{1:^7} || {2:<30} ".format("AAA","BBB","CCC"))

#{0:^20} GENERA UN RANGO DE 20 ESPACIOS Y COLOCA EL TEXTO EN EL MEDIO.



import string

#| trivial
2#

import string

a="jklmnopq"
suffix = "ack"

for index,p in enumerate(a):
    a=a.upper()
    if p != "q":
        print(a[index]+suffix)
    else:
        print(a[index]+"u"+suffix)


#3

def count_letters(string,letter):

   #  devuelve la cantidad de veces que aparece
  #  letter en el string ingresado, sin importar que tenga mayúsculas

    cont=0
    z = string.lower()
    w = letter.lower()
    for p in z:
        if w == p:
            cont+=1
    return cont

a = str(input("ingrese string: "),)
b = str(input("ingrese LETTER: "),)

print(count_letters(a,b))
"""

"""

# función find en un slice

def find2(haystack, needle, start):
    for index,letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
    return -1

print(find2("banana", "a", 3))  # ir cambiando acá el número

#al hacer enumerate(haystack[start:] me va a encontrar siempre el índice relativo a
#start, osea a partir de start cuenta 0



#4

def count_letters2(text,letter):

    cont = 0
    z = 0

   # if text.find(letter,z) == -1:
    #    return "no aparece la letra ingresada en el texto ingresado"

    while z<len(text):
        if text.find(letter,z) == -1:
            return cont
        else:
            z = 1+text.find(letter,z)
            cont += 1
    return cont

a = str(input("ingrese string: "),)
b = str(input("ingrese LETTER: "),)

print(count_letters2(a,b))

"""

#5

import string

a = """Las matemáticas son un lenguaje hermoso; uno de los principales
motivos es que dicen precisamente cualquier cosa que se propongan.
De lo contrario, no están bien escritas. En general todos los lenguajes
formales hacen lo mismo?

def remove_punctuation(phrase):
    b = ""
    for letter in phrase:
        if letter not in string.punctuation:
            b += letter
    return b

def break_string(phrase):
    return phrase.split()

def analysis_phrase(phrase):
    cont = 0
    for _ in break_string(remove_punctuation(phrase)):
        if "e" in _:
            cont += 1
    return cont

print("your text contains {0} words, of which {1} ({2:.2f}%) contains an 'e'.".format(len(break_string(a)),analysis_phrase(a),100*analysis_phrase(a)/len(break_string(a))))


#6

import string
text1 = " {0:>2}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}"
text = "{0:>2}:{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}"

print(text1.format("",1,2,3,4,5,6,7,8,9,10,11,12))
print("  :------------------------------------------------------------")

for _ in range(1,13):
    print(text.format(_,_*1,_*2,_*3,_*4,_*5,_*6,_*7,_*8,_*9,_*10,_*11,_*12))




#7
def reverse(string):
    b = ""
    for _ in range(len(string)):
        b += string[len(string)-1-_]
    return b

a = str(input("ingrese palabra a dar vuelta: ",))

print(reverse(a))

#8

def mirror(string):
    return string+reverse(string)

print(mirror(a))

#9
def remove_letter(letter,string):
    b =""
    for _ in string:
        if _ != letter:
            b += _
    return b

b= str(input("ingrese letra a quitar de la palabra ingresada: ",))

print(remove_letter(b,a))

#10
def is_palindrome(string):
    return string == reverse(string)

print(is_palindrome(a))


import string

#11
def count(substring,string):
    z = 0
    cont = 0
    appearance = string.find(substring)
    while z<len(string):
        if string.find(substring, z) == -1:
            return cont
        cont += 1
        z = 1 + string.find(substring,z)
    return cont

b= str(input("ingrese palabra a quitarle la parte: ",))
a= str(input("ingrese parte a contabilizar cuantas veces aparece: ",))

print(count(a,b))

#12
def remove(substring,string):
    b=""
    index = string.find(substring)
    cant = len(substring)
    i=0
    if substring not in string:
        return string
    else:
        while i<len(string):
            if i == index:
                i += cant
            else:
                b += string[i]
                i += 1
    return b

b= str(input("ingrese palabra a quitarle la parte: ",))
a= str(input("ingrese parte a eliminar: ",))

print(remove(a,b))


#13

def remove(substring,string):
    b=""
    index = string.find(substring)
    cant = len(substring)
    i=0
    if substring not in string:
        return string
    else:
        while i<len(string):
            if i == index:
                i += cant
                index = string.find(substring, index + 1)
            else:
                b += string[i]
                i += 1
    return b

b= str(input("ingrese palabra a quitarle la parte: ",))
a= str(input("ingrese parte a eliminar: ",))

print(remove(a,b))


"""

import string
a = str(input("ingrese texto: ",))
while a.rfind("zzz") == -1:
    b = str(input("ingrese texto, para terminar ingrese 'zzz': ",))
    a += ""+b

def remove_punctuation(phrase):
    b = ""
    for letter in phrase:
        if letter not in string.punctuation:
            b += letter
    return b

def break_string(phrase):
    return phrase.split()

def analysis_phrase(phrase):
    cont = 0
    for _ in break_string(remove_punctuation(phrase)):
        if "e" in _:
            cont += 1
    return cont

print("your text contains {0} words, of which {1} ({2:.2f}%) contains an 'e'.".format(len(break_string(a)),analysis_phrase(a),100*analysis_phrase(a)/len(break_string(a))))

