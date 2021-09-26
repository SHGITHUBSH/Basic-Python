#Guessing Game
Secret_Word = "Bomb"
Guess = input("Enter your guess word: ")
Guess_count = 0
Guess_limit = 3
Out_of_Guesses = False
while Guess != "Bomb" and not (Out_of_Guesses):
    if Guess_count < Guess_limit:
        Guess = (input("Guess again: "))
        Guess_count += 1
    else:
        Out_of_Guesses = True
if Out_of_Guesses:
    print("Out of Guesses. You Loose!")
else:
    print("You win!")
print("\n")