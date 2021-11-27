## Viikko 3

Käytetty aika: 10 tuntia

### Viikolla tehdyt toimepiteet
* Korjattiin ja tarkennettiin määrittelyä
* Aloitettiin testausdokumentaatio
* Luotiin yleinen puutietorakenne (node.py) ja sille yksikkötestit
* Luotiin varsinainen SentenceGenerator -luokka
* Rakennettiin toiminnallisuus tekstin lukemiselle ja konvertoimiselle trie-tietorakenteeksi
* Luotiin myös metodit trie-tietorakenteen tulostamiseksi näytölle tarkastelua varten
* Päätettiin käyttää puun tallentamiseen JSON-formaattia, vaikkei se olekaan koon puolesta optimaalinen
* Päivitettiin dokumentaatiota formaatin osalta

### Tällä viikolla olen oppinut
* Pythonin Dictionary-luokan toimintaa
* Pytest-testikirjastojen toimintaa

### Vielä auki olevat asiat
* Testivektorit nyt toteutetulle tietorakenteen muodostamiselle
* Automatisoitu testaus varsinaiselle toiminnalle, kun sanalistojen generoinnissa on mukana satunnaisuus

### Seuraavat toimenpiteet
* Syötemerkkijonon esikäsittely
* Tarkempi testaus, että nyt toteutettu puun muodostus tapahtuu oikein
* SentenceGenerator-luokan yksikkötestaus
* Varsinainen toiminnallisuus, eli lauseiden muodostus satunnaisesti, painotuksia noudattaen
* Tietorakenteen tallennus ja luku JSON-muodossa
