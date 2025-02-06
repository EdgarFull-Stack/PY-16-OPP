# 1 Task
class Gyvunas:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def judeti(self):
        print(f'{self.vardas} juda')
#
class Kate(Gyvunas):
    def miaukseti(self):
        print(f'{self.vardas} miauksi ')

#
class Suo(Gyvunas):
    def lot(self):
        print(f'{self.vardas} loja')
#
cat = Kate('Murkis',5)
dog = Suo('Messi',6)
#
cat.judeti()
cat.miaukseti()
dog.judeti()
dog.lot()
# dog.miaukseti() or cat.lot() is not working because functions in different classes
