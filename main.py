import json
import os
from build_reader import run_build
from load_build import load_build
from add_build import add_build
from tnkter_ui import run_overlay
def main():
    while True:
        print("Welcome to Macro-Overlay")
        print("Main Menu:")
        user_choice = input(" 1 - Load Build \n 2 - Add Build \n 3 - Exit\n ")
        if user_choice == "1":
            steps = load_build()
            run_build(steps)
            input("Press Enter to return to the main menu...")
        elif user_choice == "2":
            add_build()
        elif user_choice == "3":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()





    

