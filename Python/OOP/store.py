
class Store(object):
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

if __name__ == '__main__':
    from product import Product
    porn = Product(1203, 'hardcore porn', '2 oxen', 'the hardcore pornography people')
    condom = Product(10, 'condom', '2oz', 'hardWoodHorse')
    banana = Product(22, 'banana', '1lb', 'blue sticker lady')
    umbrella = Product(111, 'umbrella', '44oz', 'stayDryDont Cry')
    sticky_posters = Product(2434, 'sticky posters', '20oz', 'smutterButter')
    random_fruit = Product(2, 'random Fruit', '12oz', 'discount fruit')

    # porn.display_info().sell().display_info()._return('opened').display_info()


    shop = Store([porn], 'Debuquie IA', 'Matt "MF" Krabacher')

    shop.add_product(condom, banana, umbrella, sticky_posters, random_fruit).inventory()

    shop.remove_product(condom).inventory()
