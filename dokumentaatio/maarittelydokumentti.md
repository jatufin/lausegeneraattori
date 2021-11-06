# Tiralab 2021, periodi 2

# Lausegeneraattori

# Määrittelydokumenti

1 Ohjelman toiminta
Käyttäjä syöttää yhden tai useamman avainsanan. Näihin avainsanoihin ja tekstikorpuksesta luodun tietorakenteen perusteella ohjelma tuottaa sarjan sanoja, joiden pitäisi muodostaa luonnollisen kielen lausetta tai virkettä muistuttava merkkijono. Korpus on laaja tekstikokoelma, joka ohjelmalle on syötetty etukäteen.

1 Luonnolliset kielet
* Projekti toteutetaan suomeksi ja on tarkoitettu suomenkielisen tekstin käsittelyyn ja tuottamiseen
* Määrittely- ja suunnitteludokumentit tehdään suomeksi
* Muuttujat, luokat, metodit jne. ohjelmakoodissa nimetään englanniksi
* Ohjelmakoodin sisäinen dokumentaatio ja kommentit tehdään engalnniksi

1 Ohjelmointikielet
* Ohjelmointikielenä on Python 3.8
* Tekijä voi vertaisarvioida seuraavankielisiä projekteja: C, Java, JavaScript, Python, PowerShell, Haskell, Visual Basic

1 Käyttöympäristö
* Ohjelma on tarkoitettu toimimaan millä tahansa tietokoneella, jolla on yhteensopiva Python-versio asennettuna
* Ohjelman käyttö ei vaadi verkkoyhteyttä

1 Käyttöliittymä
Ohjelma käyttää interaktiivista tekstikäyttöliittymää ja tarjoaa toiminnallisuutta myös pelkillä komentoriviargumenteilla. Lisäksi tarjotaan kirjastorajapinta sen liittämiseksi muihin projekteihin.

1.1 Interaktiivinen käyttöliittymä

1.1 Komentoriviargumentit

1.1 Kirjastorajapinta

1 Syöte ja tuloste
* Ohjelma lukee korpuksen kerran ja tallentaa syntyvän tietorakenteen tiedostoon.
* Korpuksia voi olla useita ja käyttäjä voi antaa oman tiedostonsa, jokaisen tietorakenne tallennetaan erikseen.
* Käyttäjä valitsee, mitä ennalta prosessoitua korpusta käytetään.
* Käyttäjä syöttää avainsanan ja Markovin ketjun asteen.
* Ohjelma tulostaa avainsanasta lähtien satunnaispolkua seuraten ketjussa vastaan tulevista sanoista syntyvän merkkijonon.

1 Korpuksen käsittely
* Lähdetekstistä poistetaan kaikki muut välimerkit ja ylimääräiset välit, paitsi virkkeen lopettavat: . (piste), ! (huutomerkki) ja ? (kysymysmerkki)
* Loppumerkit käsitellään erillisinä sanoina ja erotetaan edeltävästä sanasta lisättävällä välillä
* Yhdyssanojen välissä olevia väliviivoja ei poisteta.
* Oletetaan, ettei tekstissä ole tavuviivoja.
* Suomen kielen taivutusmuotoja ei huomioida, vaan taivutettuja sanoja käsitellään eri sanoina.

1 Tietorakenteet
* Tekstikorpuksen prosessoinnista syntyvä tietorakenne on Trie-puu
* Solmut ovat kokonaisia sanoja siinä muodossa, kuin ne korpustekstissä esiintyvät.
* Kaaret ovat Markovin ketjun periaatteen mukaisesti painotettuja.
* Virkkeen lopettava merkki toimii polun päätepisteenä Trie-puussa

1 Lauseen, eli sanalistan generointi
* Avainsana toimii siemenenä (seed) kun sanajonoa lähdetään muodostamaan.
* Seuraava sana valitaan puusta satunnaisesti, kaarien painotuksia noudattaen.
* Annetusta ketjun asteesta riippuu, kuinka monta edeltävää sanaa otetaan huomioon.
* Kun vastaan tulee sana, joka päättyy lopetusmerkkiin, lopetetaan uusien sanojen haku.
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanan synonyymien käsittely.
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanan taivutusmuotojen käsittely.

1 Testaus
* Käytetään Pythonin *unittest*-moduulia.
* Käyttöliittymä rakennetaan niin, että se voidaan testata täysin erikseen.
* Tietorakenteiden toiminta testataan erikseen.

1 Aikavaatimukset
* Korpuksen prosessointi ja lauseen generointi ovat erillisiä prosesseja, joista ensin mainittu tarvitsee tehdä vain kerran.
* Aikavaatimus mitataan suhteessa korpuksessa olevien sanojen määrään *n* ja haettavan lauseen maksimipituuteen *L*.
* Pahimmassa tapauksessa lause olisi koko korpuksen mittainen. Tällöin O(L)=O(n), ja tätä voidaan pitää projektissa aikavaatimustavoitteena.
* Trie-puu vie huomattavan paljon tilaa. Lähdetään olettamuksesta, että tämä tila on käytettävissä, eikä sille aseteta etukäteen rajoituksia.

1 Lähteitä
* https://blog.demofox.org/2019/05/11/markov-chain-text-generation/
* https://www.geeksforgeeks.org/advantages-trie-data-structure/

