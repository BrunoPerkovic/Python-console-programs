
guess_word = "Lewis Hamilton"
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = ""
print("Note: Please use capital first letter in both first name and last name!")
while guess != guess_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Who has the most wins in F1 history? ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("YOU LOSE! ")
    if guess == guess_word:
        print("Next question!")


guess_word = "Sebastian Vettel"
guess = ""
guess_count = 0
while guess != guess_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Who is the youngest pole sitter in F1 history? ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("YOU LOSE! ")
    if guess == guess_word:
        print("Next question! ")



guess_word = "Michael Schumacher"
guess = ""
guess_count = 0
while guess != guess_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Who has the most fastest laps in F1 history? ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("YOU LOSE! ")
    if guess == guess_word:
        print("Next question! ")

guess_word = 1
guess = ""
guess_count = 0
while guess != guess_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("How many female drivers scored at least a point in F1 history? "))
        guess_count += 1
    else:
        out_of_guesses = True
        print("YOU LOSE! ")
    if guess == guess_word:
        print("Next question! ")


guess_word = ["Hill", "Rosberg"]
guess = ""
guess_count = 0
while not (guess in guess_word) and not (out_of_guesses):
    if guess_count < guess_limit:
        print("Note: Please use surname of the family! ")
        guess = input("Which family duo won F1 world titles? ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("YOU LOSE! ")
    if guess in guess_word:
        guess_word.remove(guess)
        guess_count = 0
        guess2 = ""
        while not (guess2 in guess_word) and not (out_of_guesses):
            if guess_count < guess_limit:
                guess2 = input("Which family duo won F1 world titles? ")
                guess_count += 1
            else:
                out_of_guesses = True
                print("YOU LOSE! ")
            if guess2 in guess_word:
                out_of_guesses = True
                print("YOU WIN! Congratulations! ")