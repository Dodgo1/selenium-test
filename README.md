# selenium-test

Projekt/ćwiczenie wykorzystujący selenium do przetestowania strony PWSZ

Wykorzystuje model
POM:

* P - Page
* O - Object
* M - Model

Testuje stronę *https://pwsz.edu.pl*
a także częsciowo jej podstrony
m.in.:

- https://biblioteka.pwsz.edu.pl/
- https://usosweb.pwsz.edu.pl/

### Użycie:

`pipenv install` - instalacja zależności

`pytest` - uruchomienie wszystkich testów

`pytest -n auto ` - uruchomienie wszystkich testów + wykorzystanie więcej rdzeni

**Po zakończeniu testów w tym samym folderze zostanie wygenerowany raport**



