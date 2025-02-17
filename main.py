# Example
class Kate:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

    def miaukseti(self):
        print(f"{self.vardas} sako MIAU!!!")

cat = Kate('Murkis', 'Geltonas')
cat.begti()
cat.miaukseti()
print('-'*40)
# Example
class Gyvunas:
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print(f"{self.vardas} bėgu!!!")

class Kate(Gyvunas):
    def miaukseti(self):
        print(f"{self.vardas} sako MIAU!!!")
cat = Kate('Murkis','Geltonas')
cat.miaukseti()
cat.begti()

class Suo(Gyvunas):
    def loti(self):
        print(f'{self.vardas} loja!!!')
dog = Suo('Messi','Kreminis')
dog.loti()
print('-'*40)
# Example
class Stack:
    def __init__(self):
        self.data = []

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        return self.data.pop()

class Element:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def __str__(self):
        return f'{self.item1} {self.item2}'

elems = [
     Element(1,2),
     Element(3,4),
     Element(5,6)
]

stck = Stack()

for i in elems:
    stck.push(i)

a = stck.pop()

for i in stck.data:
    print(i)
print('-'*20)
print(a)
print('-'*40)
# Example
class Asmuo:
    def __init__(self, vardas, pavarde, gim_metai):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gim_metai = gim_metai

class MokinioTevas(Asmuo):
    def __init__(self, vardas, pavarde, gim_metai, darboviete):
        super().__init__(vardas, pavarde, gim_metai)
        self.darboviete = darboviete
tevas = MokinioTevas(1, 2 ,3 ,4)
print(tevas.vardas)
print(tevas.pavarde)
print('-'*40)
# Example
class Mygtukas:
    def deaktyvuoti(self):
        print("Mygtukas deaktyvuotas")

class RaudonasMygtukas(Mygtukas):
    def deaktyvuoti(self):
        super().deaktyvuoti()
        print("Spalva pasikeitė į rausvą")
print('-'*40)
# Example
import datetime
import pickle
class House:
    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}"

try:
    with open("namai.pickle", mode="rb") as f:
        houses_kaupiklis = pickle.load(f)
except:
    houses_kaupiklis = []
#
new_house = House(price=190000, year=2024)
houses_kaupiklis.append(new_house)
#
with open('namai.pickle', mode='wb') as f:
    pickle.dump(houses_kaupiklis, f)

for h in houses_kaupiklis:
    print(h)