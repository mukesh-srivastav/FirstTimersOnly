import random
import tkinter as tk
from tkinter import messagebox

class GuessGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number!")

        # Configure window dimensions and background color
        master.geometry("400x250")
        master.configure(bg="#f0f8ff")  # Light blue background

        # Generate secret number and initialize variables
        self.secret_number = random.randint(1, 25)
        self.guess_count = 1
        self.max_guesses = 3

        # Create instruction label with clear formatting
        self.instruction_label = tk.Label(
            master,
            text="Welcome to the Guessing Game!\nYou have 3 chances to guess a number between 1 and 25.",
            font=("Helvetica", 14, "bold"),
            fg="#333333",  # Dark gray text color for better readability
            bg="#f0f8ff"   # Match background color
        )
        self.instruction_label.pack(pady=20)  # Add padding for spacing

        # Create entry field with light gray background for contrast
        self.guess_entry = tk.Entry(master, font=("Helvetica", 12), highlightthickness=2, highlightbackground="#dddddd")
        self.guess_entry.pack(pady=10)

        # Create "Guess" button with custom colors and hover effect
        self.guess_button = tk.Button(
            master,
            text="Guess",
            command=self.check_guess,
            font=("Helvetica", 12, "bold"),
            fg="#ffffff",  # White text
            bg="#3399ff",  # Blue button color
            activebackground="#007bff",  # Darker blue on hover
            highlightthickness=0,
            bd=0,
            relief=tk.RAISED
        )
        self.guess_button.pack(pady=10)
        self.guess_button.bind("<Enter>", self.on_enter)
        self.guess_button.bind("<Leave>", self.on_leave)

        # Create result label with centered alignment
        self.result_label = tk.Label(
            master,
            text="",
            font=("Helvetica", 12),
            fg="#333333",
            bg="#f0f8ff",
            justify=tk.CENTER  # Center the text
        )
        self.result_label.pack(pady=10)

    def on_enter(self, e):
        self.guess_button.config(bg="#007bff")

    def on_leave(self, e):
        self.guess_button.config(bg="#3399ff")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guess_entry.delete(0, tk.END)  # Clear the entry field after guess

            if 1 <= guess <= 25:
                if guess == self.secret_number:
                    self.result_label.config(text=f"🎉 Congratulations! You guessed it in {self.guess_count} tries.")
                    self.guess_button.config(state=tk.DISABLED)  # Disable button after win
                elif guess < self.secret_number:
                    closeness = abs(guess - self.secret_number)
                    if closeness > 3:
                        self.result_label.config(text="Your guess is too low. Try higher.")
                    else:
                        self.result_label.config(text="Getting closer! Guess a bit higher.")
                else:
                    closeness = abs(guess - self.secret_number)
                    if closeness > 3:
                        self.result_label.config(text="Your guess is too high. Try lower.")
                    else:
                        self.result_label.config(text="Getting closer! Guess a bit lower.")
                self.guess_count += 1

                if self.guess_count > self.max_guesses:
                    self.result_label.config(text=f"😞 Sorry, you ran out of guesses. The number was {self.secret_number}.")
                    self.guess_button.config(state=tk.DISABLED)  # Disable button after losing
            else:
                self.result_label.config(text="Invalid guess. Please enter a number between 1 and 25.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

root = tk.Tk()
game = GuessGame(root)
root.mainloop()
