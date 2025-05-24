from cat import TravellingCat
from locations import Location
import random

def display_welcome():
    print("=" * 40)
    print("ฅ^•ﻌ•^ฅ WELCOME TO TRAVELLING CAT ฅ^•ﻌ•^ฅ")
    print("+" * 40)
    print("Your cat travels around Sydney's tourist spots!")
    print("Call your cat to see where they appear, then interact with them.")
    print("=" * 40)

def display_main_menu():
    print("\n==MAIN MENU==")
    print('''1. Call your cat
2. Check cat's status
3. Quit game''')
    print("=" * 21)

def display_interaction_menu(cat):
    print(f"\n{cat.name} is waiting at {cat.current_location}!")
    print("\nWhat would you like to do?")
    print('''1. Order food delivery
2. Play with your cat remotely
3. Chat with your cat
4. Say goodbye
5. Check cat's status''')
    print("=" * 30)

def food_delivery(cat):
    locations = cat.locations
    food_options = locations.get_food_options(cat.current_location)
    
    print(f"\nFood delivery options at {cat.current_location}:")
    for i, food in enumerate(food_options, start=1):
        print(f"{i}. {food}")
    
    try:
        choice = int(input("\nWhich food would you like to order? Enter number: ")) - 1
        if 0 <= choice < len(food_options):
            selected_food = food_options[choice]
            result = cat.feed(selected_food)
            print(result)
        else:
            print("Invalid choice!")
    except:
        print("Please enter a valid number!")

def play_activity(cat):
    locations = cat.locations
    play_options = locations.get_play_options(cat.current_location)
    
    print(f"\nPlay activities at {cat.current_location}:")
    for i, activity in enumerate(play_options, start=1):
        print(f"{i}. {activity}")
    
    try:
        choice = int(input("\nWhat activity would you like to encourage? Enter number: ")) - 1
        if 0 <= choice < len(play_options):
            selected_activity = play_options[choice]
            result = cat.play(selected_activity)
            print(result)
        else:
            print("Invalid choice!")
    except:
        print("Please enter a valid number!")

def main():
    display_welcome()
    cat_name = input("What would you like to name your travelling cat? ").strip()
    cat = TravellingCat(cat_name)
    print(f"\nMeet {cat_name} ฅ^•ﻌ•^ฅ, your travelling cat!")
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':  # Call cat
            arrival_message = cat.appear_randomly() #have tocall cat first else no status check
            print(arrival_message)
            
            # Interaction loop while cat is present
            while cat.is_present:
                display_interaction_menu(cat)
                interaction_choice = input("Enter your choice (1-5): ").strip()
                if interaction_choice == '1':  
                    food_delivery(cat)
                elif interaction_choice == '2': 
                    play_activity(cat)
                elif interaction_choice == '3': 
                    message = cat.chat()
                    print(message)
                elif interaction_choice == '4': 
                    goodbye_message = cat.say_goodbye()
                    print(goodbye_message)
                    break #exit inner interaction loop             
                elif interaction_choice == '5':
                    status = cat.get_status()
                    print(status)
                else:
                    print("Invalid choice!")
        
        elif choice == '2':  # Check status
            if cat.is_present:
                status = cat.get_status()
                print(status)
            else:
                print(f"\n{cat_name} is not currently present. Call them first!")
        
        elif choice == '3':  # Quit
            if cat.is_present:
                print(f"\n{cat_name} waves goodbye to you!")
            else:
                print(f"\n{cat_name} is away on another adventure!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()