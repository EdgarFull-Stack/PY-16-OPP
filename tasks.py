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
print('-'*40)
#  2 Task
class Variklis:
    def __init__(self,galia):
        self.galia = galia
    def startuoti(self):
        print(f'Variklis veikia su galia: {self.galia} arklio galiu')
#
class Automobilis:
    def __init__(self,marke,modelis,variklis):
        self.marke = marke
        self.modelis = modelis
        self.variklis = variklis
    def vaziuoti(self):
        self.variklis.startuoti()
#
auto1 = Automobilis('BMW', 'M3', Variklis(500))
auto2 = Automobilis('Tesla', 'Model S Plaid', Variklis(1020))
auto1.vaziuoti()
auto2.vaziuoti()
print('-'*40)
# 3 Task
class Asmuo:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius
        print(f'Vardas: {self.vardas}, Amzius: {self.amzius}')
#
class Darbuotojas(Asmuo):
    def __init__(self, vardas, amzius, pareigos):
        super().__init__(vardas, amzius)
        self.pareigos = pareigos
        print(f'Pareigos: {self.pareigos}')
#
darbuotojas = Darbuotojas('Edgar','27','web developer')
print('-'*40)
# 4 Task
class TransportoPriemone:
    def judeti(self):
        print('Transportas juda')
#
class Dviratis(TransportoPriemone):
    def judeti(self):
        super().judeti()
        print('Dviratis juda')
#
transportas = TransportoPriemone()
dviratis = Dviratis()
#
transportas.judeti()
dviratis.judeti()
