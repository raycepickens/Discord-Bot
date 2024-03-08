import random
import requests

BASE_URL= "https://www.swapi.tech/api/"

def get_random_char():
    response = requests.get(BASE_URL + "people/")
    if response.status_code == 200:
        data = response.json()  
        character = random.choice(data["results"])
        return f"Heres a character I created: {character['name']}"
    else:
        return "Sorry the dark side is clouding my vision"

def get_random_planet():
    response = requests.get(BASE_URL + "planets/")
    if response.status_code == 200:
        data = response.json()
        planet =random.choice(data["results"])
        return f"{planet['name']} is a planet in a galax far far away"


def get_random_species():
    response = requests.get(BASE_URL + "species/")
    if response.status_code == 200:
        data = response.json()
        species = random.choice(data["results"])
        return f"Have you ever met a {species['name']}?"  
    else:
        return "Sorry, the dark side is clouding my vision"

def get_random_vehicles():
    response = requests.get(BASE_URL + "vehicles/")
    if response.status_code == 200:
        data = response.json()
        vehicle = random.choice(data["results"])
        return f"One of my favorite vehicles is the {vehicle['name']}... you should get one, if you have the credits. ."  
    else:
        return "Sorry, the dark side is clouding my vision"

def get_random_starships():
    response = requests.get(BASE_URL + "starships/")
    if response.status_code == 200:
        data = response.json()
        starship = random.choice(data["results"])
        return f"The {starship['name']} needs a pilot, time to make the Kessel run! "  
    else:
        return "Sorry, the dark side is clouding my vision"


def handle_response(message: str) -> str:
    p_message = message.lower()
    if p_message == "!planet" :
        
        return get_random_planet()
    
    if p_message == "!character" :
        ##print(get_random_char)
        return get_random_char()
        
    if p_message == "!species":
        ##print(get_random_film)
        return get_random_species()
    
    if p_message == "!vehicle":
        ##print(get_random_film)
        return get_random_vehicles()
    
    if p_message == "!starship":
        ##print(get_random_film)
        return get_random_starships()


    if p_message == "!hello":
        return "Hi im George!!! In my unbiased opinion the first 6 StarWars movies are better..."

    