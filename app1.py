import json
from difflib import get_close_matches



data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in  data:
        return data[word]
    
    #se houve digitação retorna sugere outra palavra compatível ao usuário
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
        if yn.capitalize() == "Y":
            return data[get_close_matches(word,data.keys())[0]]

        elif yn.capitalize() == "N":
            return "Word does not exist. Please double ckeck it."

        else:
            return "We didn't understand your entry."


    else:
        return "Word does not exist. Please double ckeck it."

word = input("Enter word:")

output = translate(word)
#se é uma lista imprime por linha/indice
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)