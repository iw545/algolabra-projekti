# Viikkoraportti 6

---

Tällä viikolla enimmäkseen muutin ohjelman rakennetta selkeämpään muotoon. Siirsin tekoälyn logiikkaa
käsittelevän osion omaan tiedostoon "ai.py", jottei ihan kaikki metodit ole samassa tiedostossa mikä
hankaloittaa koodin lukemista. Vähän myös yksikkötestejä tein, saman kaltaisia yksinkertaisia testejä
kuin edellisellä viikolla, vielä vähän epäselvä minkälaisia testejä vielä tehdä lisäksi. Pitää paremmin
lukea vielä testikattavuuden dokumentaatiosta ohjeita.

Käytin myös aikaa vähän asian tutkimiseen ja toteuttamiseen miten ohjelman tiedot tallennetaan tiedostoon,
jotta esim. ai logiikan tiedot eivät resetoi joka kerta kun ohjelman käynnistää uudelleen ja tekoäly
voi oppia paremmin tämän myötä. Tästä tiedon tallentamisesta esim. .txt tai .json tiedostoon opin, tällä hetkellä
.json tiedostoon tallentaminen mielestäni oli selkeämmän oloinen vaihtoehto. Vaikutti suurimmaksi osaksi helpolta, mutta vielä 
jäi epäselväksi miten esim luokan MarkovChain jokaisen eri markov mallin omat tiedot tallennetaan oikeaoppisesti, en tarpeeksi vielä 
perehtynyt tähän ja en lisännyt tällä viikolla koodiin näitä osioita repositorioon kun ei toiminut vielä niin kuin pitää.
Yritän tätä vielä saada toimimaan viimeisillä viikoilla ennen lopullista palautusta.

Myös pyrin seuraavaksi selkeyttämään koodin rakennetta enemmän ja mahdollisesti main.py tiedostossa tekemään
pariin eri metodiin osan play metodin toiminnasta selkeyttämään rakennetta vielä enemmän. Edelleen vielä
testaus ja toteutusdokumenttia tarvitsee kirjoittaa, mikä jälleen jäi tekemättä kunnolla. Käyttöohjettakin
pitäisi alkaa kirjoittamaan.

---

Käytin tällä viikolla aikaa noin 7 tuntia.