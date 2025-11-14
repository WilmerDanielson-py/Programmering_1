import random
slumptal = random.randint(1, 11)
gissning = 0
antal_gissningar = 0
max_gissningar = 3
spelpengar = 5000
spel_igång = True
def spela():
    print("Välkommer till Gissa Nummret!")
    global spelpengar, spel_igång
    while spelpengar > 0 and spel_igång == True:
        antal_gissningar = 0
        print("Du har 3 gissningar att gissa talet, talet är mellan 1-10.")
        satsning = int(input(f"Hur mycket vill du satsa? Du har {spelpengar}."))
        # print(f"spelpengar : {spelpengar}, satsning : {satsning}")
        while satsning > spelpengar:
            print(f"Du har inte så mycket pengar, välj en summa under {spelpengar}")
            satsning = int(input("Ge mig en ny satsning: "))
                
        if satsning == spelpengar:
            print("Du går all in alltså?, då får vi hålla tummarna...")
        else:
            print(f"Okej, du bettar alltså {satsning}")

        
        # print(f"antal_gissningar : {antal_gissningar}, max_gissningar : {max_gissningar}")
        while antal_gissningar < max_gissningar:
            gissning = int(input("Ge mig ditt tal"))
            if slumptal == gissning:
                spelpengar = spelpengar + satsning*2
                print(f"Du gissade rätt!, du har nu {spelpengar} att spela för!")
                break
            else:
                antal_gissningar += 1
            
                print("Fel! Gissa igen!") 
                
            if antal_gissningar == max_gissningar:
                print("Du förlorade hahaha!")
                print("Ge mig allt du satsade!")
                spelpengar = spelpengar - satsning
                print(f"Du har nu {spelpengar} att spela för!")
                if spelpengar == 0:
                    print("Slut på pengar, spelet avslutas")
                    break
                     

            if antal_gissningar == max_gissningar:
                spel_igång = input("Vill du avsluta? ja eller nej?").lower()
                if spel_igång == "ja":
                        print("Ok, spelet avslutas.")
                        spel_igång = False
                elif spel_igång == "nej":
                        print("Spelet fortsätter!")
                        spel_igång = True
