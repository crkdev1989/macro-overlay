import json
import os
from build_reader import run_build
race_choice  = input("Choose your race: 1 - Terran \n 2 - Protoss \n 3 - Zerg\n ")

steps = []
selected_race = ""

if race_choice == "1":
    selected_race = "terran"
elif race_choice == "2":
    selected_race = "protoss"
elif race_choice == "3":
    selected_race = "zerg"
else:
        print("Invalid choice") 

if selected_race == "terran":
    mu = input(" Matchup? 1 - TvZ \n 2 - TvT \n 3 - TvP \n 4 - all \n ")
    if mu == "1":
        mu = "tvz"
    elif mu == "2":
        mu = "tvt"
    elif mu == "3":
        mu = "tvp"
    elif mu == "4":
        mu = "all"
    else:
        print("Invalid matchup choice")

if selected_race == "protoss":
    mu = input(" Matchup? 1 - PvZ \n 2 - PvT \n 3 - PvP \n 4 - all \n ")
    if mu == "1":
        mu = "pvz"
    elif mu == "2":
        mu = "pvt"
    elif mu == "3":
        mu = "pvp"
    elif mu == "4":
        mu = "all"
    else:
        print("Invalid matchup choice")

if selected_race == "zerg":
    mu = input(" Matchup? 1 - ZvZ \n 2 - ZvT \n 3 - ZvP \n 4 - all \n ")
    if mu == "1":
        mu = "zvz"
    elif mu == "2":
        mu = "zvt"
    elif mu == "3":
        mu = "zvp"
    elif mu == "4":
        mu = "all"
    else:
        print("Invalid matchup choice")
 
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
    
run_build(steps)  



    

