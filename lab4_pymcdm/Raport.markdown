W ramach laboratorium 4 przeprowadziłem wielokryterialną analizę rynku mieszkaniowego, uwzględniając tylko 3‑pokojowe mieszkania na Pogodnie w Szczecinie.
Do przeprowadzenia analizy znalazłem 10 mieszkań na popularnych serwisach mieszkaniowych, z których ręcznie zebrałem dane takie jak cena, czynsz itp.
W przypadku kryterium stanu wszedłem w rolę decydenta, samodzielnie przyznając ocenę każdemu mieszkaniu w skali 1–4, gdzie 1 to najgorszy rating, a 4 najbardziej pożądany.
Odległość od centrum miasta i od przystanku komunikacji zbiorowej była określana na podstawie danych z Google Maps.

Oto konkretne kryteria i ich definicja (zysk/koszt):

cena (zł): koszt,

czynsz (zł): koszt,

metraż (m²): zysk,

stan (1–4): zysk; 1 = remont generalny, 2 = remont, 3 = do odświeżenia, 4 = gotowe do wprowadzenia,

piętro: zysk,

przestrzenie dodatkowe (garaż, piwnica, strych, ogródek, komórka lokatorska): zysk; każda z dodatkowych przestrzeni oznacza +1 do wartości,

odległość od centrum (km): koszt,

odległość od przystanku komunikacji zbiorowej (m): koszt.

Ranking SPOTIS:
Mieszkanie nr 1 – miejsce: 2.0 (wynik: 0.218)
Mieszkanie nr 2 – miejsce: 9.0 (wynik: 0.347)
Mieszkanie nr 3 – miejsce: 1.0 (wynik: 0.152) → najlepsze
Mieszkanie nr 4 – miejsce: 7.0 (wynik: 0.295)
Mieszkanie nr 5 – miejsce: 8.0 (wynik: 0.341)
Mieszkanie nr 6 – miejsce: 10.0 (wynik: 0.350) → najgorsze
Mieszkanie nr 7 – miejsce: 6.0 (wynik: 0.282)
Mieszkanie nr 8 – miejsce: 4.0 (wynik: 0.280)
Mieszkanie nr 9 – miejsce: 5.0 (wynik: 0.280)
Mieszkanie nr 10 – miejsce: 3.0 (wynik: 0.232)

Ranking TOPSIS:
Mieszkanie nr 1 – miejsce: 5.0 (wynik: 0.309)
Mieszkanie nr 2 – miejsce: 9.0 (wynik: 0.474)
Mieszkanie nr 3 – miejsce: 4.0 (wynik: 0.436)
Mieszkanie nr 4 – miejsce: 3.0 (wynik: 0.428)
Mieszkanie nr 5 – miejsce: 2.0 (wynik: 0.697)
Mieszkanie nr 6 – miejsce: 1.0 (wynik: 0.616) → najlepsze
Mieszkanie nr 7 – miejsce: 8.0 (wynik: 0.602)
Mieszkanie nr 8 – miejsce: 7.0 (wynik: 0.597)
Mieszkanie nr 9 – miejsce: 6.0 (wynik: 0.362)
Mieszkanie nr 10 – miejsce: 10.0 (wynik: 0.563) → najgorsze

Ranking COMET:
Mieszkanie nr 1 – miejsce: 10.0 (wynik: 0.245) → najgorsze
Mieszkanie nr 2 – miejsce: 6.0 (wynik: 0.438)
Mieszkanie nr 3 – miejsce: 7.0 (wynik: 0.404)
Mieszkanie nr 4 – miejsce: 8.0 (wynik: 0.359)
Mieszkanie nr 5 – miejsce: 1.0 (wynik: 0.775) → najlepsze
Mieszkanie nr 6 – miejsce: 2.0 (wynik: 0.658)
Mieszkanie nr 7 – miejsce: 4.0 (wynik: 0.616)
Mieszkanie nr 8 – miejsce: 3.0 (wynik: 0.642)
Mieszkanie nr 9 – miejsce: 9.0 (wynik: 0.293)
Mieszkanie nr 10 – miejsce: 5.0 (wynik: 0.571)

SPOTIS mierzy odległość każdej alternatywy od punktu ESP (Expected Solution Point), wybranego przez decydenta jako ten zawierający oczekiwane wartości każdego kryterium. W tym wypadku najlepszą opcją jest ta, której wynik jest najniższy (najbliższy do ESP), a najgorszą – ta o największej odległości. Według SPOTIS każda alternatywa jest akceptowalna, a kluczowe jest określenie odległości od ESP, stąd tak duża różnica względem wyników z TOPSIS. Co istotne, SPOTIS nie wykorzystuje klasycznej normalizacji wektorowej jak TOPSIS i jest mało narażony na zmiany rankingu w przypadku zmian alternatyw czy danych.

TOPSIS wykorzystuje idealne i anty‑idealne rozwiązanie, zbudowane na podstawie wprowadzonych kryteriów. Mieszkanie nr 6 ma bardzo niską cenę oraz niski czynsz, a także przyzwoite pozostałe wartości, co oznacza, że jest pod wieloma względami blisko rozwiązania idealnego i daleko od anty‑idealnego, stąd jego wysoka lokata.

COMET tworzy tzw. obiekty charakterystyczne na podstawie wprowadzonych danych; posiadając 2 poziomy (min i max) i 8 kryteriów, daje to 256 obiektów charakterystycznych (2⁸ = 256). W tym wypadku wykorzystałem metodę TOPSIS jako eksperta do oceny obiektów charakterystycznych, co pozwoliło na automatyzację procesu. Co więcej, w przeciwieństwie do TOPSIS, COMET nie jest podatny na problem odwrócenia rankingu.

Podsumowując, wszystkie wykorzystane metody i ich wyniki są użyteczne. SPOTIS może okazać się przydatny, kiedy kluczowa jest rola decydenta i jego preferencje. TOPSIS – kiedy szukamy teoretycznie i pod względem matematycznym idealnego rozwiązania, a COMET – kiedy chcemy sprawdzić, co jest najbliższe analizie eksperckiej.

W dalszej części kodu przeprowadziłem jeszcze dodatkową analizę na podstawie metody Spotis, aby sprawdzić jaka jest rzeczywiście optymalna wartość ESP po zastosowaniu metody spotis, w tym celu wykorzystałem wykres konturowy. W dalszej części jeszcze obecne są 2 wykresy, 1 przedsatwiający wpływ zmiany ESP na RW, gdzie wartości ESP były zmieniane stopniowo o +1% i -1%. Po czym przedsatwiłem jak wcześniej wspomniane zmiany ESP wpływają na ranking.