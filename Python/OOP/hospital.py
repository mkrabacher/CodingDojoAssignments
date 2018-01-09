import random

def randID():
    id = ''
    for i in range(0,8):
        id += str(random.randint(0,9))
    return id

def randBed(max):
    return random.randint(0,max)

class Patient(object):
    def __init__(self, name, allergies):
        self.id = randID()
        self.name = name
        self.allergies = allergies
        self.bed_num = 'none'

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    
    def admit(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.bed_num = randBed(self.capacity)
            print "you're lucky but you made it in {}.".format(patient.name)
        else:
            print "we don't have room in here for your kind."

    def discharge(self, name):
        for pat in self.patients:
            if pat.name == name:
                self.patients.remove(pat)
                print "get out of here {}, you're healthy enough to make it on your own.".format(pat.name)


buzz = Patient('buzz', 'nuts')
craig = Patient('craig', 'woemn')
ganggreeen = Patient('ganggreeen', 'men')
cancer = Patient('cancer', 'fun')
death = Patient('death', 'life')

Exploitation_General = Hospital('Exploitation General', 3)

Exploitation_General.admit(buzz)
Exploitation_General.admit(craig)
Exploitation_General.admit(cancer)
Exploitation_General.discharge('craig')
Exploitation_General.admit(ganggreeen)
Exploitation_General.admit(death)