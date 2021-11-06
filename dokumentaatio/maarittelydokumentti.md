# Tiralab 2021, periodi 2

# Lausegeneraattori

# Määrittelydokumenti

## Ohjelman toiminta
Käyttäjä syöttää yhden tai useamman avainsanan. Näihin avainsanoihin ja tekstikorpuksesta luodun tietorakenteen perusteella ohjelma tuottaa sarjan sanoja, joiden pitäisi muodostaa luonnollisen kielen lausetta tai virkettä muistuttava merkkijono. Korpus on laaja tekstikokoelma, joka ohjelmalle on syötetty etukäteen.

## Luonnolliset kielet
* Projekti toteutetaan suomeksi ja on tarkoitettu suomenkielisen tekstin käsittelyyn ja tuottamiseen
* Määrittely- ja suunnitteludokumentit tehdään suomeksi
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
3. Vaihda Markov-aste              (n=2)

Valitse toiminto, tai syötä sana:
```

Tai antamalla ```DAT```-tiedoston nimi:
```
$ python3 sentence_generator.py corpus.dat

*** Lausegeneraattori - päävalikko ***

1. Lue ja käsittele teksti
2. Valitse käytettävä tekstikorpus (corpus.dat)
3. Vaihda Markov-aste              (n=2)

Valitse toiminto, tai syötä sana:
```

### Komentoriviargumentit
Komentorivikutsu korpuksen käsittelemiseksi ja tietorakenteen taleentamiseksi ohjelman omaan ```dat```-tiedostoformaattiin:
```
$ python3 sentence_generator.py --init corpus.txt corpus.dat
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedostoa ```corpus.txt``` ei ole olemassa
* Tiedosto ```corpus.dat``` on jo olemassa

Komentorivikutsu, joka tulostaa generoidun merkkijono ```stdout```-vuohon:
```
$ python3 sentence_generator.py corpus.dat avainsana aste
```
Annetaan virheilmoitus ```stderr```-vuohon, mikäli:
* Tiedostoa ```corpus.dat``` ei ole olemassa
* Sanaa ```avainsana``` ei löydy lainkaan tietorakenteesta
* Argumentin ```aste``` arvo on annettujen rajojen ulkopuolella

### Kirjastorajapinta

Luokka:
```
SentenceGenerator
```

Julkiset luokkametodit:
```
SentenceGenerator.readText(filename.txt)
SentenceGenerator.save(filename.dat)
SentenceGenerator.load(filename.dat)
SentenceGenerator.generate(word, degree)
```

## Syöte ja tuloste
* Ohjelma lukee korpuksen kerran ja tallentaa syntyvän tietorakenteen tiedostoon.
* Korpuksia voi olla useita ja käyttäjä voi antaa oman tiedostonsa, jokaisen tietorakenne tallennetaan erikseen.
* Käyttäjä valitsee, mitä ennalta prosessoitua korpusta käytetään.
* Käyttäjä syöttää avainsanan ja Markovin ketjun asteen.
* Ohjelma tulostaa avainsanasta lähtien satunnaispolkua seuraten ketjussa vastaan tulevista sanoista syntyvän merkkijonon.

## Tiedostoformaatit
* Tekstikorpus luetaan yhdestä UTF-8 -koodatusta tekstitiedostosta. Järjestelmien väliset erot rivivaihtomerkkien välillä eivät vaikuta toimintaan.
* Tietorakenteet tallennetaan ohjelman omassa formaatissa. Tiedostopääte on ```dat```.

## Korpuksen käsittely
* Lähdetekstistä poistetaan kaikki muut välimerkit ja ylimääräiset välit, paitsi virkkeen lopettavat: . (piste), ! (huutomerkki) ja ? (kysymysmerkki)
* Loppumerkit käsitellään erillisinä sanoina ja erotetaan edeltävästä sanasta lisättävällä välillä
* Yhdyssanojen välissä olevia väliviivoja ei poisteta.
* Oletetaan, ettei tekstissä ole tavuviivoja.
* Suomen kielen taivutusmuotoja ei huomioida, vaan taivutettuja sanoja käsitellään eri sanoina.

## Tietorakenteet
* Tekstikorpuksen prosessoinnista syntyvä tietorakenne on Trie-puu
* Solmut ovat kokonaisia sanoja siinä muodossa, kuin ne korpustekstissä esiintyvät.
* Kaaret ovat Markovin ketjun periaatteen mukaisesti painotettuja.
* Virkkeen lopettava merkki toimii polun päätepisteenä Trie-puussa

## Lauseen, eli sanalistan generointi
* Avainsana toimii siemenenä (seed) kun sanajonoa lähdetään muodostamaan.
* Seuraava sana valitaan puusta satunnaisesti, kaarien painotuksia noudattaen.
* Annetusta ketjun asteesta riippuu, kuinka monta edeltävää sanaa otetaan huomioon.
* Kun vastaan tulee sana, joka päättyy lopetusmerkkiin, lopetetaan uusien sanojen haku.
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanan synonyymien käsittely.
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanan taivutusmuotojen käsittely.

## Testaus
* Käytetään Pythonin *unittest*-moduulia.
* Käyttöliittymä rakennetaan niin, että se voidaan testata täysin erikseen.
* Julkinen kirjastorajapinta testataan erikseen.
* Tietorakenteiden sisäinen toiminta testataan erikseen.

## Aikavaatimukset
* Korpuksen prosessointi ja lauseen generointi ovat erillisiä prosesseja, joista ensin mainittu tarvitsee tehdä vain kerran.
* Aikavaatimus mitataan suhteessa korpuksessa olevien sanojen määrään *n* ja haettavan lauseen maksimipituuteen *L*.
* Pahimmassa tapauksessa lause olisi koko korpuksen mittainen. Tällöin O(L)=O(n), ja tätä voidaan pitää projektissa aikavaatimustavoitteena.
* Trie-puu vie huomattavan paljon tilaa. Lähdetään olettamuksesta, että tämä tila on käytettävissä, eikä sille aseteta etukäteen rajoituksia.

## Lähteitä
* https://blog.demofox.org/2019/05/11/markov-chain-text-generation/
* https://www.geeksforgeeks.org/advantages-trie-data-structure/

