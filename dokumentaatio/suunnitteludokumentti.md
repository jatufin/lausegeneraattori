# Tiralab 2021, periodi 2
Koulutusohjelma: Tietojenkäsittelytieteen kandidaatti, Helsingin yliopisto

# Lausegeneraattori

# Suunnitteludokumentti

## Tietorakenteen käsittely

Syötetekstistä ei tehdä välivaiheena listaa, vaan sanat tallennetaan puuhun suoraan merkkijonosta, sen jälkeen kun se on esikäsitelty.

### Syötetekstin alustus
1. Kaikki tyhjät välimerkit (whitespace) korvataan välilyöntimerkillä (space)
2. Karsitaan syötteestä kaikki muut merkit, paitsi: ```[a-ö][A-Ö][0-9][-!?.]```
3. Lopetusmerkkien ```[!?.]``` eteen ja jälkeen lisätään välilyönti
2. Kaikki peräkkäin olevat välilyöntimerkit korvataan yhdellä välilyöntimerkillä

### Puun muodostaminen

On annettuna edellisessä vaiheessa alustettu merkkijono ```S```, sekä sen indeksi ```start = 0```.

On annettu haluttu puun syvyys ```m```

Parametri ```k``` kertoo Markovin ketjun maksimiasteen, jolloin puun syvyydeksi tulee ```k```+1.

Funktio ```next_word(S, start)``` palauttaa merkkijonon kohdasta ```S[start]``` seuraavan merkkijonossa ```S``` olevaan välilyöntiin asti, ja kasvattaa indeksin ```start``` arvoa tähän välilyöntiin asti.

Muuttuja ```root=[]``` osoittaa alussa tyhjään Hashtable-tietorakenteeseen.

```
while (word = next_word(S, start)) != NULL:
	current = root
	depth = 0
	i = start
	do:
		if current[word] == null:
	        current[word] = []          ## luodaan uusi haara
			current[word].weight = 0    ## Haaran paino muodostuu sanojen määrästä
		cuurent[word].weight++
		depth++
		current = current[word]
		if depth == m:
			break
	while(word = next_word(S, i)) != NULL	
```

### Painotuksista
Jokaiseen haaraan merkitään seuraavan sanan paino. Nämä asettuvat automaattisesti oikein, koska jos esimerkiksi sana *hopea* sijoitetaan syvyydelle 3 puussa, sitä edeltää jo tekstissä oikeasti esiintyvät kaksi sanaa. Sama sana *hopea* sijoitetaan kuitenkin puussa myös sen juureen, jolloin sen paino määräytyy riippumatta edeltävistä sanoista.

### Tekstin muuttaminen sanalistaksi

### Lauseen generointi
* Haluttu lauseen pituus on ```n``` sanaa
* Aluksi lause ```L``` on tyhjä
* Käyttäjä on antanut yhden tai useamman avainsanan
* Lähdössä tarvitaan haluttua astetta ```k``` vastaava lista ```H``` sanoja, joka vastaa jotain puun juuresta lähtevää haaraa
* Mikäli käyttäjä ei antanut yhtään sanaa, muodostetaan lista ```H``` puun juuresta satunnaisesti haarojen painoja noudattaen
* Mikäli käyttäjä antoi avainsanoja, seurataan niitä puun juuresta lähtien, kunnes ```H``` on muodostettu
* Mikäli satunnaisesti löytyvä puun haara on alle ```k``` sanaa pitkä, kopioidaan haara lauseeseen ```L``` ja lopetetaan
* Muussa tapauksessa asetetaan saatu ```k```-sanan ketju lauseen ```L``` alkuarvoksi
* Seurataan juuresta annettua ```k``` sanaa muodostavaa polkua
* Polun lopussa (eli ```k```+1 syvyydellä) kaarien painotusten suhteita painottaen valitaan seuraava sana
* Lisätään sana listaan ```L```
* Mikäli lista on ```n``` pitkä, lopetataan
* Poistetaan listasta   ```H``` ensimmäinen sana ja lisätään loppuun nyt löytynyt uusi sana
* Toistetaan haku juuresta
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanan synonyymien käsittely.
* Ohjelmaan on mahdollisuus myöhemmin lisätä avainsanan taivutusmuotojen käsittely.

## Aikavaatimusanalyysi

### Puun muodostaminen korpuksesta
Pseudokoodissa käytetään esimerkkimerkkijonoa, haluttu puun syvyys on ```m``` sanaa. Kirjaimet ```A```, ```B``` ja ```C``` vastaavat kokonaisia sanoja, eikä välejä ole. Markovin ketjun maksimiasteeksi määritetään ```k=2```.

```
t = "ABABACBABACBBBBB
k=2
root = []

for i=0 to len(t)-1:
	current = root
	depth = 0
	for j=i to i+k:           ## Tämä olisi täydellisessä suffiks-puussa: for j=i to len(t)-1
		if current[t[j]] == NULL:
			current[t[j]] = []
			current[t[j]].weight = 0
		current[t[j]].weight++
		current = current[t[j]]
		depth++
		if depth == m:
			break;
```

Ulompi silmukka suoritetaan yhtä monta kertaa, kuin korpustekstissä on sanoja. Sisempi silmukka enintään vakio ```k``` kertaa.
Aikavaatimukseksi saadaan siis O(n).

Muodostuva puun syvyys Markovin aste ```k```+1 ja leveys enintään N*(k^2). Saadaan siis tilavaatimukseksi myös O(n).


### Yhden uuden sanan hakeminen puusta

```
t = "AB.ABAC.BABA.CBB.BBB.
s[0]="A"
s[1]="B"
k=2
current = root

function get_word(s):
	for i=0 to k-1:
		current = current[s[i]]
	
	weight_all=0
	for i=0 to len(current):
		weight_all += current[i].weight
	random_path = random(weight_all)
	n=0
	for i=0 to len(current):
		n += current[i].weight
		if random_path < n:
			new_word = current[i]

	return new_word
```

Uuden sanan hakeminonenpuusta tapahtuu siis vakioajassa O(1).

### Lauseen hakeminen puusta

Lauseen hakeminen puusta kestää niin kauan, kunnes se on ```m``` merkkiä pitkä.

```
t = "AB.ABAC.BABA.CBB.BBB.
s[0]="A"
s[1]="B"
k=2
m=8
words = "AB"
current = root

function get_words(s):
	while(true):
		new_word=get_word(s)
		words.addLast(new_word)
		if words.length() == m:
			return words
		s.removeFirst()
		s.addToLast(newWord)		
```

## Visualisointi

Tehdään työkalu puurakenteen tulostamiseksi helposti tarkasteltavassa muodossa:
```
root +---- 3 aaa +---- 1 bb ---- .
     |           |
     |           +---- 2 cc +---- 2 aaa --- .
	 |   		            |
     |                      +---- 1 bb --- .
	 |
     +---- 1 bb ---- 1 .
```
