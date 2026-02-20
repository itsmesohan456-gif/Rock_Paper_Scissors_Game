import random
import sqlite3

conct = sqlite3.connect('game_results.db')
cursor = conct.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXIST stats ( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_choice TEXT,
               computer_choice TEXT,
               result TEXT
    )
''')
conct.commit()

def play_game():
    options = ["rock", "paper", "scissors"]

    print("--- Welcome to Rock, Paper, Scissors! ---")
    
    user_choice = input("Enter your choice from Rock, Paper, or Scissors (or quit to stop): ").lower()

    if user_choice == 'quit':
        return False
    
    if user_choice not in options:
        print("Oops!!\nInvalid move!!\nTry again")
        return True
    
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "Draw"
    elif (user_choice == "rock" and 
    computer_choice == "scissors") or \
             (user_choice == "paper" and 
    computer_choice == "rock") or \
             (user_choice == "scissors" and 
    computer_choice == "paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    print(f"Result: {result}")

                 