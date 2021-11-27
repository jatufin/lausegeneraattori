# Tiralab 2021, periodi 2

# Lausegeneraattori

Opiskelija: Janne Tuukkanen
Koulutusohjelma: Tietojenkäsittelytieteen kandidaatti, Helsingin yliopisto

Pythonilla toteutettu lausegeneraattori, joka Markovin ketjuja hyödyntäen luo lauseenomaisia sanayhdistelmiä lähdetekstien ja käyttäjän antamien parametrien perusteella.

## Ohjelman suoritus

Ohjelma käynnistyy interaktiivisessa tilassa projektihakemistosta komennolla:
``´
    python3 src/sentence_generator.py
``´
Tai poetry-ympäristössä::
``´
	invoke start
``´

Valikko on suoraviivainen, mutta ensimmäiseksi tulee ladata tekstitiedosto valitsemalla ``´1``´ ja syöttämällä tiedoston nimi tai koko polku. Esimerkiksi projektihakemistossa ``´text/kalevala.txt``´. Nyt tekstejä voi tuottaa painamalla ``´<enter> ``´ -painiketta. Markov-astetta voi muuttaa, ja ohjelmalle voi antaa sanat, joilla muodostuvan lauseen haluaa alkavan.

Tuotetut lauseet eivät välttämättä ole valitun Markov-asteen pituisia, ja saattavat sisältää jopa ainoastaan lopetusmerkin. Tämä on ohjelman ominaisuus silloin, jos ensimmäistä sanaketjua haettaessa törmätäänkin puun haaraan, joka loppuu alkuunsa.

Testit voi käynnistää poetry-ympäristössä:
``´
	invoke test
``´	
Tai testikattavuusraportin luomiseksi:
``´
	invoke coverage-report
``´	


### Dokumentaatio
* [Määrittelydokumentti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/maarittelydokumentti.md)
* [Suunnitteludokumentti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/suunnitteludokumentti.md)
* [Testausdokumentti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/testausdokumentti.md)

### Viikkoraportit
* [Viikko 1](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-01.md)
* [Viikko 2](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-02.md)
* [Viikko 3](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-03.md)
* [Viikko 4](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-04.md)
