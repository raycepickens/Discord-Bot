import random
#To make a HTTP request to get an api 
import requests
#Base api 
BASE_URL= "https://www.swapi.tech/api/"
#Function returning one instance of a person
def get_random_char():
    #An API call for people
    response = requests.get(BASE_URL + "people/")
    if response.status_code == 200:
        data = response.json()  
        character = random.choice(data["results"])
        return f"Heres a character I created: {character['name']}"
    else:
        return "Sorry the dark side is clouding my vision"
#Function returning one instance of a planet
def get_random_planet():
    #An API call for planets
    response = requests.get(BASE_URL + "planets/")
    if response.status_code == 200:
        data = response.json()
        planet =random.choice(data["results"])
        return f"{planet['name']} is a planet in a galax far far away"
#Function returning one instance of a species
def get_random_species():
    #An API call for species
    response = requests.get(BASE_URL + "species/")
    if response.status_code == 200:
        data = response.json()
        species = random.choice(data["results"])
        return f"Have you ever met a {species['name']}?"  
    else:
        return "Sorry, the dark side is clouding my vision"
#Function returning one instance of a vehicle
def get_random_vehicles():
    #An API call for vehicles 
    response = requests.get(BASE_URL + "vehicles/")
    if response.status_code == 200:
        data = response.json()
        vehicle = random.choice(data["results"])
        return f"One of my favorite vehicles is the {vehicle['name']}... you should get one, if you have the credits. ."  
    else:
        return "Sorry, the dark side is clouding my vision"
#Function returning one instance of a starship
def get_random_starships():
    #An API call for starships
    response = requests.get(BASE_URL + "starships/")
    if response.status_code == 200:
        data = response.json()
        starship = random.choice(data["results"])
        return f"The {starship['name']} needs a pilot, time to make the Kessel run! "  
    else:
        return "Sorry, the dark side is clouding my vision"
#Handles users repsonses in the chatroom with an ! command
def handle_response(message: str) -> str:
    p_message = message.lower()
    #if users message equals !planet, then returns an instance of a planet
    if p_message == "!planet" :
        
        return get_random_planet()
    #if users message equals !character, then returns an instance of a character
    if p_message == "!character" :
        ##print(get_random_char)
        return get_random_char()
    #if users message equals !species, then returns an instance of a species   
    if p_message == "!species":
        ##print(get_random_film)
        return get_random_species()
    #if users message equals !vehicle, then returns an instance of a vehicle
    if p_message == "!vehicle":
        ##print(get_random_film)
        return get_random_vehicles()
    #if users message equals !starship, then returns an instance of a starship
    if p_message == "!starship":
        ##print(get_random_film)
        return get_random_starships()

    #if users message equals !hello, then returns a message
    if p_message == "!hello":
        return "Hi im George!!! In my unbiased opinion the first 6 StarWars movies are better..."

    