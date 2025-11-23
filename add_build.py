import json
from pathlib import Path  
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

   
    build_root = Path("build-orders")  
    clean_name = build_name.strip().lower().replace(" ", "_")

    file_path = build_root / race / matchup / f"{clean_name}.json"

    
    file_path.parent.mkdir(parents=True, exist_ok=True)

    
    file_path.write_text(json.dumps(build_data, indent=4), encoding="utf-8")
    #

    print(f"Build '{build_name}' added successfully at {file_path}")
