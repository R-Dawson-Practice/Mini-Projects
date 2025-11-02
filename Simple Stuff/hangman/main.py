import random

words = ["beekeeper", "camel", "stuff"]

def init_display(word):
    return ["_"] * len(word) ##Equivalent to for and append

def guess():
    print ("Guess a letter")
    guess = ""
    while True:
        guess = input().strip()
        if guess == "" or not guess.isalpha():
            guess = ""
            print("Enter a letter")
            continue
        return guess
    
def check(letter, word, chosen_word):
    matches = 0
    for i in range(len(chosen_word)):
        if chosen_word[i] == letter:
            word[i] = letter
            matches += 1
    return matches


def play_game(chosen_word, lives):
    display_chosen_word = init_display(chosen_word)
    correct = 0

    while lives > 0 and "_" in display_chosen_word:
        print(display_chosen_word)
        letter = guess()
        matches = check(letter, display_chosen_word, chosen_word)
        correct = correct + matches
        if matches == 0:
            lives -=1 
            print(lives)
    print(display_chosen_word)
    if "_" not in display_chosen_word:
        return True
    return False


def main():
    chosen_word = words[random.randint(0, len(words)-1)]
    lives = 5
    win = play_game(chosen_word, lives)
    if win:
        print("Win")
    else:
        print("Lose")

if __name__ == "__main__":
    main()