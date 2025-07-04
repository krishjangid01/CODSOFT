from tkinter import *
import random

# List of options
options = ['Rock', 'Paper', 'Scissors']

# Main window
window = Tk()
window.title("Rock Paper Scissors")
window.geometry("400x450")
window.config(bg="#f0f0f0")

# Result label
result_label = Label(window, text="", font=("Arial", 14), bg="#f0f0f0", fg="#333")
result_label.pack(pady=20)

# Computer choice label
computer_choice_label = Label(window, text="", font=("Arial", 12), bg="#f0f0f0", fg="gray")
computer_choice_label.pack(pady=10)

# Player choice label
player_choice_label = Label(window, text="", font=("Arial", 12), bg="#f0f0f0", fg="gray")
player_choice_label.pack(pady=10)

# Function to handle the game logic
def play(choice):
    user_choice = choice
    computer_choice = random.choice(options)

    player_choice_label.config(text=f"🧍 You chose: {user_choice}")
    computer_choice_label.config(text=f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "😐 It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "🎉 You won!"
    else:
        result = "😢 Computer won!"

    result_label.config(text=result)

# Buttons
btn_frame = Frame(window, bg="#f0f0f0")
btn_frame.pack(pady=30)

rock_btn = Button(btn_frame, text="🪨 Rock", width=12, height=2, font=("Arial", 12), command=lambda: play('Rock'))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = Button(btn_frame, text="📄 Paper", width=12, height=2, font=("Arial", 12), command=lambda: play('Paper'))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = Button(btn_frame, text="✂️ Scissors", width=12, height=2, font=("Arial", 12), command=lambda: play('Scissors'))
scissors_btn.grid(row=0, column=2, padx=10)

# Exit button
exit_btn = Button(window, text="❌ Quit Game", width=15, height=2, font=("Arial", 12), bg="red", fg="white", command=window.destroy)
exit_btn.pack(pady=20)

window.mainloop()
