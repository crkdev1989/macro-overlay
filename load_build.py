import json
from pathlib import Path
from constants import RACE_MENU, MATCHUP_MENU, MATCHUP_PROMPTS

def load_build():
    # --- RACE SELECTION ---
    while True:
        race_choice = input("Choose your race:\n 1 - Terran \n 2 - Protoss \n 3 - Zerg\n ").strip()
        if race_choice in RACE_MENU:
            selected_race = RACE_MENU[race_choice]
            break
        print("Invalid choice, try again.")

    # --- MATCHUP SELECTION ---
    while True:
        mu_choice = input(MATCHUP_PROMPTS[selected_race]).strip()
        if mu_choice in MATCHUP_MENU[selected_race]:
            matchup = MATCHUP_MENU[selected_race][mu_choice]
            break
        print("Invalid choice, try again.")

    # --- PATHLIB ROOT DIRECTORY ---
    build_root = Path("build-orders")
    target_dir = build_root / selected_race / matchup

    # --- LIST BUILDS ---
    build_list = sorted(target_dir.iterdir())
    if not build_list:
        print("No builds found for that matchup.")
        return []

    for number, file_path in enumerate(build_list, start=1):
        print(f"{number} - {file_path.name}")

    # --- USER PICK ---
    user_choice = input("Select a build by number: ").strip()
    index = int(user_choice) - 1
    chosen_path = build_list[index]

    # --- READ JSON ---
    data = json.loads(chosen_path.read_text())

    steps = []
    for entry in data["steps"]:
        steps.append({
            "supply": int(entry["supply"]),
            "action": entry["action"],
        })

    return steps

