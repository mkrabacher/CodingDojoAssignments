class product(object):
    def __init__(self, price, item_name, weight, brand):
        self.status = 'for sale'
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand

    def sell(self):
        self.status = 'sold'
        return self

    def price_with_tax(self, tax):
        print (tax * self.price) + self.price
        return (tax * self.price) + self.price

    def _return(self, return_state):
        if return_state == 'defective':
            self.price = 0
            status = return_state
        elif return_state == 'like new':
            self.status = 'for sale'
        elif return_state == 'opened':
            self.status = 'used'
            self.price = self.price * .8
        return self

    def display_info(self):
        print'-------------------------'
        print 'status: ', self.status
        print 'price: ', self.price
        print 'item_name: ', self.item_name
        print 'weight: ', self.weight
        print 'brand: ', self.brand
        print'-------------------------'
        return self


porn = product(1203, 'hardcore porn', '2 oxen', 'the hardcore pornography people')

porn.display_info().sell().display_info()._return('opened').display_info()