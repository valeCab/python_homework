#Task 4 Closure Practice
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""
        all_guessed = True

        for char in secret_word: 
            if char in guesses: 
                display_word += char 
            else: 
                display_word += "_"
                all_guessed = False

        print(display_word)
        return all_guessed
    return hangman_closure

word = input("Secret word:").lower()
game = make_hangman(word)
finished = False

while not finished:
    guess = input("Guess a letter: ").lower()
    finished = game(guess)