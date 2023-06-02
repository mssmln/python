class Person:
    def __init__(self, firstAndLast):
        # print('constructed')
        self.firstAndLast = firstAndLast

    def getFullName(self):
        return self.firstAndLast

    # def __del__(self):
        # print('destructed')

    def setFullName(self, name):
        self.firstAndLast = name

    def getFirstName(self):
        return self.firstAndLast.split()[0]

    def getLastName(self):
        return self.firstAndLast.split()[1]

    def setFirstName(self, name):
        self.firstAndLast = f'{name} {self.firstAndLast.split()[1]}'

    def setLastName(self, name):
        self.firstAndLast = f'{self.firstAndLast.split()[0]} {name}'
   


bob = Person('Bob White')
print(dir(bob))
print(bob.getFullName())
bob.setFullName('Max Croci')
print(bob.getFirstName())
print(bob.getLastName())
bob.setFirstName('Gian')
bob.setLastName('Snyder')
print(bob.getFullName())