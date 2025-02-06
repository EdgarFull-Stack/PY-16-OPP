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
