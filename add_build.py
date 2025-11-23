import os
import json
from constants import RACE_MENU, MATCHUP_PROMPTS, MATCHUP_MENU

def add_build():
    # --- BUILD NAME ---
    build_name = input("Enter the name of the new build: ").strip()

    # --- RACE SELECTION ---
    while True:
        race_choice = input("Choose your race:\n 1 - Terran\n 2 - Protoss\n 3 - Zerg\n ").strip()
        if race_choice in RACE_MENU:
            race = RACE_MENU[race_choice]
            break
        print("Invalid choice, try again.\n")

    # --- MATCHUP SELECTION ---
    while True:
        mu_choice = input(MATCHUP_PROMPTS[race]).strip()
        if mu_choice in MATCHUP_MENU[race]:
            matchup = MATCHUP_MENU[race][mu_choice]
            break
        print("Invalid matchup choice, try again.\n")

    # --- BUILD STEPS ---
    build_steps = []
    while True:
        supply = input("Enter supply count (or 'done' to finish): ").strip().lower()
        if supply == "done":
            break

        if not supply.isdigit():
            print("Invalid supply — must be a number.")
            continue

        action = input("Enter action for this supply count: ").strip()
        build_steps.append({"supply": supply, "action": action})

    # --- SAVE STRUCTURE ---
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

# Run for testing:
add_build()