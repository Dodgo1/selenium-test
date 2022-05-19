# selenium-test

Projekt/ćwiczenie wykorzystujący selenium do przetestowania strony PWSZ

Wykorzystuje model
POM:

<style>
ul.no-bullets {
  list-style-type: none;
}
</style>

<ul class="no-bullets">
<li>P - Page   </li>
<li>O - Object </li>
<li>M - Model  </li>
</ul>

Testuje stronę *https://pwsz.edu.pl*
a także częsciowo jej podstrony
m.in.:

- https://biblioteka.pwsz.edu.pl/
- https://usosweb.pwsz.edu.pl/

### Użycie:

`pipenv install` - instalacja zależności

`cd pages/` - przejście do właściwego folderu

`pytest` - uruchomienie wszystkich testów

**Po zakończeniu testów w tym samym folderze zostanie wygenerowany raport**



