class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    
    def login(self):
        self.logged = True
        print self.name + ' is loffed in.'
        return self

    def logout(self):
        self.logged = False
        print self.name + ' is logged out.'
        return self


numa = User('Numanu', 'numanator@myla.com')

numa.login().logout()
print numa.logged
numa.logout()
