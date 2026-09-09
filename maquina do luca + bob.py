from enum import Enum
class JucaState(Enum):
    WORKING = 1
    EATING = 2
    SLEEPING = 3


class Juca:
    def __init__(self):
        self.state = JucaState.WORKING
        self.hunger = 0
        self.fatigue = 0

    def update(self):
        if self.state == JucaState.WORKING:
            self.hunger += 2
            self.fatigue += 5

        elif self.state == JucaState.EATING:
            self.hunger -= 5

        elif self.state == JucaState.SLEEPING:
            self.hunger += 1
            self.fatigue -= 10

        self.hunger = max(self.hunger, 0)
        self.fatigue = max(self.fatigue, 0)

        print("  JUCA:")

        if self.state == JucaState.WORKING:
            print("  Trabalhando...")

        elif self.state == JucaState.EATING:
            print("  Comendo...")

        elif self.state == JucaState.SLEEPING:
            print("  Dormindo...")

        print("  Fome:", self.hunger)
        print("  Cansaço:", self.fatigue)

        if self.state == JucaState.WORKING:

            if self.fatigue > 50:
                self.state = JucaState.SLEEPING
                print("  Bateu um sono...")

            elif self.hunger > 10:
                self.state = JucaState.EATING
                print("  Bateu uma fome...")

        elif self.state == JucaState.EATING:

            if self.hunger <= 0:
                self.hunger = 0

                print("  Ufa! Já estou cheio...")

                self.state = JucaState.WORKING
                print("  Hora de ir para o trabalho!")

        elif self.state == JucaState.SLEEPING:

            if self.fatigue <= 0:
                self.fatigue = 0

                if self.hunger <= 10:
                    self.state = JucaState.WORKING
                    print("  Hora de ir para o trabalho!")

                else:
                    self.state = JucaState.EATING
                    print("  Bateu uma fome...")

class BobState(Enum):
    COOKING = 1
    CLEANING = 2


class Bob:
    def __init__(self):
        self.state = BobState.COOKING
        self.cookingProgress = 0
        self.mess = 0

    def update(self):
        if self.state == BobState.COOKING:
            self.cookingProgress += 3
            self.mess += 2

        elif self.state == BobState.CLEANING:
            self.mess -= 4
        self.cookingProgress = max(self.cookingProgress, 0)
        self.mess = max(self.mess, 0)
        print("  BOB:")

        if self.state == BobState.COOKING:
            print("  Cozinhando...")

        elif self.state == BobState.CLEANING:
            print("  Limpando...")

        print("  Progresso da comida:", self.cookingProgress)
        print("  Bagunça:", self.mess)

        if self.state == BobState.COOKING:
            if self.cookingProgress >= 12:
                self.cookingProgress = 12
                print("  A comida está pronta!")
                self.state = BobState.CLEANING
                print("  Agora preciso limpar esta bagunça...")
        elif self.state == BobState.CLEANING:


            if self.mess <= 0:
                self.mess = 0
                print("  Tudo limpo!")
                self.cookingProgress = 0
                self.state = BobState.COOKING
                print("  Hora de preparar uma refeição!")

juca = Juca()
bob = Bob()
tick = 0

while True:
    tick += 1
    print("\n==============================")
    print("TICK", tick)
    print("==============================")
    juca.update()
    print()
    bob.update()