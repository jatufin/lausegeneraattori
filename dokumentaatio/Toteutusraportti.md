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


### `Node`-luokka (_Dictionary_)
* Jokainen sana on talletettu avaimeksi lapsisolmut sisältävään Pythonin Dictionary-rakenteeseen.
* `Node`-solmuun itseensä ei sanaa tallenneta lainkaan, ainoastaan sen paino, eli esiintymistodennäköisyys.
* `Node`-luokan käyttäjällä on tieto puun juurisolmusta, eikä sitä ole talletettu omaan luokkaansa.

### `Trie`-luokka (_List_)
* Vaihtoehtoinen `Trie` ja `TrieNode` -toteutus
* `Trie` sisältää juurisolmun, sekä tarvittavat metodit rakenteen käsittelyyn.
* Varsinainen puu on tallennettu `TrieNode` -solmuihin, jotka sisältävät sekä sanan, sen painon, että lapsisolmut.
* Lapsisolmuja ei kuitenkaan ole tallennettu Dictionary-avaimeksi, vaan tavalliseen listaan

## Saavutetut aika ja tilavaativuudet

### Tilavaatimus
Molemmat tietorakenteet on toteutettu täsmälleen samalla tavalla, ja niiden tilavaatimus on _O(nm)_ missä _n_ on syötetekstin pituus sanoina, ja _m_ on luodun puun syvyys. Puun syvyys on yksi enemmän, kuin sen luontiaikana määritetty maksimiarvo Markovin asteelle. Eli, jos puun syvyys on 6, pystyy siitä hakemaan enintään viidennen asteen Markovin ketjuja.

### Aikavaativuus
Aikavaativuuden puun generoinnille tulisi olla _O(n)_, eli sen pitäisi kasvaa lineaarisesti. Tämä vahvistuu alustavasti tehdyillä raporttiajoilla:

![Trie build times](https://github.com/jatufin/lausegeneraattori/blob/master/dokumentaatio/trie_build_time.png)

## Puutteet ja parannusehdotukset

## Lähteet
