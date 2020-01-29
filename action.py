from characters import Wizard
from characters import Archer
from characters import Warrior
from characters import Elfewizard
from characters import Elfearcher
from characters import Elfewarrior
from characters import Dwarfwizard
from characters import Dwarfarcher
from characters import Dwarfwarrior


def main():
    merlin = Elfewizard ("merlin")
    miniwizard= Dwarfwizard ( "miniwizard")
    oubien = Elfearcher ( "oubien")
    minarcher=Dwarfarcher("minarcher")
    bourrin= Dwarfwarrior ( "Bourrin")
    grosbourrin=Elfewarrior("grosbourrin")

    while merlin._life_point or miniwizard._life_point or oubien._life_point or minarcher._life_point or bourrin._life_point or grosbourrin._life_point >=0:

            character_attack = input("qui attaque :")
            if character_attack == "merlin":
                weapon, attack_points = merlin.attack()
            if character_attack == "oubien":
                weapon , attack_points = oubien.attack()
            if character_attack== "bourrin":
                weapon , attack_points = bourrin.attack()
            if character_attack == "miniwizard":
                 weapon , attack_points= miniwizard.attack()
            if character_attack== "minarcher":
                weapon , attack_points= minarcher.attack()
            if character_attack == "grosbourrin":
                weapon , attack_points = grosbourrin.attack()



            character_defend = input ( " qui defend :")
            if character_defend == "merlin":
                merlin.defend (weapon, attack_points)
            if character_defend == "oubien":
                oubien.defend ( weapon, attack_points)
            if character_defend == "bourrin":
                bourrin.defend( weapon,attack_points)
            if character_defend == "miniwizard":
                miniwizard.defend ( weapon,attack_points)
            if character_defend == "minarcher":
                minarcher.defend ( weapon,attack_points)
            if character_defend == "grosbourrin":
                grosbourrin.defend (weapon,attack_points)

if __name__ == '__main__':
     main()








