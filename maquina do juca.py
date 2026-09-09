from enum import Enum


class State(Enum):
    WORKING = 1
    EATING = 2
    SLEEPING = 3


class Juca:
    def __init__(self):
        self.state = State.WORKING
        self.hunger = 0
        self.fatigue = 0

    def update(self):

        if self.state == State.WORKING:
            self.hunger += 2
            self.fatigue += 5

        elif self.state == State.EATING:
            self.hunger -= 5

        elif self.state == State.SLEEPING:
            self.hunger += 1
            self.fatigue -= 10
        self.hunger = max(self.hunger, 0)
        self.fatigue = max(self.fatigue, 0)

        if self.state == State.WORKING:
            print("Trabalhando...")

        elif self.state == State.EATING:
            print("Comendo...")

        elif self.state == State.SLEEPING:
            print("Dormindo...")

        print("Fome:", self.hunger)
        print("Cansaço:", self.fatigue)
        if self.state == State.WORKING:

            if self.fatigue > 50:
                self.state = State.SLEEPING
                print("Bateu um sono...")

            elif self.hunger > 10:
                self.state = State.EATING
                print("Bateu uma fome...")

        elif self.state == State.EATING:

            if self.hunger <= 0:
                self.hunger = 0

                print("Ufa! Já estou cheio...")

                self.state = State.WORKING
                print("Hora de ir para o trabalho!")

        elif self.state == State.SLEEPING:

            if self.fatigue <= 0:
                self.fatigue = 0

                if self.hunger <= 10:
                    self.state = State.WORKING
                    print("Hora de ir para o trabalho!")

                else:
                    self.state = State.EATING
                    print("Bateu uma fome...")

juca = Juca()

tick = 0

while True:
    tick += 1

    print()
    print("====================")
    print("Tick:", tick)
    print("====================")

    juca.update()