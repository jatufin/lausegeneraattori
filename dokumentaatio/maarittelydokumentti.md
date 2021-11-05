# Tiralab 2021, periodi 2

# Lausegeneraattori
## Määrittelydokumenti

### Ohjelman toiminta
Käyttäjä syöttää yhden tai useamman avainsanan. Näihin avainsanoihin ja tekstikorpuksesta luodun tietorakenteen perusteella ohjelma tuottaa sarjan sanoja, joiden pitäisi muodostaa luonnollisen kielen lausetta tai virkettä muistuttava merkkijono. Korpus on laaja tekstikokoelma, joka ohjelmalle on syötetty etukäteen.

### Luonnolliset kielet
* Projekti toteutetaan suomeksi ja on tarkoitettu suomenkielisen tekstin käsittelyyn ja tuottamiseen
* Dokumentaatio ja kommentointi tehdään suomeksi
* Muuttujat, luokat, metodit jne. ohjelmakoodissa nimetään englanniksi

### Ohjelmointikielet
* Ohjelmointikielenä on Python 3.8
* Tekijä voi vertaisarvioida seuraavankielisiä projekteja: C, Java, JavaScript, Python, PowerShell, Haskell, Visual Basic

### Käyttöympäristö
* Ohjelma on tarkoitettu toimimaan millä tahansa tietokoneella, jolla on yhteensopiva Python-versio asennettuna
* Ohjelman käyttö ei vaadi verkkoyhteyttä

### Käyttöliittymä
* Ohjelma käyttää interaktiivista tekstikäyttöliittymää
* Ohjelma tarjoaa toiminnallisuutta myös pelkillä komentoriviargumenteilla
* Ohjelman tarjoaa kirjastorajapinnan sen liittämiseksi muihin projekteihin

### Tietorakenteet
* Trie-puu
* Solmut ovat kokonaisia sanoja siinä muodossa, kuin ne korpustekstissä esiintyvät
* Kaaret ovat Markovin ketjun periaatteen mukaisesti painotettuja

### Korpuksen käsittely
* Lähdetekstistä poistetaan kaikki muut välimerkit ja ylimääräiset välit, paitsi virkkeen lopettavat: . (piste), ! (huutomerkki) ja ? (kysymysmerkki)
* Yhdyssanojen välissä olevia väliviivoja ei poisteta
* Oletetaan, ettei tekstissä ole tavuviivoja
* Suomen kielen taivutusmuotoja ei huomioida, vaan taivutettuja sanoja käsitellään eri sanoina


### Syöte ja tuloste
* Ohjelma lukee korpuksen kerran ja tallentaa syntyvän tietorakenteen tiedostoon
* Korpuksia voi olla useita ja käyttäjä voi antaa oman tiedostonsa, jokaisen tietorakenne tallennetaan erikseen
* Käyttäjä valitsee, mitä ennalta käsiteltyä korpusta käytetään
* Käyttäjä syöttää rajallisen määrän avainsanoja, joita käytetään tekstin löytämiseen
* Tavoite on, että jos käyttäjä syöttää kolme avainsanaa, nämä kolme sanaa ovat myös ohjelman tuottamassa, normaalin lauseen tai virkkeen mittaisessa tekstissä.

### Lauseen, eli sanalistan generointi
* Ensimmäinen avainsana toimii siemenenä (seed) kun sanajonoa lähdetään muodostamaan
* Seuraava sana valitaan puusta satunnaisesti, kaarien painotuksia noudattaen
* Kun vastaan tulee sana, joka päättyy lopetusmerkkiin, lopetetaan uusien sanojen haku.
* Mikäli lopputuloksessa ei ole kaikkia käyttäjän antamia avainsanoja, voidaan:
  * Hylätä löytynyt sanalista ja yrittää hakua uudelleen
  * Hakea erillinen virke löydetyn merkkijono perään
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanojen synonyymien käsittely
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanojen taivutusmuotojen käsittely

### Testaus
* Käytetään Pythonin *unittest*-moduulia
* Käyttöliittymä rakennetaan niin, että se voidaan testata täysin erikseen
* Tietorakenteiden toiminta testataan erikseen

### Aikavaatimukset
* Kaksi aikavaatimusta ovat erilliset:
  * Korpus käsittellään ja tietorakenne muodostetaan vain kerran
  * Lauseen muodostaminen tietorakenteesta käyttäjän syötteen perusteella
* Korpuksen pituus voidaan mitata sekä merkkien määränä n, että sanojen määränä m
* Sanalista ja mahdolliset hash -koodit saadaan tuotettua O(n) ajassa suhteessa merkkien määrään n
* Sanapuu luodaan suhteessa sanojen määrään m
