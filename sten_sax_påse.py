import random 

def spela():
    
    val = ["sten", "sax", "påse"]
    hand = random.choice(val)
    # print(f"hand: {hand}")
    print("Välkommen till sten sax påse!")
    per1 = input("sten, sax eller påse?: ").lower()

    if hand == per1:
        print(f"Ai valde {hand}.")
        print("Lika.")
        # spelgång = input("Vill du köra igen?").lower()
    elif hand == "sten" and per1 == "påse":
        print(f"Ai valde {hand}.")
        print("Person 1 vann.")
        # spelgång = input("Vill du köra igen?").lower()
    elif per1 == "sten" and hand == "påse":
        print(f"Ai valde {hand}.")
        print("Ai vann.")
        # spelgång = input("Vill du köra igen?").lower()
    elif hand == "påse" and per1 == "sax":
        print(f"Ai valde {hand}.")
        print("Person 1 vann.")
        # spelgång = input("Vill du köra igen?").lower()
    elif per1 == "påse" and hand == "sax":
        print(f"Ai valde {hand}.")
        print("Ai vann.")
        # spelgång = input("Vill du köra igen?").lower()
    elif hand == "sax" and per1 == "sten":
        print(f"Ai valde {hand}.")
        print("Person 1 vann.")
        # spelgång = input("Vill du köra igen?").lower()
    elif per1 == "sax" and hand == "sten":
        print(f"Ai valde {hand}.")
        print("Ai vann.")
        # spelgång = input("Vill du köra igen?").lower()
    else:
        print("Kör om")
        
spela()