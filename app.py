import json
import difflib
from difflib import get_close_matches

# Loading json data into a variable called data
data = json.load(open("data.json"))

# Function to find the word and it's meaning from the JSON file
def translate(w):
    w = w.lower()
    
    # Condition to check if the string is empty
    if w.strip() == "":
        return "You entered an empty string. Try again..."
    
    # Condition to check if the word exists in the variable data
    elif w in data:
        return data[w]

    # Condition to check for proper nouns such as names of Cities or Countries (Paris, Seattle etc.)
    elif w.title() in data:
        return data[w.title()]

    # Condition to check for acronyms such as USA, NATO etc.
    elif w.upper() in data:
        return data[w.upper()]

    # If there is a close match
    elif len(get_close_matches(w,data.keys())) > 0:
        # Getting the top 3 matches
        matches = get_close_matches(w,data.keys(),cutoff = 0.8)
        yn = input("Did you mean " + matches[0] + "? (Y/N): ")
        if yn == "y" or yn == "Y":
            return data[matches[0]]
        elif yn == "n" or yn == "N":
            return "The word may not exist. Please double check or enter a different word."
        else:
            return "Invalid Input!"
            
    # If all the above conditions are false then the word does not exist
    else:
        return "Word does not exist!"
            
# Empty string for input
word = ""

# Loop to ask for a user input word
# while word != "/end":
#     word = input("Enter word: ")
#     meaning = translate(word)
#     print(meaning)

word = input("Enter word: ")
meaning = translate(word)
if type(meaning) == str:
    print(meaning)

elif type(meaning) == list:
    for item in meaning:
        print(item)