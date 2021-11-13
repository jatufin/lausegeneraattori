# Tiralab 2021, periodi 2
Koulutusohjelma: Tietojenkäsittelytieteen kandidaatti, Helsingin yliopisto

# Lausegeneraattori

# Suunnitteludokumentti

## Aikavaatimusanalyysi

### Puun muodostaminen korpuksesta
Pseudokoodissa käytetään esimerkkimerkkijonoa, jossa piste ```.``` vastaa mitä tahansa lopetusmerkkiä, ja kirjaimet ```A```, ```B``` ja ```C``` kokonaisia sanoja. Markovin ketjun maksimiasteeksi määritetään ```k=2```.

```
t = "AB.ABAC.BABA.CBB.BBB.
k=2
root = []

for i=0 to len(t)-1:
	current = root
	for j=i to i+k:           ## Tämä olisi täydellisessä suffiks-puussa: for j=i to len(t)-1
		if current[t[i]] == NULL:
			current[t[i]] = []
			current[t[i]].weight = 0
		current[t[i]].weight++
		current = current[t[i]]
		if t[i] == ".":
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

Lauseen hakeminen puusta kestää niin kauan kun vastaan tulee lopetusmerkki "```.```". Pahimmassa tapauksessa lähdeteksti ei sisällä sellaista lopetusmerkkiä ollenkaan. Aikavaatimukseksi muodostuu keskimääräinen sanojen määrä lopetusmerkkien välillä alkutekstissä.

```
t = "AB.ABAC.BABA.CBB.BBB.
s[0]="A"
s[1]="B"
k=2
words = "AB"
current = root

function get_words(s):
	while(true):
		new_word=get_word(s)
		words.addLast(new_word)
		if new_word == ".":
			return words
		s.removeFirst()
		s.addToLast(newWord)		
```
