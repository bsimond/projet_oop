from characters import Wizard
from characters import Archer
from characters import Warrior

def main():
    merlin = Wizard ("Merlin")
    oubien = Archer ( "oubien")
    bourrin= Warrior ( "Bourrin")


    character_attack = input("qui attaque :")
    if character_attack == "merlin":
        weapon, attack_points = merlin.attack()
    if character_attack == "oubien":
        weapon , attack_points = oubien.attack()
    if character_attack== "bourrin":
        weapon , attack_points = bourrin.attack()

    character_defend = input ( " qui defend :")
    if character_defend == "merlin":
        merlin.defend(weapon, attack_points)
    if character_defend == "oubien":
        oubien.defend ( weapon, attack_points)
    if character_defend == "bourrin":
        bourrin.defend( weapon,attack_points)


if __name__ == '__main__':
     main()








