class bike(object):
    def __init__(self, price, max_speed):
        bike.price = price
        bike.max_speed = max_speed
        bike.miles = 0

    def display_info(self):
        print 'This bike costs {}, has a max speed of {}, and have been ridden {} miles total'.format(self.price, self.max_speed, self.miles)
        return self
    
    def ride(self):
        print 'ridin now boss.'
        self.miles += 10
        return self
    
    def reverse(self):
        print 'reversin now boss'
        self.miles -= 5
        return self

    




print '--------------------------------------------------------------------------'
bike1 = bike(200, "25mph")
bike1.display_info().ride().reverse().ride().ride().reverse().display_info()
print '--------------------------------------------------------------------------'
bike2 = bike(100, "21mph")
bike2.display_info().ride().reverse().reverse().reverse().reverse().display_info()
print '--------------------------------------------------------------------------'
bike3 = bike(400, "254mph")
bike3.display_info().reverse().ride().ride().display_info()
print '--------------------------------------------------------------------------'