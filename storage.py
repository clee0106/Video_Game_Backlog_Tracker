"""
Program: Video Game Backlog Tracker
Author: Colin Lee
Purpose: Saves and loads backlog data using JSON.
Resources: Python Crash Course, 3rd Edition
Date: October 28, 2026
"""

import json
from pathlib import Path

from game import Game


DATA_FILE = Path("games.json")


def save_games(games):
    """Save the current backlog to a JSON file."""
    game_data = []

    for game in games:
        game_data.append({
            "title": game.title,
            "genre": game.genre,
            "status": game.status,
            "rating": game.rating
        })

    DATA_FILE.write_text(json.dumps(game_data, indent=4))


def load_games():
    """Load backlog data from JSON and return Game objects."""
    try:
        contents = DATA_FILE.read_text()
        game_data = json.loads(contents)
    except FileNotFoundError:
        return []

    games = []

    for item in game_data:
        game = Game(
            item["title"],
            item["genre"],
            item["status"]
        )
        game.rating = item["rating"]
        games.append(game)

    return games