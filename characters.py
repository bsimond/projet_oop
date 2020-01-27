from random import randint


class Character:
    max_life_point = 12

    def __init__(self, name):
        self.name = name
        self.life_point = self.max_life_point
        self.height = randint(170, 190)
        self.weight = randint(70, 90)

    def dices_roll(self):
        magic = randint(1, self.magicdice)
        sword = randint(1, self.sworddice)
        bow = randint(1, self.bowdice)
        resultsdices = [["magic", magic], ["sword", sword], ["bow", bow]]
        return resultsdices

    def attack(self):
        dices_roll = self.dices_roll()
        winnerdices = sorted(dices_roll, key=lambda x: x[1], reverse=True)
        results = winnerdices[0]
        print(str(self.name) + " utilise " + str(results))
        return results

    def defend(self, weapon, attack_point, ):
        dices_roll = dict(self.dices_roll())
        defendweapon = dices_roll[weapon]
        difference = attack_point - defendweapon
        print(str(self.name) + " se defend en faisant " + str(defendweapon))

        if attack_point > defendweapon:
            self.life_point = self.life_point - difference
            print("il reste  à " + str(self.name) + " " + str(self.life_point) + "  point de vie")
            return self.life_point
        if attack_point <= defendweapon:
            self.life_point = self.life_point
            print(str(self.name) + " a toujours " + str(self.life_point))
            return self.life_point


class Wizard(Character):
    magicdice = 12
    sworddice = 8
    bowdice = 10

    def attack(self):

        weapon, attack_point = super().attack()
        magicdammage = randint(1, self.magicdice)

        if attack_point < magicdammage:
            return "magic", magicdammage
        elif weapon == "sword":
            bonussword = (self.height + self.weight)// 40
            totalsword = bonussword + attack_point
            print(totalsword)
            return "sword", totalsword
        elif weapon == "bow":
            bonusbow = (self.height - 170) % 3
            totalbow = bonusbow + attack_point
            print(totalbow)
            return "bow", totalbow
        return weapon ,attack_point


class Archer(Character):
    magicdice = 10
    sworddice = 8
    bowdice = 10

    def attack(self):
        weapon, attack_point = super().attack()
        if weapon == "magic":
           bonusmagic= self.weight//20
           totalmagic= attack_point + bonusmagic + 1
           print(totalmagic)
           return "magic" , totalmagic
        elif weapon == "sword":
            bonussword= self.height//40
            totalsword = attack_point + bonussword +1
            print(totalsword)
            return "sword", totalsword
        return weapon , attack_point


class Warrior(Character):

    max_life_point = 16
    magicdice = 8
    sworddice = 12
    bowdice = 10


    def attack(self):
        weapon, attack_point = super().attack()
        if weapon == "magic":
            bonusmagic=self.weight//30
            totalmagic= bonusmagic + attack_point
            print(totalmagic)
            return "magic",totalmagic
        elif weapon=="bow":
            bonusbow= (self.height -170)%3
            totalbow= bonusbow + attack_point
            print(totalbow)
            return "bow",totalbow
        return weapon ,attack_point