from random import randint

class Wizard:

    magicdice=12
    sworddice=8
    bowdice=10



    def __init__(self,name):
         self.name = name

    def dices_roll(self,):
        magic = randint(1, self.magicdice)
        sword = randint(1, self.sworddice)
        bow = randint(1, self.bowdice)
        resultsdices = [["magic", magic], ["sword", sword], ["bow", bow]]
        return resultsdices

    def attack (self):
         dices_roll= self.dices_roll()
         winnerdices= sorted( dices_roll ,key=lambda x:x[1], reverse=True )
         results=winnerdices[0]
         print(results)
         return results


    def defend ( self, weapon, attack_point):
        dices_roll=dict(self.dices_roll())
        defendweapon = dices_roll[weapon]
        difference = attack_point - defendweapon
        print(dices_roll)
        print(difference)







merlin = Wizard ("Merlin")
print ( merlin.name)

merlin.dices_roll()

weapon, attack_points = merlin.attack()


merlin.defend(weapon, attack_points)











