def wypisz_tekst(tekst, ile_razy = 1):
    print(tekst*ile_razy)

def policz_srednia(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma/len(lista)

def dodaj(a, b):
    return a+b

#zadania
#1. Napisz funkcję, która zwróci odległość między dwoma punktami w 2D(wzór
# z prezentacji).
#2. Napisz funkcję, która policzy średnią z wylosowanych liczb,
# z zakresu do 0 do 100. Losuje tyle razy, ile jej podamy w argumencie.
#3. Napisz funkcję, która zwróci odległość między dwoma punktami w 3D(wzór
# z prezentacji).
#4. Napisz funkcję powitanie(), która przyjmuje jeden argument, który domyślnie
# ma wartość 'en' i wtedy ta funkcja wypisuje powitanie po angielsku(hello), ale jak
# argument będzie 'pl' to wypisze powitanie po polsku(elo), a jak 'es' to po hiszpańsku(hola)
#5. Napisz funkcję, która zwróci najmniejszą wartość z listy(musisz przeglądnąć)
# listę, trochę podobne do policz_srednia(lista)
#6. To samo ale policz minimum

#wywolania funkcji: odkomentuj tylko te linijki, które masz już zrobione
#1.
#punkt1=[2,5]
#punkt2=[4,-1]
#odleglosc=odleglosc2D(punkt1, punkt2)
#print(odleglosc)

#2.
#srednia=losuj_i_zwroc_srednia(10000)
#print(srednia)

#3.
#punkt1=[2,5, 7]
#punkt2=[4,-1, 8]
#odleglosc=odleglosc3D(punkt1, punkt2)
#print(odleglosc)

#4.
#powitanie('pl')
#powitanie()

#5 i 6
#lista = [3,8,-45,22,-5,234,65,325,-356,11,8]
#print(minimum(lista))
#print(maksimum(lista))


