from abc import ABC, abstractmethod

class State(ABC):

    def __init__(self, juca):
        self.juca = juca

    @abstractmethod
    def execute(self):
        pass
class Working(State):

    def execute(self):

        self.juca.hunger += 2
        self.juca.fatigue += 5

        print("Trabalhando...")

        print("Fome:", self.juca.hunger)
        print("Cansaço:", self.juca.fatigue)

        if self.juca.fatigue > 50:
            print("Bateu um sono...")
            self.juca.change_state(Sleeping(self.juca))

        elif self.juca.hunger > 10:
            print("Bateu uma fome...")
            self.juca.change_state(Eating(self.juca))
class Eating(State):

    def execute(self):

        self.juca.hunger -= 5

        self.juca.hunger = max(self.juca.hunger, 0)

        print("Comendo...")

        print("Fome:", self.juca.hunger)
        print("Cansaço:", self.juca.fatigue)

        if self.juca.hunger <= 0:
            self.juca.hunger = 0

            print("Ufa! Já estou cheio...")

            self.juca.change_state(Working(self.juca))

            print("Hora de ir para o trabalho!")

class Sleeping(State):

    def execute(self):

        self.juca.hunger += 1
        self.juca.fatigue -= 10

        self.juca.hunger = max(self.juca.hunger, 0)
        self.juca.fatigue = max(self.juca.fatigue, 0)

        print("Dormindo...")

        print("Fome:", self.juca.hunger)
        print("Cansaço:", self.juca.fatigue)

        if self.juca.fatigue <= 0:
            self.juca.fatigue = 0

            if self.juca.hunger <= 10:

                self.juca.change_state(Working(self.juca))

                print("Hora de ir para o trabalho!")

            else:

                self.juca.change_state(Eating(self.juca))

                print("Bateu uma fome...")
class Juca:

    def __init__(self):

        self.hunger = 0
        self.fatigue = 0
        self.state = Working(self)

    def change_state(self, state):

        self.state = state

    def update(self):

        self.state.execute()

juca = Juca()

tick = 0

while True:

    tick += 1

    print()
    print("====================")
    print("Tick:", tick)
    print("====================")

    juca.update()