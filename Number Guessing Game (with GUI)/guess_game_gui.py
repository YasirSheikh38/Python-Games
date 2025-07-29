import tkinter as tk
import random

# Generate the number
secret_number = random.randint(1, 100)
attempts_left = 10

def check_guess():
    global attempts_left, secret_number

    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="⛔ Please enter a valid number.")
        return

    guess = int(guess)
    attempts_left -= 1

    if guess < secret_number:
        result_label.config(text=f"Too low! Attempts left: {attempts_left}")
    elif guess > secret_number:
        result_label.config(text=f"Too high! Attempts left: {attempts_left}")
    else:
        result_label.config(text="🎉 Correct! You win!")
        guess_button.config(state=tk.DISABLED)
        return

    if attempts_left == 0:
        result_label.config(text=f"💀 Game Over! The number was {secret_number}")
        guess_button.config(state=tk.DISABLED)

def restart_game():
    global secret_number, attempts_left
    secret_number = random.randint(1, 100)
    attempts_left = 10
    result_label.config(text="Guess a number between 1 and 100")
    guess_button.config(state=tk.NORMAL)
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("🎲 Number Guessing Game")
root.geometry("400x250")

title = tk.Label(root, text="Guess the number (1-100)", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

guess_button = tk.Button(root, text="Check Guess", command=check_guess)
guess_button.pack()

restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.pack(pady=5)

result_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
