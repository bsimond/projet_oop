class Animal:

    hairs_type=""
    life_exp=0

    def __init__(self ,name,weight,color,age):

        self.name = name
        self.weight = weight
        self.color= color
        self.age= age

    def talk(self):

        return self.sound

    def get_diet(self ):
        return self.liste_aliment

    def eat(self, aliment):
        if aliment in self.liste_aliment:
            self.weight += self.weight*0.05
        else:
            print("aliment pas mangé")

    def _get_age(self):
        return self._age

    def _set_age (self , value):
        if value < 0 or value > self.life_exp:
            raise Exception()
        else:
              self._age=value


    age = property (_get_age,_set_age)








class Cat(Animal):
    hairs_type = "cours"
    life_exp = 15
    liste_aliment=["poisson" , "sourie"]
    sound= "miaou"




class Snail ( Animal):
    hairs_type = "coquille"
    life_exp = 2
    liste_aliment=["salade", "carotte"]
    sound = "shuut"


class Snake ( Animal):
    hairs_type = "chauve"
    life_exp = 10
    liste_aliment=["sourie","oiseau"]



momo=Cat("momo" , 15 ,"gris",10)
print(momo.name)
print ( momo.weight)
print(momo.color)
print(momo.talk())
momo.eat("poisson")
print(momo.weight)
print(momo.get_diet())
momo.eat('elephant')

asgard=Snake ( "asgard", 1 ,"vert",2)
print(asgard.name)