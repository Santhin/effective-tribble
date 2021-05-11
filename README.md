# Struktura plików:
```
.
├── poetry.lock                             
├── pyproject.toml
├── README.md
├── requirements.txt - biblioteki zawarte w projekcie  
├── zadanie1
│   ├── xkom
│   │   ├── scrapy.cfg
│   │   ├── xkom
│   │   │   ├── __init__.py
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py - ustawienia pająka
│   │   │   └── spiders
│   │   │       ├── __init__.py
│   │   │       └── xkomapi.py - crawler
│   │   └── xkomapi.json - plik ze scrawlowanymi danymi
│   └── xkom.postman_collection.json - testowanie api za pomocą postmana
├── zadanie2
│   ├── a.csv
│   ├── b.csv
│   ├── c.csv - plik z miesięcznymi średnimi wartościami
│   └── Notebook_zad2.ipynb
└── zadanie3
    ├── Notebook_zad3.ipynb
    ├── similarity_with_text.csv - plik z podobieństwem tekstów
    ├── vectors.csv - plik z wektorami
    ├── x_learn.txt
    └── x_test.txt
```

1. Scrawluj jeden ze sklepów z elektroniką euro.com.pl lub x-kom.pl za pomocą biblioteki scrapy. Potrzebuję cen i nazw produktów, ewentualnie opis. Potrzebuję co najmniej 1500 produktów. Jako wynik oczekuję: <br>
1a. pliku ze scrawlowanymi danymi (csv, json lub sqlite) - ```xkomapi.json ``` <br>
1b. pliku ze spiderem - ```xkomapi.py ```<br>
1c. mile widziane problemy na które natrafiłeś, i jak je rozwiązałeś <br>
<font color="red">Kiedyś miałem już do czynienia ze scrapowaniem sklepu x-kom, ale wtedy korzystałem z selector'ów xpath, dlatego tym razem postanowiłem skorzystać z api. Postman okazał się być bardzo pomocny przy testowaniu, nie mieli zbyt mocnych zabezpieczeń ponieważ wystarczyło wstrzyknąć X-API-Key z user agentem i autoryzacja przechodziła. Skorzystałem jeszcze z paczki scrapy-crawl-once w celu niepobierania tych samych produktów przy ponownym puszczaniu crawlera i html_text w celu wyczyszczenia opisu przedmiotu z szumu.</font> <br>

---
2. W załączniku są dwa pliki a.csv i b.csv - to są przykładowe dane. Dane są próbkowane co jeden dzień.  
Używając biblioteki pandas przygotuj następujące dane: <br>
2a. dla każdej kolumny, dla obydwu plików wygeneruj informacje o średnich wartościach dla każdego miesiąca. Innymi słowy, jeżeli w kolumnie masz 365 danych, to wynikowo dostanę 12 danych, gdzie każda to będzie średnia z każdego miesiąca. Staraj się wykonać obliczenia jak najbardziej optymalnie - używanie metod iterrows jest dyskwalifikacją. Oczekuję skryptu oraz wyników. <br>
2b. połącz pliki a.csv i b.csv używając indexu. Wygenerowany plik zapisz do c.csv. Oczekuję pliku c.csv <br>
---

3. W załączniku są pliki x_learn.txt i x_test.txt - są to teksty z Pana Tadeusza. Chodzi o "zwektoryzowanie" tych danych za pomocą metody TFIDF dostępnej w bibliotece scikit-learn.

3a. TFIDF powinien się "nauczyć" i przetworzyć dane zawarte w pliku x_learn.txt. Natomiast dane z pliku x_test.txt ma tylko przetworzyć. Potraktuj linie w plikach jako osobne próbki danych. Oczekuje przetworzonych danych(plik csv) oraz skryptu.