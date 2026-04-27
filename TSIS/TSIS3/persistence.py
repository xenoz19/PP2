import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"


def load_settings():

    if not os.path.exists(SETTINGS_FILE):

        settings = {
            "difficulty": "normal",
            "sound": True,
            "color": "blue"
        }

        save_settings(settings)

        return settings

    with open(SETTINGS_FILE, "r") as f:

        return json.load(f)


def save_settings(settings):

    with open(SETTINGS_FILE, "w") as f:

        json.dump(settings, f, indent=4)


def load_leaderboard():

    if not os.path.exists(LEADERBOARD_FILE):

        return []

    with open(LEADERBOARD_FILE, "r") as f:

        return json.load(f)


def save_score(name, coins, distance):

    data = load_leaderboard()

    data.append({
        "name": name,
        "coins": coins,
        "distance": distance
    })

    data = sorted(
        data,
        key=lambda x: x["coins"],
        reverse=True
    )[:10]

    with open(LEADERBOARD_FILE, "w") as f:

        json.dump(data, f, indent=4)