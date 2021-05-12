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