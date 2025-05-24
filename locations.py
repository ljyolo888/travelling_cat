"""
Location data and management for the Travelling Cat game
Features 4 popular Sydney tourist spots
"""

import random

class Location:
    def __init__(self):
        #dictionary of location_name: location_data
        self.locations = {
            "Sydney Opera House": {
                "mood_change": -5, #kitten doesn't take to the opera
                "description": "sitting on the steps, watching boats in the harbour",
                "food_options": ["Market sashimi", "Sydney rock oysters", "Marinated octopus"],
                "play_options": ["chase seagulls", "watch symphony performances", "tag along with a guidedtour"]
            },
            "Bondi Beach": {
                "mood_change": 6,
                "description": "lounging on the warm sand, listening to the waves",
                "food_options": ["Fish and chips", "Prawn pizza", "Gelato"],
                "play_options": ["build sandcastles", "surfing", "sunbathe"]
            },
            "Royal Botanic Gardens": {
                "mood_change": 7,
                "description": "hiding among lush plants and flowers, very peaceful",
                "food_options": ["Gyoza", "Fresh herb salad", "Sushi"],
                "play_options": ["explore plant collections", "chase butterflies", "nap in flower beds"]
            },
            "Queen Victoria Building": {
                "mood_change": 8,
                "description": "wandering through the beautiful shopping arcade, admiring the architecture",
                "food_options": ["Large cup of Boost juice", "Salmon gravlax", "Fish tacos"],
                "play_options": ["explore the shops", "listen to the Great Australian Clock", "people watch"]
            }
        }
        
    def get_random_location(self):
        return random.choice(list(self.locations.keys()))
    
    def get_location_data(self, location_name):
        #default to empty dict if location not found
        return self.locations.get(location_name, {})
    
    def get_all_locations(self):
        return list(self.locations.keys())
    
    def get_location_description(self, location_name):
        #default to unknown if location not found
        location_data = self.locations.get(location_name, {})
        return location_data.get("description", "somewhere unknown")
    
    def get_food_options(self, location_name):
        #default to basic cat food if location not found
        location_data = self.locations.get(location_name, {})
        return location_data.get("food_options", ["basic cat food"])
    
    def get_play_options(self, location_name):
        #default to basic play if location not found
        location_data = self.locations.get(location_name, {})
        return location_data.get("play_options", ["basic play"])