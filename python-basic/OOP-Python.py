class Superman:
    strength = 50
    def __init__(self, name,weapon,clothes):
        self.name = name
        self.weapon = weapon
        self.clothes = clothes
    def __str__(self):
        return 'day la {} su dung {}'.format(self.name,self.clothes)
    def __repr__(self):
        return 'hello superman'
superman_A= Superman('meo','mong vuot','cao')

print('%s'%superman_A)
print('%r'%superman_A)