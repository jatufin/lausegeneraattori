# Testausdokumentti

## Yleiskuvaus

* Yksikkötestauksessa käytetään *Pytest*-työkaluja
* Ohjelmassa mukana oleva mahdollisuus trie-tietorakenteen tulostamiseksi helpottaa visuaalista tarkastelua

## Yksikkötestaus
* Node-luokka (```node.py```) yksikkötestaus on kattava 99% (Yksi varoitus johtuu suunnitelman mukaisesta silmukasta poistumisesta)
* SentenceGenerator-luokan ```sentence_generator.py``` yksikkötestaus on kattava 85% (ulkopuolelle jää main() -metodi, joka käsittelee komentoriviargumentit)

### Testikattavuus
![coverage report](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/coverage_report.png)

## Käyttöliittymä

Tiedosto: ```sentence_generator_ui.py ```

Käyttöliittymä on jätetty automaattisen testauksen ulkopuolelle. Koska valikkorakenne on yksitasoinen, se on testattu kattavasti käsin:
* Päävalikko käynnistyy
* Päävalikko reagoi oikein kaikkiin syötteisiin: 1,2,3,4,0
* Päävalikko reagoi oikein virheellisiin syötteisiin
* Tiedoston avaus toimii oikealla tiedostonimellä
* Tiedoston avaus antaa oikean virheen virheellisellä tiedostonimellä
* Käytettävän Markovin asteen vaihto toimii
* Käytettävän Markovin asteen vaihto virheellisellä arvolla ei onnistu
* Lauseen aloitussanojen anto toimii
* Lauseiden muodostus toimii

## Komentoriviargumentit

Ohjelman kutsuminen komentoriviltä on testattu kattavasti manuaalisesti:
* Ilman argumentteja aukeaa interaktiivinen käyttöliittymä
* Tiedostonimi-argumentti käsitellään oikein
* Markovin aste -argumentti käsitellään oikein
* Avainsana -argumentit käsitellään oikein


## Laajempi testaus
Luodaan automaatiolla aineisto, joka sisältää sanoja, jotka seuraavat toisiaan tunnetuilla todennäköisyyksillä. Tällä aineistolla tehdään suuri määrä ajoja ja muodostetaan näistä yhdistetyn tekstin sanojen ilmenemisen tilastollista suhdetta alkuperäiseen testiaineistoon:

