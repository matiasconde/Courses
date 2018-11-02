## 4. Implementing Binary Search: Part 1 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    # We need to format our name appropriately for successful comparison
    name = format_name(name)
    # First guess halfway through the list
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[first_guess_index][0])
    # Check where we should continue searching
    if first_guess < name: return "later"
    elif first_guess > name: return "earlier"
    else: return "found"
    
johnson_odom_age = player_age("Darius Johnson-Odom")
young_age = player_age("Nick Young")
adrien_age = player_age("Jeff Adrien")

## 5. Implementing Binary Search: Part 2 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    # We need to format our name appropriately for successful comparison
    name = format_name(name)
    # Initial bounds of the search
    upper_bound = length - 1
    lower_bound = 0
    # Index of first split
    first_guess_index = math.floor(length/2)
    first_guess = format_name(nba[first_guess_index][0])
    if first_guess > name: 
        upper_bound = first_guess_index-1
        lower_bound = lower_bound
        length2 = upper_bound+(lower_bound)
        second_guess_index = math.floor(length2/2)
        return format_name(nba[second_guess_index][0])
    elif first_guess < name:
        upper_bound = upper_bound
        lower_bound = first_guess_index+1
        length2 = upper_bound+(lower_bound)
        second_guess_index = math.floor(length2/2)
        
        return format_name(nba[second_guess_index][0])   
    else: return first_guess

gasol_age = player_age("Pau Gasol")
pierce_age = player_age("Paul Pierce")

## 7. Implementing Binary Search: Part 3 ##

# A function to extract a player's last name
def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)

# Implement the player_age function. For now, just return what the instructions specify
def player_age(name):
    # We need to format our name appropriately for successful comparison
    name = format_name(name)
    # Bounds of the search
    upper_bound = length - 1
    lower_bound = 0
    # Index of first split. It's important to understand how we compute this
    index = math.floor((upper_bound + lower_bound) / 2)
    # First, guess halfway through the list
    guess = format_name(nba[index][0])
    
    while guess != name: 
    
        if name < guess: 
            upper_bound = index - 1
            lower_bound = lower_bound
            index = math.floor((upper_bound+lower_bound)/2)
            guess = format_name(nba[index][0])
        elif name > guess: 
            upper_bound = upper_bound
            lower_bound = index + 1 
            index = math.floor((upper_bound+lower_bound)/2)
            guess = format_name(nba[index][0])
        else : return "found"
    
    return "found"

carmelo_age = player_age("Carmelo Anthony")

    # Keep guessing until it finds the name. Use a while loop here.
        # Check where our guess is in relation to the name we're requesting,
        #     and adjust our bounds as necessary (multiple lines here).
        #     If we have found the name, we wouldn't be in this loop, so
        #     we shouldn't worry about that case
        # Find the new index of our guess
        # Find and format the new guess value
    # When our loop terminates, we have found the right NBA player's name

## 8. Implementing Binary Search: Part 4 ##

def format_name(name):
    return name.split(" ")[1] + ", " + name.split(" ")[0]

# The length of the data set
length = len(nba)


def player_age(name): 
    
    name = format_name(name)
    upper_bound = length - 1
    lower_bound = 0
    
    index = math.floor((upper_bound+lower_bound)/2)
    guess = format_name(nba[index][0])
    
    while name  != guess and lower_bound <= upper_bound:
       
        if name < guess: 
            upper_bound = index - 1
            lower_bound = lower_bound
            index = math.floor((upper_bound+lower_bound)/2)
            guess = format_name(nba[index][0])
        elif name > guess: 
            upper_bound = upper_bound
            lower_bound = index + 1
            index = math.floor((upper_bound+lower_bound)/2)
            guess = format_name(nba[index][0])
    
    if name == guess: 
        return nba[index][2]
    else: 
        return -1

curry_age = player_age("Stephen Curry")
griffin_age = player_age("Blake Griffin")
jordan_age = player_age("Michael Jordan")