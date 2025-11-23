import os
import json
from constants import RACE_MENU, MATCHUP_MENU, MATCHUP_PROMPTS

def load_build():
    steps = []
    while True:
       race_choice = input("Choose your race:\n 1 - Terran \n 2 - Protoss \n 3 - Zerg\n ").strip()
       if race_choice in RACE_MENU:
           selected_race = RACE_MENU[race_choice]
           break
       print("Invalid choice, try again.")

    # choose matchup for that race
    while True:
        mu_choice = input(MATCHUP_PROMPTS[selected_race]).strip()
        if mu_choice in MATCHUP_MENU[selected_race]:
            mu = MATCHUP_MENU[selected_race][mu_choice]
            break
        print("Invalid choice, try again.")
    
    build_list = os.listdir(f"build-orders/{selected_race}/{mu}/") 
    for number, file in enumerate(build_list, start=1 ):
        print(f"{number} - {file}")
    user_choice = input("Select a build by number: ")

    number = int(user_choice)
    index = number - 1
    chosen_build = build_list[index]

    with open(f"build-orders/{selected_race}/{mu}/{chosen_build}", "r") as f:
        print(f)

        for string in f:
            clean = string.strip()
            parts = clean.split(" ")
            supply_str = parts[0]
            action = " ".join(parts[1:])
            supply = int(supply_str)
            step = {"supply": supply,"action": action}
            steps.append(step)
    return steps
