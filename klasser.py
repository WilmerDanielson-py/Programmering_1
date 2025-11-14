import random as r


class weapon():
    def __init__(self, Rarity_W, Name_W, Type_W, Dmg_W, AtkSpeed_W, Range_W):
        self.Dmg_W = Dmg_W
        self.Range_W = Range_W
        self.AtkSpeed_W = AtkSpeed_W
        self.Type_W = Type_W
        self.Name_W = Name_W
        self.Rarity_W = Rarity_W

    def __str__(self):
        return f"You have these weapons in your inventory.\n This {self.Name_W} is a {self.Type_W} type weapon.\n Stats are;\n Damage: {self.Dmg_W}\n AtkSpeed: {self.AtkSpeed_W}\n Range: {self.Range_W} "
# weapon = weapon("rarity", "name","type","dmg","Atkspeed","range")
weapon_1 = weapon("Common", "Dagger", "Blade", "15", "20", "1")
weapon_2 = weapon("Uncommon", "Rapier", "Blade", "45", "10", "20")
weapon_3 = weapon("Rare", "Zweihander", "Blade", "60", "8", "25")
weapon_4 = weapon("Rare", "Shorre", "Gun", "250", "7", "30")
weapon_5 = weapon("Epic", "Ak 5", "Gun", "7", "25", "100")
weapon_6 = weapon("Legendary", "Golden Scar", "Gun", "10", "30", "150")
weapon_7 = weapon("Mythic", "Musket", "Gun", "2000", "1", "200")


inventory = [weapon_1]
# weapon_2, weapon_3, weapon_4, weapon_5, weapon_6, weapon_7

# for vapen in inventory:
#     print(vapen)
    
#     print("--------------------------------------------------------------------------------------")


class entity():
    def __init__(self, Name_E, Element_E, HP_E, Weak_E, STR_E, ):
        self.Name_E = Name_E
        self.STR_E = STR_E
        self.HP_E = HP_E
        self.Element_E = Element_E
        self.Weak_E = Weak_E

    def __str__(self):
        return f"You have encountered a {self.Element_E} type {self.Name_E} meaning its weak to {self.Weak_E} type attacks.\nIts stats are;\n Strenght: {self.STR_E}\n HP: {self.HP_E}\n"
# entity = entity("name","type","HP","weak","STR")
entity_1 = entity("Goblin","Normal","150","Blade and Gun","5")
entity_2 = entity("Zombie","Undead","170","Blade","10")
entity_3 = entity("Ravager","Tank","1000","Gun","3")
entity_4 = entity("Warlock","Berserker","70","Blade","49")
entity_5 = entity("Greger","Dark","1337","Blade","24")
entity_6 = entity("Bellman","Jester","inf","Joke","10")
entity_7 = entity("Johannes Thessén","Coder","5000","Sunlight","99")
entity_8 = entity(r" ρ * ( ∂u/∂t  +  (u · ∇)u )  =  -∇p  +  μ ∇²u  +  f","Physics","2500","Nikodesmos","35")

Enteties = [entity_1, entity_2, entity_3, entity_4, entity_5, entity_6, entity_7, entity_8]

# for monster in Enteties:
#     print(monster)
    
#     print("--------------------------------------------------------------------------------------")

class Player():
    def __init__(self, Name_P, HP_P, MaxHP_P, Level_P):
        self.Name_P = Name_P
        self.HP_P = HP_P
        self.MaxHP_P = MaxHP_P
        self.Level_P = Level_P

    def __str__(self):
        return f"Player Name: {self.Name_P}\n Player HP: {self.HP_P}/{self.MaxHP_P}\n Player Level: {self.Level_P}"
player_name = input("What is your name brave one?")
Player_1 = Player(f"{player_name}", 100, 100, 1)



def main():
    

    Entity_list = ["Goblin","Zombie","Ravager","Warlock","Greger"]
    Entity_in_room = r.choice(Entity_list)

    if Entity_in_room == "Goblin":
        print(entity_1)
        action = input("Do you wish to attack, or do you wish to escape? ")
        if action == "attack":
            for weapon in inventory:
                print(weapon)
            weapon_choice = input("What weapon do you wish to use?")

        elif action == "escape":
            print(escape)



    elif Entity_in_room == "Zombie":
        print(entity_2)
        action = input("Do you wish to attack, or do you wish to escape? ")
        if action == "attack":
            for weapon in inventory:
                print(weapon)
            weapon_choice = input("What weapon do you wish to use?")
            
        elif action == "escape":
            print(escape)


    elif Entity_in_room == "Ravager":
        print(entity_3)
        action = input("Do you wish to attack, or do you wish to escape? ")
        if action == "attack":
            for weapon in inventory:
                print(weapon)
            weapon_choice = input("What weapon do you wish to use?")
            
        elif action == "escape":
            print(escape)


    elif Entity_in_room == "Warlock":
        print(entity_4)
        action = input("Do you wish to attack, or do you wish to escape? ")
        if action == "attack":
            for weapon in inventory:
                print(weapon)
            weapon_choice = input("What weapon do you wish to use?")
            
        elif action == "escape":
            print(escape)


    elif Entity_in_room == "Greger":
        print(entity_5)
        action = input("Do you wish to attack, or do you wish to escape? ")
        if action == "attack":
            for weapon in inventory:
                print(weapon)
            weapon_choice = input("What weapon do you wish to use?")
            
        elif action == "escape":
            print(escape)



#ef draw_room(player_icon="P" , enemy_icon="E", Entity_in_room):
#    pass
