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

    # If there is a close match
    elif len(get_close_matches(w,data.keys())) > 0:
        
        # Getting the top 3 matches
        matches = get_close_matches(w,data.keys(),cutoff = 0.8)
        yn = input("Did you mean " + matches[0] + "? (Y/N): ")
        if yn == "y" or yn == "Y":
            # Returning the meaning of the first match
            string = data[matches[0]]
            for lettr in string:
                if lettr != "[" or lettr != "]":
                    meaning += lettr
                else:
                    meaning += ""
            return meaning
        elif yn == "n" or yn == "N":
            return "The word does not exist. Please double check or enter a different word."
        else:
            return "Invalid Input!"
            
    # If all the above conditions are false then the word does not exist
    else:
        return "Word does not exist!"
            
# Empty string for input
word = ""

# Loop to ask for a user input word
while word != "/end":
    word = input("Enter word: ")
    meaning = translate(word)
    print(meaning)