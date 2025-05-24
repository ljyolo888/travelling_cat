"""
TravellingCat class
"""

import random
from locations import Location

class TravellingCat:
    def __init__(self, name):
        self.name = name
        self.locations = Location()
        self.current_location = None
        self.mood = 50
        self.fullness = 60
        self.energy = 70
        self.visit_history = []
        self.is_present = False #if cat is currently in the location and available to interact with
        
    def appear_randomly(self):
        self.is_present = True
        
        #random location and mood change
        self.current_location = self.locations.get_random_location()
        location_data = self.locations.get_location_data(self.current_location)
        mood_change = location_data.get("mood_change", 0)
        self.mood += mood_change
        self.mood = max(0, min(100, self.mood))  # Keep between 0-100
        
        # Hunger and energy slightly decrease from traveling; keep above 0
        self.fullness = max(0, self.fullness - random.randint(5, 10))
        self.energy = max(0, self.energy - random.randint(5, 10))
        
        # Add to visit history
        self.visit_history.append(self.current_location)

        #generate arrival message
        arrival_message = self.get_arrival_message()
        return arrival_message
    
    def get_arrival_message(self):
        description = self.locations.get_location_description(self.current_location)
        feeling = self.get_mood_description()
        return f'''
ฅ^•ﻌ•^ฅ {self.name} appears at {self.current_location}.
{self.name} is {description} and {feeling}.'''
    
    def get_mood_description(self):
        if self.mood > 80:
            return "purring, feeling happy"
        elif self.mood > 50:
            return "seems okay, could be better though"
        elif self.mood > 20:
            return "looking a bit grumpy"
        else:
            return "quite unhappy and stressed"
    
    def feed(self, food_choice):
        if self.fullness == 100:
            return f"\n{self.name} is full!\n"
        
        fullness_increase = random.randint(20, 30)
        mood_boost = random.randint(5, 10)
        self.fullness = min(100, self.fullness + fullness_increase)
        self.mood = min(100, self.mood + mood_boost)
        return f'''
You order {food_choice} to be delivered to {self.current_location}.
{self.name} devours it eagerly! Fullness and mood improved!'''
    
    def play(self, play_choice):
        energy_cost = random.randint(5, 10)
        mood_boost = random.randint(10, 20)
        self.energy = max(0, self.energy - energy_cost)
        self.mood = min(100, self.mood + mood_boost)
        return f'''
You encourage {self.name} to {play_choice}.
{self.name} has a great time! Mood improved.'''
    
    def chat(self):
        user_message = input(f"\nWhat would you like to say to {self.name}? ")
    
        # Cat responds based on keywords in user's message
        # can't use a for loop directly in an if statement, hence any()
        if any(word in user_message.lower() for word in ['lov', 'miss', 'cute', 'adorable', 'sweet', 'hug', 'pet']):
            response = f"*{self.name} purrs loudly and looks very happy*"
        elif any(word in user_message.lower() for word in ['food', 'hungry', 'starve', 'eat', 'treat', 'snack', 'meal']):
            response = f"*{self.name} meows and looks toward their food expectantly*"
        elif any(word in user_message.lower() for word in ['play', 'fun', 'game', 'toy', 'ball', 'fetch','jump']):
            response = f"*{self.name} gets excited and looks around playfully*"
        else:
            response = f"*{self.name} meows in response and seems to consider the idea*"

        self.mood = min(100, self.mood + 10)
        return f"\n{response}\n{self.name} seems happy you're talking to them!"
    
    def say_goodbye(self):
        self.is_present = False
        self.current_location = None
        return f"\n{self.name} meows goodbye and disappears into the crowd!\n"
    
    def get_status(self):
        status = f'''
========== {self.name}'s Status ==========
Location: {self.current_location}
Mood: {self.mood}/100 ({self.get_mood_description()})
Fullness: {self.fullness}/100
Energy: {self.energy}/100
Recent location: {self.visit_history[-1] if len(self.visit_history) > 1 else "No recent locations"}
========================================'''  
        return status
    
    