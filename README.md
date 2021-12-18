# Tiralab 2021, periodi 2

# Lausegeneraattori

Opiskelija: Janne Tuukkanen
Koulutusohjelma: Tietojenkäsittelytieteen kandidaatti, Helsingin yliopisto

Pythonilla toteutettu lausegeneraattori, joka Markovin ketjuja hyödyntäen luo lauseenomaisia sanayhdistelmiä lähdetekstien ja käyttäjän antamien parametrien perusteella.

## Ohjelman toiminta
Käyttäjä antaa ohjelmalle tekstitiedoston, esimerkiksi Kalevalan, jonka ohjelma käsittelee ja jonka perusteella luodaan sisäinen tietorakenne. (Trie-puu) Tämän jälkeen ohjelma tuottaa pyydettäessä puusta sanaketjuja, "lauseita", Markovin ketjuja. Ohjelmalle voi määritellä halutun Markovin ketjun asteen ja sanan tai sanat, joilla haluaa lauseen alkavan, lisäksi annetaan tieto, kuinka monta sanaa muodostuvassa lauseessa halutaan olevan.

On huomioitava, että mitä suurempi Markov-ketjun aste tai pienempi lähdetekstin koko, sitä orjallisemmin ohjelma tuottaa suoria kopioita lähdetekstissä esiintyvistä lauseista.

## Ohjelman käynnistys

Ohjelma käynnistyy interaktiivisessa tilassa projektihakemistosta komennolla:


```
    python3 src/sentence_generator.py
```

Tai poetry-ympäristössä::

```
	invoke start
```

Valikko on suoraviivainen, mutta ensimmäiseksi tulee ladata tekstitiedosto valitsemalla `1` ja syöttämällä tiedoston nimi tai koko polku. Esimerkiksi projektihakemistossa `text/kalevala.txt`. Nyt tekstejä voi tuottaa painamalla `<enter>` -painiketta. Markov-astetta voi muuttaa, sekä muodostuvan lauseen pituutta,ja ohjelmalle voi antaa sanat, joilla muodostuvan lauseen haluaa alkavan.

Testit voi käynnistää poetry-ympäristössä:
```
	invoke test
```	
Tai testikattavuusraportin luomiseksi:
```
	invoke coverage-report
```	


### Dokumentaatio
* [Määrittelydokumentti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/maarittelydokumentti.md)
* [Suunnitteludokumentti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/suunnitteludokumentti.md)
* [Testausdokumentti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/testausdokumentti.md)
* [Toteutusraportti](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/Toteutusraportti.md)
### Viikkoraportit
* [Viikko 1](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-01.md)
* [Viikko 2](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-02.md)
* [Viikko 3](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-03.md)
* [Viikko 4](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-04.md)
* [Viikko 5](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-05.md)
* [Viikko 6](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-06.md)
* [Viikko 7](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/viikkoraportti-07.md)
