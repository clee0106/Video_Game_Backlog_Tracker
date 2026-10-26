"""
Program: Video Game Backlog Tracker
Author: Colin Lee
Purpose: Defines the Game class used to represent games in the backlog.
Resources: Python Crash Course, 3rd Edition
Date: October 26, 2026
"""


class Game:
  """Represent a video game in the user's backlog."""

  def __init__(self, title, genre, status="Backlog"):
      """Initialize a game's title, genre, and rating."""
      self.title = title
      self.genre = genre
      self.status = status
      self.rating = None

  def mark_completed(self):
      """Mark the game as completed."""
      self.status = "Completed"

  def rate_game(self, rating):
      """Assign a rating to the game."""
      self.rating = rating
