import json
import difflib

# Loading json data into a variable called data
data = json.load(open("data.json"))

# Function to find the word and it's meaning from the JSON file
def translate(w):
    meaning = ""
    w = w.lower()
    if w in data:
        print("Word exists!")
        str = data[w]
        for lettr in str:
            if lettr != "[" or lettr != "]":
                meaning += lettr
            else:
                meaning += ""
            return meaning
    else:
        return "Word does not exist!"

word = ""

# Loop to ask for a user input word
while word != "/end":
    word = input("Enter word: ")
    meaning = translate(word)
    print(meaning + "\n")
