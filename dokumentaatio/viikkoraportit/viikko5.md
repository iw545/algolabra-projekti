# Viikkoraportti 5

---

Tällä viikolla jäi työskentely liian vähäksi, liian paljon oli tekemisten siirtämistä myöhemmälle mikä ei hyvä menettely.
Yksikkötestejä tein muutamat yksinkertaiset, lähinnä sellaisia mitkä testaavat palauttaako metodit sellaiset syötteet
mitä pitää. Coveragen mukaan testikattavuus oli ohjelman päätiedostossa vain 39%, eli pitää tehdä enemmän testejä
mitkä käyvät läpi enemmän koodirivejä. Ongelmaksi koitui vähän tässä se, miten paljon ohjelman logiikasta tapahtuu yhden
metodin sisällä, missä vaaditaan käyttäjältä manuaalinen syöte. Jotta yksikkötestejä pystyn tekemään laajemmin,
yritän refaktoroida ja muotoilla koodia paremmaksi, jotta metodissa jossa käyttäjältä kysytään syöte ei olisi
lähes yhtään mitään muuta niin yksikkötestien tekeminenkin helpottuisi kun voi keskittyä tarkempiin metodeihin
joilla jokaisella tarkemmat tarkoitukset. 

Onnistuin myös korjaamaan virheen, mikä aiheutti sen ettei tekoäly valinnut oikein omaa valintaansa. Yksinkertainen, 
mutta aluksi vaikeasti löydettävä ratkaisu kun tällä hetkellä koodin rakenne niin sekavasti rakennettu: tekoäly valitsi 
valintansa numeroista (1,2,3) vaikka piti valita kirjaimista (R,P,S). Vertaisarvioinnin palautteen perusteella onnistuin
myös paikantamaan toisen virheen, missä ohjelman logiikka haki väärän tiedon tekoälyn dictionarystä (merkkijonon sijaan haki
numeron).

Seuraavaksi siirryn vihdoin dokumentaation kirjoittamiseen testaus ja toteutusdokumenttien kohdalla. Otan myös huomioon ohjelman
parantamisen kannalta palautteen mitä vertaisarvioinnissa minulle kirjoitettiin, mitä oli kattava määrä. Pyrin myös yllä mainittuun
koodin rakenteen parantamiseen, jotta ei olisi niin sekava rakenne ja helpompi lukea ja että enemmän yksikkötestejä olisi
helpompi tehdä.

---

Ohjaajalle kysymys:

Onko ohjelman ydintoiminta tarpeeksi kattava? Jos ei, millä tavalla vielä olisi hyvä lisätä toiminnallisuutta ohjelman toimintaan?
Puuttuuko ohjelmasta jotain mitä olen mahdollisesti unohtanut tehdä mikä olisi hyvä jo olla tehtynä 
(muuta kuin nuo puuttuvat dokumentaatiot ja vähäiset yksikkötestit)?

---

Käytin tällä viikolla aikaa projektin parissa noin 7 tuntia.
