class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, 170)
    
    def fly(self):
        self.health -= 10

    def display_health(self):
        print 'Imma Bong Rippin Dragon!', self.health
        return self

    

doggo = Dog('doog', 150)

bongripper = Dragon('Bongripper', 170)

doggo.display_health().walk().walk().walk().run().run().display_health().pet().display_health()

bongripper.display_health().fly()

