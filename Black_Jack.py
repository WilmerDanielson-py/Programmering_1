# blackjack.py
# Enkel terminal-version av Blackjack
# Kör: python3 blackjack.py

import random

# --------- Grundläggande funktioner ----------
vals = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
farg = ['♠','♥','♦','♣']

def create_deck():
    """Skapar en standard 52-kortslek"""
    return [(v, s) for v in vals for s in farg]

def card_value(card):
    """Returnerar värdet för ett kort (ess returnerar 11 här, justeras senare)"""
    v = card[0]
    if v in ['J','Q','K']:
        return 10
    if v == 'A':
        return 11
    return int(v)

def hand_value(hand):
    """Beräkna bästa totala värdet för en hand (hanterar ess som 1 eller 11)"""
    total = sum(card_value(c) for c in hand)
    # Om total > 21, konvertera ess från 11 till 1 tills total <=21 eller inga ess kvar
    aces = sum(1 for c in hand if c[0] == 'A')
    while total > 21 and aces:
        total -= 10  # byter ett ess från 11 till 1
        aces -= 1
    return total

def show_hand(hand):
    """Formatera hand som sträng"""
    return ' '.join(f"{v}{s}" for v,s in hand)

# --------- Spel-logik ----------
def play_round(balance):
    deck = create_deck()
    random.shuffle(deck)

    # Insats
    while True:
        try:
            print(f"\nDin saldo: {balance} kr")
            bet = int(input("Ange insats (heltal, 0 för att avbryta spelet): "))
            if bet == 0:
                return balance, False  # spelaren vill sluta
            if bet < 0 or bet > balance:
                print("Ogiltig insats. Sätt en summa mellan 1 och ditt saldo.")
                continue
            break
        except ValueError:
            print("Skriv ett heltal för insatsen.")

    # Dela kort: 2 till spelare, 2 till dealer (en dold)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Spelarens tur
    while True:
        print(f"\nDina kort: {show_hand(player_hand)}  (Poäng: {hand_value(player_hand)})")
        print(f"Dealerns synliga kort: {dealer_hand[0][0]}{dealer_hand[0][1]}  (ett kort dolt)")
        if hand_value(player_hand) == 21:
            print("Blackjack! Du har 21.")
            break
        move = input("Vill du (h)it eller (s)tand? ").strip().lower()
        if move == 'h' or move == 'hit':
            player_hand.append(deck.pop())
            if hand_value(player_hand) > 21:
                print(f"\nDu drog {player_hand[-1][0]}{player_hand[-1][1]} och blev över 21 ({hand_value(player_hand)}).")
                break
            else:
                continue
        elif move == 's' or move == 'stand':
            break
        else:
            print("Svara 'h' för hit eller 's' för stand.")

    player_total = hand_value(player_hand)
    if player_total > 21:
        print("Du förlorade rundan (bust).")
        balance -= bet
        return balance, True

    # Dealerns tur (följer enkla regler: drar till 17 eller mer)
    print("\nDealerns tur:")
    print(f"Dealerns kort: {show_hand(dealer_hand)}  (Poäng: {hand_value(dealer_hand)})")
    while hand_value(dealer_hand) < 17:
        drawn = deck.pop()
        dealer_hand.append(drawn)
        print(f"Dealern drar {drawn[0]}{drawn[1]} — nu {hand_value(dealer_hand)} poäng")
    dealer_total = hand_value(dealer_hand)

    # Visa slutresultat
    print("\n--- Resultat ---")
    print(f"Dina kort:   {show_hand(player_hand)}  = {player_total}")
    print(f"Dealerns kort:{show_hand(dealer_hand)}  = {dealer_total}")

    # Bestäm vinnare
    if dealer_total > 21 or player_total > dealer_total:
        # Blackjack (21 med två kort) betalar 3:2
        if player_total == 21 and len(player_hand) == 2:
            win = int(1.5 * bet)
            print(f"Grattis! Blackjack — du vinner {win} kr.")
            balance += win
        else:
            print(f"Du vinner {bet} kr!")
            balance += bet
    elif player_total == dealer_total:
        print("Push — oavgjort. Insatsen återbetalas.")
    else:
        print(f"Du förlorar {bet} kr.")
        balance -= bet

    return balance, True

# --------- Huvudprogram ----------
def main():
    print("Välkommen till Blackjack! (skriv '0' som insats för att sluta)")
    balance = 500  # startsaldo
    playing = True
    while playing and balance > 0:
        balance, cont = play_round(balance)
        if not cont:
            print("Tack för att du spelade! Hej då.")
            break
        if balance <= 0:
            print("Du är bankrutt. Spelet är slut.")
            break
        # Fråga spela vidare
        svar = input("\nVill du spela en runda till? (j/n) ").strip().lower()
        if svar not in ('j','ja','y','yes'):
            playing = False
            print("Tack för spelet — välkommen tillbaka!")
    print(f"Slutsaldo: {balance} kr")

if __name__ == "__main__":
    main()
