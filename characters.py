from random import randint


class Character:
    _max_life_point = 12
    bowbonus=0
    swordbonus=0

    def __init__(self, name):
        self.name = name
        self._life_point =self._max_life_point
        self._height=randint(170,190)
        self._weight = randint(70, 90)
    def _get_height (self):
        return self._height
    def _get_weight(self):
        return self._weight


    height = property( _get_height)
    weight = property(_get_weight)

    def dices_roll(self):
        magic = randint(1, self.magicdice)
        sword = randint(1, self.sworddice)
        bow = randint(1, self.bowdice)
        resultsdices = [["magic", magic], ["sword", sword], ["bow", bow]]
        return resultsdices

    def attack(self):
        dices_roll = self.dices_roll()
        winnerdices = sorted(dices_roll, key=lambda x: x[1], reverse=True)
        weapon, attack_points= winnerdices[0]
        if weapon == "sword":
            attack_points = attack_points + self.swordbonus
            print(str(self.name) + " utilise " + str(weapon)+" et fait un " + str(attack_points))
            return weapon , attack_points
        if weapon == " bow":
            attack_points= attack_points +self.bowbonus
            print(str(self.name) + " utilise " + str(weapon)+" et fait un " + str(attack_points))
            return weapon, attack_points
        else :
            print(str(self.name) + " utilise " + str(weapon)+" et fait un " + str(attack_points))
            return weapon, attack_points

    def defend(self, weapon, attack_point, ):
        dices_roll = dict(self.dices_roll())
        defendweapon = dices_roll[weapon]
        difference = attack_point - defendweapon
        print(str(self.name) + " se defend en faisant " + str(defendweapon))

        if attack_point > defendweapon:
            self._life_point = self._life_point - difference
            print("il reste  à " + str(self.name) + " " + str(self._life_point) + "  point de vie")
            return self._life_point
        if attack_point <= defendweapon:
            self._life_point = self._life_point
            print(str(self.name) + " a toujours " + str(self._life_point))
            return self._life_point


class Wizard(Character):
    magicdice = 12
    sworddice = 8
    bowdice = 10

    def attack(self):
        weapon, attack_points = super().attack()
        magicdammage = randint(1, self.magicdice)
        if attack_points < magicdammage:
            return "magic", magicdammage
        elif weapon == "sword":

            bonussword = (self._height + self._weight)// 40
            totalsword = bonussword + attack_points
            print(totalsword)
            return "sword", totalsword
        elif weapon == "bow":
            bonusbow = (self._height - 170) % 3
            totalbow = bonusbow + attack_points
            print(totalbow)
            return "bow", totalbow
        return weapon ,attack_points


class Archer(Character):
    magicdice = 10
    sworddice = 8
    bowdice = 10

    def attack(self):
        weapon, attack_points = super().attack()
        if weapon == "magic":
           bonusmagic= self._weight//20
           totalmagic= attack_points + bonusmagic + 1
           print(totalmagic)
           return "magic" , totalmagic
        elif weapon == "sword":
            bonussword= self._height//40
            totalsword = attack_points + bonussword +1
            print(totalsword)
            return "sword", totalsword
        return weapon , attack_points


class Warrior(Character):

    _max_life_point = 16
    magicdice = 8
    sworddice = 12
    bowdice = 10


    def attack(self):
        weapon, attack_points = super().attack()
        if weapon == "magic":
            bonusmagic=self._weight//30
            totalmagic= bonusmagic + attack_points
            print(totalmagic)
            return "magic",totalmagic
        elif weapon=="bow":
            bonusbow= (self._height -170)%3
            totalbow= bonusbow + attack_points
            print(totalbow)
            return "bow",totalbow
        return weapon ,attack_points


class Dwarf:

    swordbonus=2



class Elfe:

    bowbonus=2


class Dwarfwizard ( Dwarf , Wizard):
    pass

class Dwarfarcher ( Dwarf , Archer):
    pass

class Dwarfwarrior ( Dwarf , Warrior):
    pass

class Elfewizard ( Elfe, Wizard) :
    pass

class Elfearcher ( Elfe , Archer):
    pass

class Elfewarrior (Elfe , Warrior) :
    pass

