# Toteutusraportti

## Ohjelman toiminta


Lähdettäessä kasvattamaan Markovin ketjun astetta arvosta 0 ylöspäin, tuotetut lauseet alkavat vastata enemmän ja enemmän alkuperäisessä tekstissä olevia lauseita, kuten on odotettavissakin. Esimerkiksi kun käytetään lähdeaineistona _Kalevalaa_:
#### Markovin aste 0:
* _Hirvet niin riuuttele hännät sitte ilman luopui kultaisemme._
* _Suurimpia terhenisen kumottamatta tuosta miniä kuvoasi äitteleikse tähän._
* _Kuvoannasta nuorukainen kaiketi mieli on ristin katala taikka._

#### Markovin aste 1:
* _Kynnykset kykertelihe hienohelman hempujaista ovet vahvat paukahteli kalliot._
* _Nyt suolle viety eikä päiveä rukoelevi ututyttö terhenneiti._
* _Tällä inhalla iällä katovalla kannikalla lauloi päivät pilviset._

#### Markovin aste 2:
* _Elossa vieri valkamavesille ei venettä valkamassa tuosta tunsi._
* _Valkamansa entiset elosijansa mäet tunsi mäntyinensä kummut kaikki._
* _Kukkalatva lausui lakkapää petäjä voipa miestä mieletöintä kehuit._

#### Markovin aste 3:
* _Leipojaksi siitä vanha väinämöinen sormin suistuvi sulahan käsin._
* _Vaaran käy vaaran vasenta puolta tuostapa joki tulevi._
* _Vesille yksi lypsi mustan maion siitä syntyi meltorauta._

#### Markovin aste 4:
* _Havukka se on seppo ilmarinen itse tuon sanoiksi._
* _Aukeilta eipä vielä sieltäkänä ei perän pereäkänä kasvoi._
* _Kaikki kasvinkumppalini joien joukossa elelin kasvoin kanssa kasvinaian._

#### Markovin aste 5:
* _Rintahansa itse iskihe kärelle siihen surmansa sukesi kuolemansa._
* _Syylättelen panen aitan parven päähän luisten lukkojen sisälle._
* _Huolimatta poiastasi kun olen koville luotu pantu päiville._

## Ohjelman rakenne

Ohjelma koostuu viidestä lähdekooditiedostosta:
* `sentence_generator.py` sisältää `SentenceGenerator`-pääluokan, ja sen kautta ohjelma myös käynnistetään
* Trie-tietorakenne, johon sisään luettu teksti tallenetaan, on toteutettu kahdella eri tavalla:
  * `nodes.py` Nodes-luokassa puun haarat on tallennettu Pythonin Dictionary-olioon
  * `trie.py` TrieNode-luokassa, jota käytetään Trie-pääluokan kautta, puun haarat ovat Pythonin listatietorakenteessa
* `sentence_generator_ui.py` sisältää tekstipohjaisen, interaktiivisen käyttöliittymän koodin
* `time_report.py` sisältää koodin suoritusaikatestaukseen

## Tietorakenteet
Markovin ketjujen generoinnissa käytettävistä Trie-puista tehtiin kaksi vaihtoehtoista versiota, jotka pystyy valitsemaan käyttöliittymästä, tai `SentenceGenerator` -instanssia luotaessa. Koska `Node`-toteus käyttää hajautustauluun perustuvaa Pythonin Dictionary-rakennetta, on sen toiminta huomattavasti nopeampaa, kuin tavallisella listalla toteutettu `Trie`-luokka.

![Sanat Trie-puussa](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/sanat_puussa.svg)

### `Node`-luokka (_Dictionary_)
* Jokainen sana on talletettu avaimeksi lapsisolmut sisältävään Pythonin Dictionary-rakenteeseen.
* `Node`-solmuun itseensä ei sanaa tallenneta lainkaan, ainoastaan sen paino, eli esiintymistodennäköisyys.
* `Node`-luokan käyttäjällä on tieto puun juurisolmusta, eikä sitä ole talletettu omaan luokkaansa.

### `Trie`-luokka (_List_)
* Vaihtoehtoinen `Trie` ja `TrieNode` -toteutus
* `Trie` sisältää juurisolmun, sekä tarvittavat metodit rakenteen käsittelyyn.
* Varsinainen puu on tallennettu `TrieNode` -solmuihin, jotka sisältävät sekä sanan, sen painon, että lapsisolmut.
* Lapsisolmuja ei kuitenkaan ole tallennettu Dictionary-avaimeksi, vaan tavalliseen listaan

![Trie- ja Node-tietorakenteet](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/Trie_ja_Node-rakenteet.svg)

## Saavutetut aika ja tilavaativuudet

## Testisyötteet:

* _AA_BB_ -teksti on pituudeltaan 50000 sanaa ja sisältää vain sanoja "aa" ja "bb". Tekstissä ei ole muita rakenteita, kuin toisen sanan kaksinkertainen ilmaantuvuustodennäköisyys toisen sanan jälkeen.
* _Kalevala_ -teksti
### Tilavaatimus
Molemmat tietorakenteet on toteutettu täsmälleen samalla tavalla, ja niiden tilavaatimus on _O(nm)_ missä _n_ on syötetekstin pituus sanoina, ja _m_ on luodun puun syvyys. Puun syvyys on yksi enemmän, kuin sen luontiaikana määritetty maksimiarvo Markovin asteelle. Eli, jos puun syvyys on 6, pystyy siitä hakemaan enintään viidennen asteen Markovin ketjuja.

### Aikavaativuus Trie-puun muodostamiselle
Aikavaativuuden puun generoinnille tulisi olla _O(n)_, ja lineaarinen kasvu näkyykin hyvin _AA_BB_ -tekstin kohdalla molemmilla implementaatioilla:

![Trien rakennus aa bb -tekstille](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/build_aabb.png)

_Kalevala_-tekstin kohdalla tulee ilmeiseksi, kuinka paljon nopeampi _Dictionaryä_ käyttävä _Node_-implementaatio on:

![Trien rakennus Kalevalalle -tekstille molemmilla implementaatioilla](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/build_Kalevala.png)

Tulostamalla _Node_-ratkaisun erikseen, näemme että puu syntyy edelleen lineaarisessa ajassa suhteessa syötteen pituuteen. Ero implemntaatioiden välillä on siis ainoastaan vakiokertoimessa.

![Trien rakennus Kalevalalle -tekstille Node implementaatiolla](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/build_Kalevala_Node.png)

### Aikavaativuus lauseiden muodostamiselle

Lauseiden muodostuksen pahimman vaihtoehdon aikavastaavuus on _O(n)_ mutta todellisuudessa yksinkertaiselle _AA_BB_ -tekstille se on verrannollinen vain käytettyyn Markovin asteeseen. Tämä onkin loogista, sillä vain kaksi sanaa sisältävässä aineistossa ei lapsisolmuja jouduta juurikaan käymään läpi. Mielenkiintoista en, että _Dictionaryä_ käyttävä _Node_ on alle 20000 sanan mittaisilla syötteillä lähes kaksi kertaa listalla toteutettua _Trie_-tietorakennetta nopeampi, mutta tämän jälkeen ero katoaa:

![Lauseiden muodostus aa bb -tekstille](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/generation_aabb.png)

_Kalevala_-teksti on rakenteeltaan lähes päinvastainen: Erilaisia sanoja on lähes kolmasosa kokonaismäärästä. Ensisilmäyksellä hakunopeus näyttäisi muuttuvan epälineaarisesti:

![Lauseiden muodostus Kalevalalle -tekstille](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/generation_Kalevala.png)

Kääntämällä mitattava arvo nopeuden sijasta lauseenmuodostukseen meneväksi ajaksi, nähdään kuitenkin, että haut kasvavat lineaarisesti syötetkstin pituuden suhteen, kuten _O(n)_ ennustaakin:

![Lauseiden muodostus Kalevalalle -tekstille](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/generation_Kalevala_time.png)

## Puutteet ja parannusehdotukset
* Alkuperäisten ajatusten pohjalta luotu Node-tietorakenne on toteutettu turhan monimutkaiseksi, ja yhteensopivuuden saavuttamiseksi myös Trie-tietorakenne on samankaltainen
* Trie-tietorakenne kannattaisi luoda yleiskäyttöiseksi, jolloin sana (tai _token_) voisi olla mikä tahansa Pythonin objekti, jota voidaan käyttää _Dictionary_ -luokan avaimena
* Tkinter-yhteensopiva NetworkX-kirjasto tarjoaisi valmiiksi sekä tietorakenteet, että työkalut niiden visualisoimiseksi

## Lähteitä
* https://blog.demofox.org/2019/05/11/markov-chain-text-generation/
* https://www.geeksforgeeks.org/advantages-trie-data-structure/
* https://www.cs.jhu.edu/~langmea/resources/lecture_notes/tries_and_suffix_tries.pdf
* GUSFIELD, D. Algorithms on Strings, Trees, and Sequences : Computer Science and Computational Biology. Cambridge [England]: Cambridge University Press, 1997. ISBN 9780521585194. Disponível em: https://search-ebscohost-com.libproxy.helsinki.fi/login.aspx?direct=true&db=e000xww&AN=502387&site=ehost-live&scope=site. Acesso em: 13 nov. 2021.
