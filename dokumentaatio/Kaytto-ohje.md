# Käyttö-ohje

## Asennus

Ensimmäiseksi tulee ladata ja purkaa ohjelman julkaisun (release) zip-tiedosto:

[Loppupalautus](https://github.com/jatufin/lausegeneraattori/releases/tag/loppupalautus)

Tämän jälkeen siirrytään projektihakemistoon ja asennetaan riippuvuudet komennolla:


```
    poetry install
```

## Ohjelman käynnistys

Ohjelma käynnistyy interaktiivisessa tilassa projektihakemistosta komennolla:


```
	poetry run invoke start
```

Tai poetry-ympäristössä::

```
	invoke start
```

Testien ajo tapahtuu komennolla:
```
	poetry run invoke test
```	
Ja testikattavuusraportin voi luoda komennolla:
```
	poetry run invoke coverage-report
```	

## Ohjelman käyttö

Valikko on suoraviivainen, mutta ensimmäiseksi tulee ladata tekstitiedosto valitsemalla `1`. Ohjelma listaa tiedostot projektihakemiston `text` ja halutun tiedoston saa valittua antamalla sitä vastaavan numeron. Nyt tekstejä voi tuottaa painamalla `<enter>` -painiketta. Markov-astetta voi muuttaa, sekä muodostuvan lauseen pituutta,ja ohjelmalle voi antaa sanat, joilla muodostuvan lauseen haluaa alkavan.

### Päävalikko

#### 1 - Aseta ja lue tiedosto
Listaa ./text -alahakemiston sisällön ja antaa valita halutun tiedoston

#### 2 - Vaihda generaattoria
Antaa mahdollisuuden valita eri implementaatioiden välillä.

#### 3 - Vaihda Markov-aste
Vaihtaa Markovin asteen, jolla lauseita muodostetaan.

#### 4 - Anna lauseen aloittavat sanat
Tähän voi antaa sanat, joilla lause haluaa lauseen alkavan.

#### 5 - Anna haluttu lauseen pituus
Tuotettujen lauseiden pituus sanoina.

#### 6 - Tulosta tietorakenne
Tulostaa näytölle Trie-puun.

#### 7 - Aja aikaraportti
Tekee nyt valitulla tiedostoilla testit, kuinka pitkään Trie-puun muodostus, ja uusien lauseiden generointi kestää.
Tulokset tallentuvat CSV-tiedostoihin myöhempää analyysiä varten.

#### 8 - Aja tuotettujen lauseiden analyysi
Generoi lauseita ja vertaa niissä ilmeneviä sanoja alkuperäistekstin sanojen ilmenemistodennäköisyyksiin.
Tulokset tallentuvat CSV-tiedostoihin myöhempää analyysiä varten.

#### 0 - Lopeta

#### Lauseiden generointi
Aina pPainamalla `<enter>`-painiketta tulostuu näytölle lause. Takaisin päävalikkoon pääsee antamalla `0`.


