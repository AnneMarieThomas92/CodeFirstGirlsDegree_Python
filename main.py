## Import the requests module.
import requests

#Creating a dictionary to store the pokemon types.
pokemon_type_dict = dict()

##Function to be called when checking if Pokemon type is already in array.
def does_type_already_exist(type_name):
    for key,value in pokemon_type_dict.items():
        for type in value:
            if type_name ==type:
                print (f"A {type_name.capitalize()} type Pokemon has already been chosen. Please chose another.")
                return True
    return False

#Ask the user for their name to create their Pokemon Trainer name.
user_name = input("What is your name?")
trainer_name = user_name[:4]

#Create a file to write the results.
with open("Pokemon_deck.txt","w") as file:

#Welcoming user and asking them to chose a pokemon.
    print(f"Welcome, Trainer {trainer_name}!")
    print("Pick three different types of Pokemon to add to your deck. ")

#Checking the amount of Pokemon stored in the array.
    while len(pokemon_type_dict) <=3:
        if len(pokemon_type_dict) ==3:
            print("You have chosen 3 different types of Pokemon and your deck is complete!")
            break

        pokemon_name= input("Type the name of a Pokemon and press enter to add it to your deck:\n")
        pokemon_name= pokemon_name.lower()
        response_API = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')

#Checking the response status from the API and storing the Pokemon type in a dictionary of pokemon:pokemon_types[]
        status_code = response_API.status_code
        if status_code ==200:
            response_data = response_API.json()
            pokemon_types = []
            continue_flag = False
            for type in response_data["types"]:
                if does_type_already_exist(type["type"]["name"]):
                    continue_flag = True
                else:
                    pokemon_types.append(type["type"]["name"])
            if continue_flag:
                continue
            pokemon_type_dict[pokemon_name]=pokemon_types
            print (f"You chose {pokemon_name.capitalize()}.")
            print (f"{pokemon_name.capitalize()} is a",end="")
            for type_name in pokemon_types:
                print(f" {type_name.capitalize()}",end="")
            print (" type pokemon.",end="")
# Write the results in a file.
            file.write(f"You chose {pokemon_name.capitalize()}. ")
            file.write(f"{pokemon_name.capitalize()} is a")
            for type_name in pokemon_types:
                file.write(f" {type_name.capitalize() }")
            file.write(" type pokemon.\n")

        else:
            print (f"{pokemon_name.capitalize()} is not valid. Please try again.")
#Close the file
file.close()
