
"""
Program: Video Game Backlog Tracker
Author: Colin Lee
Purpose: Allow users to add, view, search, complete, and rate video games while tracking statistics.
Resources: Python Crash Course, 3rd Edition;
Date: September 25, 2026
"""

from game import Game

games = []

def show_statistics(games):
  """Display total, completed, and remaining game statistics."""
  total_games = len(games)
  completed_games = 0

  for game in games:
    if game.status.lower() == "completed":
      completed_games += 1

  remaining_games = total_games - completed_games

  print("\nGame Statistics")
  print("Total games:", total_games)
  print("Completed games:", completed_games)
  print("Remaining games:", remaining_games)

def find_game(games, title):
  """Return a game that matches the requested title."""
  for game in games:
    if game.title.lower() == title.lower():
      return game

  return None

def add_game(games):
  """Create a new Game object and add it to the backlog."""
  title = input("Enter the game title: ")
  genre = input("Enter the game genre: ")
  status = input("Enter the game status: ")

  game = Game(title, genre, status)
  games.append(game)

  print(title, "was added to your backlog!")

print("Welcome to the Video Game Backlog Tracker!")
while True:
  print("\nMenu")
  print("1. Add a game")
  print("2. View games")
  print("3. Search for a game")
  print("4. Mark a game as completed")
  print("5. Rate a game")
  print("6. Show statistics")
  print("7. Quit")
  
  choice = input("Enter your choice: ")
  if choice == "1":
    add_game(games)
  elif choice == "2":
      if len(games) == 0:
        print("No games in your backlog.")
      else:
        for game in games:
         print(game.title, "-", game.genre, "-", game.status)

         if game.rating is not None:
            print("Rating:", game.rating, "/10")
  elif choice == "3":
    search = input("Enter the game title:")

    game = find_game(games, search)

    if game:
        print("Game found!")
        print("Title:", game.title)
        print("Genre:", game.genre)
        print("Status:", game.status)

        if game.rating is not None:
          print("Rating:", game.rating, "/10")
    else:
        print("Game not found.")
  elif choice == "4":
    title = input("Enter the game title: ")

    found = False

    for game in games:
      if game.title.lower() == title.lower():
          game.mark_completed()
          print(title, "has been marked as completed!")
          found = True
          break

    if not found:
        print("Game not found.")
  elif choice == "5":
    title = input("Enter the game title: ")

    found = False

    for game in games:
      if game.title.lower() == title.lower():
          rating = input("Rate this game from 1 to 10: ")

          if rating.isdigit() and 1 <= int(rating) <= 10:
              game.rate_game(int(rating))
              print(title, "has been rated", rating, "out of 10!")
          else:
              print("Invalid rating. Enter a number from 1 to 10.")

          found = True
          break

    if not found:
        print("Game not found.")
  elif choice == "6":
      show_statistics(games)
  elif choice == "7":
    print("Goodbye!")
    break
    
  else:
    print("Invalid choice")
