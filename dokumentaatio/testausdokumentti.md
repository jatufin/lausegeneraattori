# Testausdokumentti

## Yleiskuvaus

* Yksikkötestauksessa käytetään *Pytest*-työkaluja
* Ohjelmassa mukana oleva mahdollisuus trie-tietorakenteen tulostamiseksi helpottaa visuaalista tarkastelua

## Yksikkötestaus
* Node-luokka (```node.py```) yksikkötestaus on kattava 99% (Yksi varoitus johtuu suunnitelman mukaisesta silmukasta poistumisesta)
* SentenceGenerator-luokan ```sentence_generator.py``` yksikkötestaus on kattava 85% (ulkopuolelle jää main() -metodi, joka käsittelee komentoriviargumentit)
* Trie- ja TrieNode -luokkien (```trie.py```) yksikkötestaukset ovat kattavia. Vastaavasti kuin edellä, ulkopuolelle jäävät ```print``` metodit ja yksittäinen poistuminen silmukasta suunnitellusti
* Käyttöliittymä ja aikaraportin generointi on jätetty yksikkötestauksen ulkopuolelle

### Testikattavuus
![coverage report](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/coverage_report.png)

## Käyttöliittymä

Tiedosto: ```sentence_generator_ui.py ```

Käyttöliittymä on jätetty automaattisen testauksen ulkopuolelle. Koska valikkorakenne on yksitasoinen, se on testattu kattavasti käsin:
* Päävalikko käynnistyy
* Päävalikko reagoi oikein kaikkiin syötteisiin: 1,2,3,4,5,6 ja 0
* Päävalikko reagoi oikein virheellisiin syötteisiin
* Tiedoston valinta ja avaus toimii oikein
* Käytettävän Markovin asteen vaihto toimii
* Käytettävän Markovin asteen vaihto virheellisellä arvolla ei onnistu
* Käytettävä lausegeneraattorin valinta ja vaihto toimivat
* Genroitavan lauseen pituuden asetus toimii
* Lauseen aloitussanojen anto toimii
* Lauseiden muodostus toimii

## Komentoriviargumentit

Ohjelman kutsuminen komentoriviltä on testattu kattavasti manuaalisesti:
* Ilman argumentteja aukeaa interaktiivinen käyttöliittymä
* Tiedostonimi-argumentti käsitellään oikein
* Markovin aste -argumentti käsitellään oikein
* Tuotettavan lauseen pituus -argumentti käsitellään oikein
* Avainsana -argumentit käsitellään oikein

## Laajempi testaus

Sama tietorakenne on toteutettu kahdella eri tavalla:
* Node-luokka käyttää Pythonin Dictionary -luokkaa puun haarojen säilyttämiseen
* Trie-luokka tallettaa haarat Pythonin listaan

Jo alustavasti ollaan nähty, että jälkimmäinen Trie-luokka toimii aineiston käsittelyssä oleellisesti ensimmäistä hitaammin. Tämän tukimiseksi ja yleensäkin aikaavtivuuksien tarkistamiseksi, on ohjelmassa aikaraportti -toiminto, joka tuottaa CSV-tiedostoihin mittausdataa annetun syötetiedoston perusteella.





