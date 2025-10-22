#program posiada 2 zmienne lista1 i lista2. Zmienna fzip jest wynikiem zzipowania, 
# czyli połączenia/sklejenia ze sobą tych dwóch list, poprzez połączenie ze sobą elementow o odpowiadających sobie indeksach.
# Na końcu program drukuje wynik działania funkcji zip jako listę.

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
fzip = zip(lista1, lista2)
print(list(fzip))


#program losuje 6 liczb z zakresu 1 do 49(!) i drukuje je jako listę.
import random
k = random.sample(range(1, 50), 6)
print(k)

#program w wypadku próby dzielenia przez zero drukuje komunikat "Nie dziel przez zero!"
try:
    10/0
except ZeroDivisionError:
    print("Nie dziel przez zero!")