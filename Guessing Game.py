
secret_word = "house"
guess = ""
counter = 0
guess_limit = 5
out_of_chances = False

while guess != secret_word and not out_of_chances:
    if counter < guess_limit:
        guess = input("Enter guess: ")
        counter += 1
    else:
        out_of_chances = True

if out_of_chances:
    print("You lost!")
else:
    print("You won!")
