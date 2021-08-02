import json

data = json.load(open("data.json"))

def translate(word):
    if word in  data:
        return data[word]

    else:
        return "Word does not exist."

word = input("Enter word:")

print(translate(word))