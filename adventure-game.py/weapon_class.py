
from colors import *
from entity_class import *

# Här skapas vapen
class weapon():
    def __init__(self, Rarity_W, Name_W, Type_W, Dmg_W, AtkSpeed_W, Range_W, Hits_W):
        self.Dmg_W = Dmg_W
        self.Range_W = Range_W
        self.AtkSpeed_W = AtkSpeed_W
        self.Type_W = Type_W
        self.Name_W = Name_W
        self.Rarity_W = Rarity_W
        self.Hits_W = Hits_W
        
# Här skapas en strängrepresentation av vapnet
    def __str__(self):
        return f"\n{self.Name_W}\nThis {self.Rarity_W} {self.Name_W} is a {self.Type_W} type weapon.\n   Stats are:\n   Damage: {self.Dmg_W}\n   AtkSpeed: {self.AtkSpeed_W}\n   Range: {self.Range_W} "

# Här skapas vapenobjekt
# weapon = weapon("rarity", "name","type","dmg","Atkspeed","range","max hits")
weapon_1 = weapon(BLACK("Common"), "Dagger", Blade, 15 , 20, 1, 1)
weapon_2 = weapon(GREEN("Uncommon"), "Rapier", Blade, 45, 10, 20, 1)
weapon_3 = weapon(BLUE("Rare"), "Zweihander", Blade, 25, 8, 25, 3)
weapon_4 = weapon(BLUE("Rare"), "Shorre", Gun, 20, 7, 30, 5)
weapon_5 = weapon(MAGENTA("Epic"), "Ak 5", Gun, 4, 25, 100, 20)
weapon_6 = weapon(YELLOW("Legendary"), "Golden Scar", Gun, 7, 30, 150, 20)
weapon_7 = weapon(RED("Mythic"), "Musket", Gun, 300, 1, 200, 1)





# Här skapas en lista för spelarens vapen-inventory
weapon_inventory = [weapon_1]

# Här skapas en funktion för att applicera vapenmodifierare baserat på fiendens svaghet
def apply_weapon_modifier(weapon, enemy):
    
    if weapon.Type_W == Blade and "Blade" in enemy.Weak_E:
        weapon.Dmg_W = int(weapon.Dmg_W * 1.5)
    elif weapon.Type_W == Gun and "Gun" in enemy.Weak_E:
        weapon.Dmg_W = int(weapon.Dmg_W * 1.5)
    else:
        weapon.Dmg_W = int(weapon.Dmg_W * 0.75)