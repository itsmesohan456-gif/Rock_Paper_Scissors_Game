import random
import sqlite3

conct = sqlite3.connect('game_results.db')
cursor = conct.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS stats ( 
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

    cursor.execute('INSERT INTO stats (user_choice, computer_choice, result) VALUES (?, ?, ?)',
                   (user_choice, computer_choice, result))
    conct.commit()

    return True

playing = True
while playing:
    playing = play_game()

print("]n--- FINAL GAME STATISTICS ---")
cursor.execute('SELECT result, COUNT(*) FROM stats GROUP by result')
summary = cursor.fetchall()

for row in summary: 
  print(f"{row[0]}: {row[1]}")

conct.close()
print("Thanks for playing the game!")