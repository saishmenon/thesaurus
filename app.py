import json
import difflib
from difflib import get_close_matches

# Loading json data into a variable called data
data = json.load(open("data.json"))

# Function to find the word and it's meaning from the JSON file
def translate(w):
    meaning = ""
    w = w.lower()
    
    # Condition to check if the string is empty
    if w.strip() == "":
        return "You entered an empty string. Try again..."
    
    # Condition to check if the word exists in the variable data
    elif w in data:
        print("Word exists!")
        string = data[w]
        for lettr in string:
            if lettr != "[" or lettr != "]":
                meaning += lettr
            else:
                meaning += ""
            return meaning

    # If all the above conditions are false then the word does not exist
    else:
        print("Word does not exist!")
        # Getting the top 3 close matches
        matches = get_close_matches(w,data.keys(),cutoff = 0.8)
        return matches

# Empty string for input
word = ""

# Loop to ask for a user input word
while word != "/end":
    word = input("Enter word: ")
    meaning = translate(word)
    if type(meaning) == str:
        print(meaning + "\n")
    else:
        print("Did you mean " + meaning[0] + "?")
