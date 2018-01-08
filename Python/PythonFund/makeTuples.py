my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tupler(dic):
    arr = []
    for el in dic:
        arr.append((el, dic[el]))
    return arr

print tupler(my_dict)