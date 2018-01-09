import random

def randID():
    id = ''
    for i in range(0,8):
        id += str(random.randint(0,9))
    return id

def randPhone():
    num = '('
    for i in range(0,3):
        num += str(random.randint(0,9))
    num += ') '
    for i in range(0,3):
        num += str(random.randint(0,9))
    num += '-'
    for i in range(0,4):
        num += str(random.randint(0,9))
    return num

class Call(object):
    def __init__(self, caller_name, phone_number, time_of_call, reason_for_call):
        self.unique_id = randID()
        self.caller_name = caller_name
        self.caller_phone_number = phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    
    def display(self):
        print 'ID:', self.unique_id
        print 'Name:', self.caller_name
        print 'Phone Number:', self.caller_phone_number
        print 'Time:', self.time_of_call
        print 'Reason:', self.reason_for_call

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue = len(calls)
    
    def add(self, newCall):
        self.calls.append(newCall)
        return self

    def remove(self):
        self.calls.pop(0)
        return self

    def removeNum(self, num):
        for call in self.calls:
            if call.caller_phone_number == num:
                self.calls.remove(call)
        return self

    def sort(self):
        goAgain = True
        while goAgain:
            goAgain = False
            for call in range(0, len(self.calls) - 1):
                if self.calls[call].time_of_call[0] > self.calls[call + 1].time_of_call[0]:
                    self.calls.append(self.calls.pop(call))
                    goAgain = True

        return self
    
    def info(self):
        for call in self.calls:
            print '----------ID: {}------------'.format(call.unique_id)
            print call.caller_name
            print call.caller_phone_number
            print call.time_of_call
            print'----------------------------------'
        return self


aCall = Call('GangStarr', randPhone(), '6:15pm', 'bordem')
bCall = Call('major tom', '(208) 610-5161', '4:15pm', 'bordem')
cCall = Call('dick', randPhone(), '3:15pm', 'yep')
dCall = Call('jane', randPhone(), '1:25pm', 'broke')
eCall = Call('brin', randPhone(), '2:05pm', 'tmi')
fCall = Call('lee', randPhone(), '5:11pm', 'too much time')

callers = [aCall, bCall, cCall, dCall, eCall, fCall]

center = CallCenter(callers)

center.sort().info()