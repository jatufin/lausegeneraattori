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

### Suorituskyky

Tietorakenteiden suorituskykyvertailua, ja niiden vastaavuutta alkuperäisiin aikavaatimusarvioihin varten on luotu testausohjelma: ```time_report.py```. Tähän pääsee käsiksi ohjelman käyttöliittymästä.

### Ohjelman toiminnan oikeellisuus

Tuotetut lauseet alkavat vastata lähemmin ja lähemmin alkutekstiä, kun niitä tuotettaessa Makovin aste kasvaa. Esimerkkejä on [Toteutusraportissa](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/Toteutusraportti.md)

Yksikkötesteissä testataan, että alkeistapaukset, kuten tyhjä tai yhden tai kahden sanan mittainen syöte, toimivat. 

Tarkempaa analyysiä varten on luotu ohjelmaosio ```output_diagnose.py```, joka vertaa tuotettujen sanalistojen ominaisuuksia verrattuna alkuperäiseen tekstiin. Tarkemmin sanoen tuotetuissa lauseissa olevien _n_-pituisia sanaketjuja seuraavien sanojen esiintymistiheyksiä verrataan samoja sanaketjuja alkuperäistekstissä seuraavien sanojen tiheyteen.

Nähdään, että mitä enemmän lauseita tuotetaan, sitä tarkemmin nämä vastaavat toisiaan. Lisäksi sillä, käytetään _Trie_ vai _Node_ -tietorakennetta ei ole vaikutusta:

Alla olevasta kuvaajasta näkyy, että kun tuotettujen listojen määrä kasvaa, sanojen ilmenemistodennäköisyydet lähestyvät alkuperäisen tekstin vastaavia lukuja, kuten pitääkin. Eroja ei myöskään ilmene tuloksissa Node- ja Trie-tietorakenteiden välillä:

Node-tietorakennetta käyttäen ajettu analyysi alkeelliselle "aa bb" -korpukselle, kun tuotetum lauseet ovat 7 sanan pituisia:
![Kuvaaja](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/output_diagnose_aabb_Node.png)

Trie-tietorakennetta käyttäen ajettu analyysi alkeelliselle "aa bb" -korpukselle, kun tuotetum lauseet ovat 7 sanan pituisia:
![Kuvaaja](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/output_diagnose_aabb_Trie.png)

Tulosten poikkeama pienenee huomattavasti hitaammin, kun korpuksena on paljon enemmän sanoja sisältävä Kalevala, mutta lauseiden pituus edelleen vain 7 merkkiä:
![Kuvaaja](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/output_diagnose_Kalevala_Node.png)

Tehtäessä ajo suurille lausemäärille käyrän muoto tulee ilmeiseksi.
![Kuvaaja](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/output_diagnose_Kalevala_Node_long.png)

Kaiken kaikkiaan sanojen esiintymistodennäköisyydet sanayhdistelmien jälkeen vastaavat niitä, mitä lähdetekstissäkin ilmenee, alkaen Markovin asteesta 0, jolloin jokaisen sanan esiintymistodennäköisyys vastaa kyseisen sanan ilmenemismäärien suhdetta koko tekstin pituuteen. Ohjelma siis tuottaa sellaisia sanaketjuja, kuten pitääkin.



