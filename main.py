import requests

def get_random_fact():
    return requests.get("https://cat-fact.herokuapp.com/facts/random").json()["text"]

def get_fact_by_id(pID):
    return requests.get("https://cat-fact.herokuapp.com/facts/" + pID).json()["text"]

while(True):
    print("Welcome to the cat fact generator.\n")
    selection = input("Please type 'q' to quit, 'r' for a random fact, or a cat fact ID for a specific _"
                      "fact. Example ID: 591f98803b90f7150a19c229\n")

    if selection.lower() == "r":
        print("\n" + get_random_fact() + "\n")
    elif selection.lower() == "q":
        break
    else:
        try:
            print("\n" + get_fact_by_id(selection) + "\n")
        except:
            print("Invalid ID.\n")
