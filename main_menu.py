import pickle
from typing import Dict
from intorduction import *


def save_game(game_state: Dict, filename: str):
    """Saves the characters in current game"""
    with open(f"{filename}.pickle", "wb") as f:
        pickle.dump(game_state["characters"], f)


def load_game(game_state, filename: str) -> Dict:
    """Loads in the characters and their details"""
    with open(f"{filename}.pickle", "rb") as f:
        game_state["characters"] = pickle.load(f)

    return game_state


def main_menu():
    """Presents the player with choices in the main menu"""
    from base_material import game_state
    while True:
        print("1. New Game")
        print("2. Load Game")
        print("3. Save Game")
        print("4. Exit Menu")
        print("0. Quit Game")
        choice = input("Enter your choice: ")

        if choice == "1":
            introduction()
        
        elif choice == "2":

            filename = input("Enter the name of the save file: ")
            try:
                game_state = load_game(game_state, filename)
            except FileNotFoundError:
                print("Save file not found. Please choose a different file or create a new game.")

        elif choice == "3":

            filename = input("Enter the name of the save file: ")
            save_game(game_state, filename)

        elif choice == "4":
            return

        elif choice == "0":
            quit()
        else:
            print("Invalid choice. Please try again.")
