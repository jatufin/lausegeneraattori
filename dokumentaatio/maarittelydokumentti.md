# Tiralab 2021, periodi 2
Koulutusohjelma: Tietojenkäsittelytieteen kandidaatti, Helsingin yliopisto

# Lausegeneraattori

# Määrittelydokumenti

## Ohjelman toiminta
Käyttäjä voi syöttää yhden tai useamman avainsanan, tai ne generoidaan satunnaisesti. Näihin avainsanoihin ja tekstikorpuksesta luodun tietorakenteen perusteella ohjelma tuottaa sarjan sanoja, joiden pitäisi muodostaa luonnollisen kielen lausetta tai virkettä muistuttava merkkijono. Korpus on laaja tekstikokoelma, joka ohjelmalle on syötetty etukäteen.

## Luonnolliset kielet
* Projekti toteutetaan suomeksi ja on tarkoitettu suomenkielisen tekstin käsittelyyn ja tuottamiseen
* Määrittely-, suunnittelu- ja testausdokumentit tehdään suomeksi
* Muuttujat, luokat, metodit jne. ohjelmakoodissa nimetään englanniksi
* Ohjelmakoodin sisäinen dokumentaatio ja kommentit tehdään engalnniksi

## Ohjelmointikielet
* Ohjelmointikielenä on Python 3.8
* Tekijä voi vertaisarvioida seuraavankielisiä projekteja: C, Java, JavaScript, Python, PowerShell, Haskell, Visual Basic

## Käyttöympäristö
* Ohjelma on tarkoitettu toimimaan millä tahansa tietokoneella, jolla on yhteensopiva Python-versio asennettuna
* Ohjelman käyttö ei vaadi verkkoyhteyttä

## Käyttöliittymä
Ohjelma käyttää interaktiivista tekstikäyttöliittymää ja tarjoaa toiminnallisuutta myös pelkillä komentoriviargumenteilla. Lisäksi tarjotaan kirjastorajapinta sen liittämiseksi muihin projekteihin.

### Interaktiivinen käyttöliittymä

Tekstipohjainen käyttöliittymä avautuu, mikäli ohjelma käynnistetään ilman argumentteja:
```
$ python3 sentence_generator.py

*** Lausegeneraattori - päävalikko ***

1. Lue ja käsittele teksti
2. Valitse käytettävä tekstikorpus (ei valittu)
3. Vaihda Markov-aste              (k=2)

Valitse toiminto, syötä aloitussana tai -lause, tai paina <enter>:
```

Tai antamalla ```JSON```-tiedoston nimi:
```
$ python3 sentence_generator.py corpus.json

*** Lausegeneraattori - päävalikko ***

1. Lue ja käsittele teksti
2. Valitse käytettävä tekstikorpus (corpus.json)
3. Vaihda Markov-aste              (k=2)

Valitse toiminto, syötä aloitussana tai -lause, tai paina <enter>:
```

### Komentoriviargumentit
Komentorivikutsu korpuksen käsittelemiseksi ja tietorakenteen taleentamiseksi ohjelman omaan ```json```-tiedostoformaattiin:
```
$ python3 sentence_generator.py --init corpus.txt corpus.json
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedostoa ```corpus.txt``` ei ole olemassa
* Tiedosto ```corpus.json``` on jo olemassa

Komentorivikutsu, joka tulostaa generoidun merkkijonon ```stdout```-vuohon perustuen satunnaiseen aloituslauseeseen:
```
$ python3 sentence_generator.py corpus.json aste
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedostoa ```corpus.json``` ei ole olemassa
* Argumentin ```aste``` arvo on annettujen rajojen ulkopuolella

Komentorivikutsu, joka tulostaa generoidun merkkijono ```stdout```-vuohon perustuen käyttäjän antamaan avainsanaan:
```
$ python3 sentence_generator.py corpus.json aste avainsana1 [avainsana2]
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedostoa ```corpus.json``` ei ole olemassa
* Sanaa ```avainsanaN``` ei löydy lainkaan tietorakenteesta
* Argumentin ```aste``` arvo on annettujen rajojen ulkopuolella

### Kirjastorajapinta

Luokka:
```
SentenceGenerator
```

Julkiset luokkametodit:
```
SentenceGenerator.readText(filename.txt)
SentenceGenerator.save(filename.json)
SentenceGenerator.load(filename.json)
SentenceGenerator.generate(wordlist, degree)
SentenceGenerator.generate(degree)
```

## Syöte ja tuloste
* Ohjelma lukee korpuksen kerran ja tallentaa syntyvän tietorakenteen tiedostoon.
* Korpuksia voi olla useita ja käyttäjä voi antaa oman tiedostonsa, jokaisen tietorakenne tallennetaan erikseen.
* Käyttäjä valitsee, mitä ennalta prosessoitua korpusta käytetään.
* Käyttäjä syöttää Markovin ketjun asteen ```k```.
* Käyttäjä voi syöttää enintään ```k``` avainsanaa ```sN```
* Mikäli käyttäjä ei anna lainkaan avainsanaa, haetaan alku satunnaisesti.
* Ohjelma tulostaa avainsanojen muodostamasta lauseesta lähtien satunnaispolkua seuraten ketjussa vastaan tulevista sanoista syntyvän merkkijonon.

## Tiedostoformaatit
* Tekstikorpus luetaan yhdestä UTF-8 -koodatusta tekstitiedostosta. Järjestelmien väliset erot rivivaihtomerkkien välillä eivät vaikuta toimintaan.
* Tietorakenteet tallennetaan JSON-formaatissa. Tiedostopääte on ```json```.
* 

## Korpuksen käsittely
* Lähdetekstistä poistetaan kaikki muut välimerkit ja ylimääräiset välit, paitsi virkkeen lopettavat: . (piste), ! (huutomerkki) ja ? (kysymysmerkki)
* Loppumerkit käsitellään erillisinä sanoina ja erotetaan edeltävästä sanasta lisättävällä välillä
* Yhdyssanojen välissä olevia väliviivoja ei poisteta.
* Oletetaan, ettei tekstissä ole tavuviivoja.
* Suomen kielen taivutusmuotoja ei huomioida, vaan taivutettuja sanoja käsitellään eri sanoina.

## Tietorakenteet
* Tekstikorpuksen prosessoinnista syntyvä tietorakenne on syvyydeltään rajoitettu Trie-puu
* Solmut ovat kokonaisia sanoja siinä muodossa, kuin ne korpustekstissä esiintyvät.
* Kaaret ovat Markovin ketjun periaatteen mukaisesti painotettuja.
* Virkkeen lopettava merkki toimii polun päätepisteenä Trie-puussa
* Puusta haetaan enintään halutun asteen ```k``` syvyinen ketju, jota seuraava sana valitaan palautettavan lauseen seuraavaksi

## Lauseen, eli sanalistan generointi
* Lause muodostetaan Trie-puusta siten, että ensimmäiset ```k``` sanaa ovat tiedossa, ja näitä seuraamalla valitaan seuraava sana
* Tämän jälkeen haku toistetaan juuresta poistamalla alkuperäisistä ```k``` sanasta ensimmäinen ja lisäämällä löydetty uusi sana viimeiseksi
* Haun alussa ensimmäiset sanat valitaan satunnaisesti, käyttäjän mahdollisesti antamiin avainsanoihin perustuen

## Testaus
* Käytetään Pythonin *unittest*-moduulia.
* Käyttöliittymä rakennetaan niin, että se voidaan testata täysin erikseen.
* Julkinen kirjastorajapinta testataan erikseen.
* Tietorakenteiden sisäinen toiminta testataan erikseen.

## Aikavaatimukset
* Korpuksen prosessointi ja lauseen generointi ovat erillisiä prosesseja, joista ensin mainittu tarvitsee tehdä vain kerran.
* Aikavaatimus mitataan suhteessa korpuksessa olevien sanojen määrään *n* ja haettavan lauseen maksimipituuteen *L*.
* Täydellisen trie-puun sijasta, jonka syvyys olisi yhtä suuri kuin leveys, ja tilavaatimus siten O(n^2) tarvitaan vain ```k``` + 1 syvyinen puu.
* Tällä rajauksella päästään sekä korpuksen käsittelyssä, että lauseen generoinnissa aikavaatimukseen O(n)

## Lähteitä
* https://blog.demofox.org/2019/05/11/markov-chain-text-generation/
* https://www.geeksforgeeks.org/advantages-trie-data-structure/
* https://www.cs.jhu.edu/~langmea/resources/lecture_notes/tries_and_suffix_tries.pdf
* GUSFIELD, D. Algorithms on Strings, Trees, and Sequences : Computer Science and Computational Biology. Cambridge [England]: Cambridge University Press, 1997. ISBN 9780521585194. Disponível em: https://search-ebscohost-com.libproxy.helsinki.fi/login.aspx?direct=true&db=e000xww&AN=502387&site=ehost-live&scope=site. Acesso em: 13 nov. 2021.
