import os
import json

def add_build():
    build_name = input("Enter the name of the new build: ").strip()
    race = input("What race is this build for? (terran/protoss/zerg): ").strip().lower()
    if race == "terran":
        matchup = input("What matchup is this build for? (tvz/tvt/tvp/all): ").strip().lower()
    
    elif race == "protoss":
        matchup = input("What matchup is this build for? (pvz/pvt/pvp/all): ").strip().lower()
    elif race == "zerg":
        matchup = input("What matchup is this build for? (zvz/zvt/zvp/all): ").strip().lower()
    else:
        print("Invalid choice")
    build_steps = []
    while True:
        supply = input("Enter supply count for the step (or 'done' to finish): ").strip().lower()
        if supply == "done":
            break
        if not supply.isdigit():
            print("Invalid supply count. Please enter a number.")
            supply = int(supply)
            continue
            
            

        action = input("Enter action for this supply count: ").strip()
        build_steps.append({"supply": supply, "action": action})
    build_data = {
        "build_name": build_name,
        "race": race,
        "matchup": matchup,
        "steps": build_steps
    }
    base_dir = "build-orders"
    clean_name = build_name.strip().lower().replace(" ", "_")
    file_path = os.path.join(base_dir, race, matchup, f"{clean_name}.json")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as f:
        json.dump(build_data, f, indent=4)
    print(f"Build '{build_name}' added successfully at {file_path}")


         