import json

def load_targets():
    with open("config/targets.json", "r", encoding="utf-8") as f:
        return json.load(f)
