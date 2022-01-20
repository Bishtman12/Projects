# Features Need to be added -> 1. Score Counter 3. Category Wise Split
import random
import requests
from pprint import pprint

def getquiz():
    url = requests.get("https://api.trivia.willfry.co.uk/questions?limit=10")
    quiz = url.json()
    return quiz  # Quiz contains everything in the json format

def hmap(o):
    hmap = {}
    for i in range(len(o)):
        hmap[i + 1] = [o[i]]
    return hmap

def user():
    # o -> options list
    # a -> Correct Answer
    # q -> Question
    x = int(input("Which Mode Do you want to Play?\n1. 5-Questions\n2. 10-Questions\n"))
    if x == 1:
        call = logic(5)
    elif x == 2:
        call = logic(10)
    else:
        print("Invalid Input")
def logic(count):
    o = []
    fox = getquiz()
    for x in range(count):
        # getting the questions from the json format
        q = fox[x]['question']
        a = fox[x]['correctAnswer']
        options = fox[x]['incorrectAnswers']
        print(a)
        print(f"Question-{q}")

        o.append(a)
        for i in range(3):
            o.append(options[i])
        t = len(o)
        random.shuffle(o)
        for j in range(4):
            print(f"{j + 1}.{o[j]}")
            t = t - 1
        mapping = hmap(o)
        choice = int(input("\nChoose You Option\n"))
        find = mapping[choice]
        if find[0] in a :
            print("\n**Bingo!Correct Answer**\n")
        else:
            print("\n**Neh!Wrong Choice**\n")

user()


