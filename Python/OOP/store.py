class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, *products):
        for product in products:
            self.products.append(product)
        return self

    def remove_product(self, product_name):
        self.products.remove(product_name)
        return self

    def inventory(self):
        print '---------Inventory----------'
        for i in self.products:
            print i.item_name
        print '----------------------------'
        return self

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
condom = product(10, 'condom', '2oz', 'hardWoodHorse')
banana = product(22, 'banana', '1lb', 'blue sticker lady')
umbrella = product(111, 'umbrella', '44oz', 'stayDryDont Cry')
sticky_posters = product(2434, 'sticky posters', '20oz', 'smutterButter')
random_fruit = product(2, 'random Fruit', '12oz', 'discount fruit')

# porn.display_info().sell().display_info()._return('opened').display_info()


shop = store([porn], 'Debuquie IA', 'Matt "MF" Krabacher')

shop.add_product(condom, banana, umbrella, sticky_posters, random_fruit).inventory()

shop.remove_product(condom).inventory()