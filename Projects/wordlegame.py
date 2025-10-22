import random

def load_words_per_line(wordlewords):
    """Loads words from a text file where each word is on a new line."""
    words = []
    try:
        with open(wordlewords, 'r') as file:
            for line in file:
                word = line.strip()  # Remove leading/trailing whitespace and newline characters
                if word:  # Only add non-empty strings
                    words.append(word)
        return words
    except FileNotFoundError:
        print(f"Error: The file '{wordlewords}' was not found.")
        return []


wordlist=load_words_per_line("Projects/wordlewords.txt")
hidden_word = random.choice(wordlist)
hidden_word = hidden_word.lower()


print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"


        # 2 letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
        
        # 3 letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
        
        # 4 letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
        
        # 5 letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

 
print(f"the word was {hidden_word}")
print(f"You used {i+1} guesses")