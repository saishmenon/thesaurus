import json

data = json.load(open("data.json"))

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

while word != "/end":
    word = input("Enter word: ")
    meaning = translate(word)
    print(meaning + "\n")
