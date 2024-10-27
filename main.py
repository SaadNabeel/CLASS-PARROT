class Parrot:
    species = "bird"

    def __init__(self, name, age):  
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name, 'Age:', self.age)


p1 = Parrot('woo', 12)
p1.display()

p2 = Parrot('blu', 8)
p2.display()
