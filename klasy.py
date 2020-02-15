class Samochod:
    def __init__(self, ile_koni, marka):
        self.ile_koni = ile_koni
        self.marka = marka
    def wypisz_info(self):
        print('Samochód marki '+self.marka)
        print('Ma '+str(self.ile_koni)+' koni.')


auto = Samochod(500, 'fiat') #tworzenie samochodu
auto.wypisz_info() #wywołanie jego metody

print(auto.marka) #odwołanie się do jego składowej

class Kilof:
    pass # do napisania razem

class Blok:
    pass # do napisania razem

# funkcja do zwracania wytrzymałości

#Zadanie:
#Napisz klasę Gracz, która będzie miała takie składowe:
#aktualne życie, maksymalne życie, kilof
#i takie metody:
#regeneruj() - regeneruje aktualne życie do maxa
#zwieksz_max_zycie() - zwiększa maksymalne życie o 1
#niszcz_blok(blok): zadaje hity blokowi, odejmuje mu tyle
#wytrzymałości, ile hitów zadaje kilof







