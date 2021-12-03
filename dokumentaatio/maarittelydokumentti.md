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

Lähdeteksti: <ei valittu>
Markov-aste: 2
Lauseen alku: <tyhjä>
Maksimiaste: 5

1 - Lue tekstitiedosto
2 - Vaihda Markov-aste
3 - Anna lauseen aloittavat sanat
4 - Anna haluttu lauseen pituus
5 - Tulosta tietorakenne

0 - Lopeta

Valitse toiminto tai paina <enter> tuottaaksesi uuden lauseen: 
```

### Komentoriviargumentit
Komentorivikutsu, joka tulostaa generoidun merkkijonon ```stdout```-vuohon perustuen satunnaiseen aloituslauseeseen:
```
$ python3 sentence_generator.py corpus.txt aste pituus
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedoston ```corpus.txt``` luku tai käsittely ei onnistu
* Argumentin ```aste``` arvo on annettujen rajojen ulkopuolella
* Argumentin ```pituus``` arvo on annettujen rajojen ulkopuolella

Komentorivikutsu, joka tulostaa generoidun merkkijono ```stdout```-vuohon perustuen käyttäjän antamiin avainsanoihin:
```
$ python3 sentence_generator.py corpus.txt aste pituus avainsana1 [avainsana2]
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedoston ```corpus.txt``` luku tai käsittely ei onnistu
* Sanaa ```avainsanaN``` ei löydy lainkaan tietorakenteesta
* Argumentin ```aste``` arvo on annettujen rajojen ulkopuolella
* Argumentin ```pituus``` arvo on annettujen rajojen ulkopuolella

### Kirjastorajapinta

Luokka:
```
SentenceGenerator
```

Julkiset luokkametodit:
```
SentenceGenerator(maximum_degree=5)
SentenceGenerator.readText(filename.txt)
SentenceGenerator.generate(wordlist, degree, length=8)
SentenceGenerator.generate(degree, length=8)
```

## Syöte ja tuloste
* Ohjelma lukee korpuksen kerran ja pitää syntyvän trie-puun muistissa
* Tekstitiedostoa käsitellessä syntyvä puu on ```k```+1 sanaa syvä
* Oletusarvo on ```k=5``` (Tämän voi määritellä ```SentenceGenerator```-luokan konstruktorissa
* Käyttäjä syöttää Markovin ketjun asteen ```k```.
* Käyttäjä voi syöttää enintään ```N``` avainsanaa ```sN```
* Käyttäjä syöttää Markovin ketjun asteen ```m```, oletusarvo on 8.
* Mikäli käyttäjä ei anna lainkaan avainsanaa, haetaan alku satunnaisesti.
* Ohjelma tulostaa avainsanojen muodostamasta lauseesta lähtien satunnaispolkua seuraten ketjussa vastaan tulevista sanoista syntyvän merkkijonon.

## Tiedostoformaatit
* Tekstikorpus luetaan yhdestä UTF-8 -koodatusta tekstitiedostosta. Järjestelmien väliset erot rivivaihtomerkkien välillä eivät vaikuta toimintaan.

## Korpuksen käsittely
* Lähdetekstistä poistetaan kaikki muut merkit, paitsi suomen kielen kirjaimet (a-ö)
* Kaikki kirjaimet muutetaan pieniksi kirjaimiksi
* Oletetaan, ettei tekstissä ole tavuviivoja.
* Suomen kielen taivutusmuotoja ei huomioida, vaan taivutettuja sanoja käsitellään eri sanoina.

## Tietorakenteet
* Tekstikorpuksen prosessoinnista syntyvä tietorakenne on syvyydeltään rajoitettu Trie-puu
* Solmut ovat kokonaisia sanoja siinä muodossa, kuin ne korpustekstissä esiintyvät.
* Kaaret ovat Markovin ketjun periaatteen mukaisesti painotettuja.
* Puusta haetaan enintään halutun asteen ```k``` syvyinen ketju, jota seuraava sana valitaan palautettavan lauseen seuraavaksi

## Lauseen, eli sanalistan generointi
* Lause muodostetaan Trie-puusta siten, että ensimmäiset ```k``` sanaa ovat tiedossa, ja näitä seuraamalla valitaan seuraava sana
* Tämän jälkeen haku toistetaan juuresta poistamalla alkuperäisistä ```k``` sanasta ensimmäinen ja lisäämällä löydetty uusi sana viimeiseksi
* Haun alussa seurataan käyttäjän mahdollisesti antamien avainsanojen ketjua

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
