import random
import tkinter as tk

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def guess_f():
    letter = letter_inp.get().lower()
    letter_inp.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Invalid guess. Enter a single letter.")
        return

    if letter in guesses:
        result_label.config(text="You have already guessed this letter. Try another letter.")
        return

    guesses.append(letter)

    if letter in selected_word:
        index = 0
        for i in range(len(selected_word)):
            if selected_word[i] == letter:
                predicted_w[i] = letter
                index += 1

        guess_label.config(text="The predicted word: " + " ".join(predicted_w))

        if "_" not in predicted_w:
            result_label.config(text="Congrats! You guessed right. The chosen word: " + selected_word)
            guess_buton.config(state=tk.DISABLED)
            letter_inp.config(state=tk.DISABLED)
    else:
        attempts_number[0] -= 1
        result_label.config(text="Wrong guess. Number of remaining attempts: " + str(attempts_number[0]))

        if attempts_number[0] == 0:
            result_label.config(text="You have no more right to guess. The right word: " + selected_word)
            guess_buton.config(state=tk.DISABLED)
            letter_inp.config(state=tk.DISABLED)

def newgame_f():
    global selected_word, predicted_w, guesses, attempts_number

    selected_word = random.choice(word_list)
    word_length = len(selected_word)
    predicted_w = ["_"] * word_length
    guesses = []
    attempts_number = [5]

    guess_label.config(text="The predicted fruit:  " + " ".join(predicted_w))
    result_label.config(text="")
    guess_buton.config(state=tk.NORMAL)
    letter_inp.config(state=tk.NORMAL)
    letter_inp.focus()

word_list = ["apple", "orange","banana", "melon", "strawberry"]
selected_word = random.choice(word_list)
word_length = len(selected_word)
predicted_w = ["_"] * word_length
guesses = []
attempts_number = [5]

scrwin = tk.Tk()
scrwin.title("The Word Guessing Game ")

guess_label = tk.Label(scrwin, text="The predicted fruit:  " + " ".join(predicted_w))
guess_label.pack()

letter_inp = tk.Entry(scrwin)
letter_inp.pack()
letter_inp.focus()

guess_buton = tk.Button(scrwin, text="Guess", command=guess_f)
guess_buton.pack()

result_label = tk.Label(scrwin, text="")
result_label.pack()

newgame_f_buton = tk.Button(scrwin, text="New Game", command=newgame_f)
newgame_f_buton.pack()

scrwin.mainloop()
