# Tiralab 2021, periodi 2

# Lausegeneraattori
## Määrittelydokumenti

### Luonnolliset kielet
* Projekti toteutetaan suomeksi ja on tarkoitettu suomenkielisen tekstin käsittelyyn ja tuottamiseen
* Dokumentaatio ja kommentointi tehdään suomeksi
* Muuttujat, luokat, metodit jne. nimetään englanniksi

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
* Solmut ovat kokonaisia sanoja

### Korpuksen käsittely
* Lähdetekstistä poistetaan kaikki muut välimerkit ja välit, paitsi virkkeen lopettavat: . (piste), ! (huutomerkki) ja ? (kysymysmerkki)
* Yhdyssanojen välissä olevia väliviivoja ei poisteta
* Oletetaan, ettei tekstissä ole tavuviivoja
* Suomen kielen taivutusmuotoja ei huomioida, vaan taivutettuja sanoja käsitellään eri sanoina

### Syöte ja tuloste
* Ohjelma lukee korpuksen kerran ja tallentaa syntyvän trie-tietorakenteen tiedostoon
* Korpuksia voi olla useita ja käyttäjä voi antaa oman tiedostonsa, jokaisen tietorakenne tallennetaan erikseen
* Käyttäjä syöttää rajallisen määrän avainsanoja, joita käytetään tekstin löytämiseen
* Tavoite on, että jos käyttäjä syöttää kolme avainsanaa, nämä kolme sanaa ovat myös ohjelman tuottamassa, normaalin lauseen tai virkkeen mittaisessa tekstissä.
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanojen synonyymien käsittely
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanojen taivutusmuotojen käsittely

### Testaus
* Käytetään *unittest*-moduulia
* Käyttöliittymä rakennetaan niin, että se voidaan testata täysin erikseen
* Tietarakenteet testataan täysin erikseen
