class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 15
        else:
            self.tax = 12
    
    def display_all(self):
        print 'Price: ', self.price
        print 'speed: ', self.speed
        print 'fuel: ', self.fuel
        print 'mileage: ', self.mileage
        print 'tax: ', self.tax

print '------------------------'
car1 = car(2000, '35mph', 'full', '15mpg')
car1.display_all()
print '------------------------'
car2 = car(2000, '315mph', 'full', '15mpg')
car2.display_all()
print '------------------------'
car3 = car(2000, '305mph', 'full', '15mpg')
car3.display_all()
print '------------------------'
car4 = car(2000, '205mph', 'full', '15mpg')
car4.display_all()
print '------------------------'
car5 = car(2000, '21mph', 'full', '15mpg')
car5.display_all()
print '------------------------'
car6 = car(2000, '25mph', 'full', '15mpg')
car6.display_all()
print '------------------------'
