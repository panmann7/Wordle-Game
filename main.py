def main():
    filename = input("Enter the name of the word file: ")
    play_game(filename)

def play_game(filename):
    words = get_words(filename)

    greeting()
    instructions()
    correct_attempts_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    win_count = 0
    game_round = 0
    
    play_again_input = True
    while play_again_input == True:
        puzzle_word = get_random_word(words)
        game_round += 1
        
        round_attempt = play_round(puzzle_word, game_round)
        if round_attempt[1] == True:
            correct_attempts_dict[round_attempt[0]] += 1
            win_count += 1
            
        play_again_input = play_again()

    summary(win_count, game_round, correct_attempts_dict)
    
def get_words(filename):
    input_file = open(filename, "r")
    words = input_file.read().split()
    input_file.close()

    return words

def greeting():
    name = input("Please enter your name: ")
    print()  
    print(f"Welcome to Wordle 101 {name}")
    print()

def instructions():
    print("========================================================================")
    print("                                 Rules")
    print("You have 6 guesses to figure out the solution.")
    print("All solutions are words that are 5 letters long.")
    print("Words may include repeated letters.")
    print("Letters that have been guessed correctly are displayed in uppercase.")
    print("Letters that are in the word but have been guessed in the wrong location")
    print("are displayed in lowercase.")
    print("========================================================================")
    print()
    print()

def play_round(word, game_round):
    print(f"Round: {game_round}")
    print()
    
    for i in range(1, 7):
        player_guess = get_player_guess(i)
        update_game_state(player_guess, word)
        print()

        if player_guess == word:
            print(f"Success! The word is {word}!")
            return (i, True)
        
    print(f"Better luck next time! The word is {word}!")
    return (6, False)

def update_game_state(guess, word):
    game_state = ["_", "_", "_", "_", "_"]
    
    for i in range(len(guess)):
        if guess[i] == word[i]:
            game_state[i] = guess[i].upper()
    for i in range(len(guess)):
        is_letter_count_valid = game_state.count(guess[i].lower()) + game_state.count(guess[i].upper()) < word.count(guess[i])
        if guess[i] in word and game_state[i] != guess[i].upper() and is_letter_count_valid:
            game_state[i] = guess[i]
            
    print(" ".join(game_state))
    
def get_player_guess(guess_num):
    print(f"Guess {guess_num}: ")
    print()
    
    guess = input("Please enter your guess: ")
    
    while len(guess) != 5 or guess.isalpha() == False:
        guess = input("Your guess must have 5 letters: ")

    return guess.lower()

def play_again():
    print()
    play_again_input = input("Please enter 'Y' to continue or 'N' to stop playing: ")

    while play_again_input != "Y" and play_again_input != "N":
        print("Only enter 'Y' or 'N'!")
        play_again_input = input("Please enter 'Y' to continue or 'N' to stop playing: ")
    
    print()
    return play_again_input == "Y"

def summary(win_count, game_round, correct_attempts_dict):
    print("========================================================================")
    print("                                Summary")
    print(f"Win percentage: {get_win_percentage(win_count, game_round)}%")
    print("Win Distribution: ")
    print_bar_chart(correct_attempts_dict)
    print("========================================================================")

def print_bar_chart(data_dict):
    for key in data_dict:
        hashtag_amount = data_dict[key] * "#"
        print(f"{key}|{hashtag_amount}{data_dict[key]}")
        
def get_win_percentage(win_num, game_round):
    win_percentage = round((win_num / game_round) * 100)
    return win_percentage