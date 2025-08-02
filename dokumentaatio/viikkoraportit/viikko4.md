# Viikkoraportti 4

---

Tällä viikolla enimmäkseen kehitin ohjelman päälogiikkaa, miten ohjelma tallentaa ja käyttää hyödykseen
dataa defaultdict tietorakenteissa. Tällä hetkellä sen pitäisi toimia odotetulla tavalla ainakin
tiedon tallentamisen kannalta, mutta itse peliä pelatessa on ongelmia tekoälyn logiikan kohdalla vielä.
Joissain tilanteissa saman vaihtoehdon jatkuvaa valitsemista (kivi / paperi / sakset) monta kertaa peräkkäin
(esim kymmeniä kertoja) ei aiheuta sitä, että tekoäly vaihtaisi käyttämään oikeata vaihtoehtoa (esim kivi vastaan sakset).
En kunnolla vielä onnistunut testaamaan ja hahmottamaan missä vika on, mitä yritän ensi viikolla selvittää enemmän.

Opin hahmottamaan paremmin miten tietorakenteisiin tällaisessa pelissä tallennetaan tietoja ja mitä tietoja tulisi
tallentaa. Tällä hetkellä ohjelma tallentaa max 6 merkin merkkijonoja mitä pelaaja on pelannut edellisillä kierroksilla
(esim "kspksp") ja tallentaa aina sitten minkä valinnan pelaaja valitsi seuraavana ("kspks: p: 1 tyylisesti).

Yksikkötestaamista en vieläkään ole aloittanut, pyrin niitä tekemään ensi viikolla kiitettävän
määrän ja enemmän vielä vertaisarviointien jälkeen. Toteutusdokumentin kirjoittamistakaan en
vielä aloittanut, sitä olisi tarkoitus myös alkaa kirjoittamaan ensi viikolla toivon mukaan.

Tällä hetkellä koodin on jonkin verran monimutkainen / sekava rakenteeltaan. Ehkä olen tehnyt
liian monta metodia mikä jokainen käydään läpi jonomaisesti hyppien aina edellisestä seuraavaan, kunnes lopulta päästään
takaisin alkumetodiin. Tämä saattaa jonkin verran ennestään vaikeuttaa ongelmien selvitystä ja korjaamista, esim yllä mainittua
tekoälyn logiikan virheellisyyttä. En vielä ihan varma pitäisikö jotain esim refaktoroida järkevämmäksi luettavuudelta
ja toiminnan hahmottamisen kannalta.

---

Käytin tällä viikolla aikaa tämän projektin parissa noin 10 tuntia.
Suurin osa ajasta meni ohjelman ydin logiikan kehittämiseen ja miettimiseen / hahmottamiseen.
Aikaa myös meni aiemman koodin paranteluun ja tekemällä ohjelman testaamisesta miellyttävämpää 
(enemmän infoa printattuna peliä pelatessa).
