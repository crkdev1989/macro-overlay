
import json
from pathlib import Path
from constants import RACE_MENU, MATCHUP_MENU

BUILD_ROOT = Path("build-orders")


def list_races():
    
    return list(dict.fromkeys(RACE_MENU.values())) 

def list_matchups(race: str):
    
    return list(MATCHUP_MENU[race].values())


def list_build_files(race: str, matchup: str):
    target_dir = BUILD_ROOT / race / matchup
    if not target_dir.exists():
        return []
    return sorted(target_dir.glob("*.json"))  


def load_build_from_file(path: Path):
    data = json.loads(path.read_text())
    steps = []
    for entry in data.get("steps", []):
        steps.append({
            "supply": int(entry["supply"]),
            "action": entry["action"],
        })
    return steps