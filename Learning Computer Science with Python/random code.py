"""
a = str(input("ingrese palabra o texto: ",))

count_letter = {}

for letter in a:
    count_letter[letter] = count_letter.get(letter,0)+1

print(count_letter)



#1
import string

a = str(input("ingrese palabra o texto: ",))

a_lower = a.lower()
b = list(a_lower)
b.sort()
inventory_of_letters = {}

for letter in b:
    inventory_of_letters[letter] = inventory_of_letters.get(letter,0)+1

for key in inventory_of_letters:
    print("{0:>5} {1:>5}".format(key,inventory_of_letters[key]))



#2

def add_fruit(new_inventory,fruit,q = 0):
    new_inventory[fruit] = q
    return new_inventory

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(new_inventory)
print(("strawberries" in new_inventory))
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)

"""

#3

def tuplesv2(a,b,c):

    var1 = a
    var2 = b
    var3 = c

    import turtle
    import math
    c=0
    while var1+var2+var3<9:
        compute = turtle.Turtle()
        window = turtle.Screen()
        compute.forward(a+b+c)

        c +=1
        if c >10:
            break



tuplesv2(2,3,3)

