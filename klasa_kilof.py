#skladowe: wytrzymalosc, wydajnosc, atak, enchanty, materiał
#metody: naprawianie go, zyskanie enchanta, niszczenie bloków

def wytrzymalosc_dla_materialu(material):
    if material == 'drewno':
        return 59
    elif material == 'kamien':
        return 150
    elif material == 'stal':
        return 250

def atak_dla_materialu(material):
    if material == 'drewno':
        return 50
    elif material == 'kamien':
        return 100
    elif material == 'stal':
        return 150

def wydajnosc_dla_materialu(material):
    if material == 'drewno':
        return 10
    elif material == 'kamien':
        return 20
    elif material == 'stal':
        return 30

class Kilof:
    def __init__(self, material, enchanty=[]):
        self.wytrzymalosc_max = wytrzymalosc_dla_materialu(material)
        self.aktualna_wytrzymalosc = self.wytrzymalosc_max 
        self.wydajnosc = wydajnosc_dla_materialu(material)
        self.atak = atak_dla_materialu(material)
        self.material = material
        self.enchanty = enchanty
    def napraw(self):
        self.aktualna_wytrzymalosc = wytrzymalosc_max
        print('naprawiono')
    def enchantuj(self, enchant):
        self.enchanty.append(enchant)
    def niszcz_blok(self, blok):
        pass

kilof1 = Kilof('drewno') 
kilof2 = Kilof('stal', ['sharpness', 'efficiency'])

kilof1.enchantuj('sharpness')

print(kilof1.material)
print(kilof1.enchanty)

print(kilof2.material)
print(kilof2.enchanty)





        
        
