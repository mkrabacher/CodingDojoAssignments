name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def listToDics(l1, l2):
    if len(l1) >= len(l2):
        keys = l1
        values = l2
    else:
        keys = l2
        values = l1
    new_dict = {}
    for i in range(0, len(keys)):
        # print new_dict, keys[i], values[i]
        new_dict[keys[i]] = values[i]

    return new_dict

print listToDics(name, favorite_animal)