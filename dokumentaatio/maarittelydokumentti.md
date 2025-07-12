# Määrittelydokumentti

---

Käytän tässä projektissa ohjelmointikielenä Pythonia.

---

Toteutan kivi-sakset-paperi pelin, jossa pelin pelaaja pelaa tekoälyä vastaan.

Jokaisella kierroksella pelaaja valitsee jonkun vaihtoehdoista "kivi / sakset / paperi" ja tekoäly tekee samoin, jonka jälkeen tulee tieto
kumpi voitti kierroksen. Pelin edetessä tieto pelaajan käyttämistä vaihtoehdoista tallentuu taulukoihin / matriiseihin. Sitten seuraavilla kierroksilla 
tekoäly pyrkii ennakoimaan mitä vaihtoehtoa pelaaja todennäköisimmin käyttäisi. Tähän käytän Markovin ketjuja, jossa tekoäly vertailee tuloksia useamman 
muun tekoälyn kanssa testidataa hyödyntäen. Tekoäly yrittää valita todennäköisimmät vaihtoehdot näistä tietorakenteista johon pelaajan valinnat
tallentuvat. 

Aikavaativuuksista vähän huonosti onnistuin selvittämään tietoa tähän mennessä (miten Markovin ketjuihin liittyvät toiminnot kokonaisuudessaan vievät),
mutta esim. taulukosta / matriisista etsittävät tiedot pelaajan tekemistä valinnoista pitäisi suoriutua aika- ja tilavaativuuksissa 0(n) kun käydään
läpi lista kokonaan ja etsitään toistuvia ketjuja tehdyista valinnoista ja tiedon tallentaminen näihin tietorakenteisiin on vaativuuksiltaan 0(1).

---

Opinto-ohjelma johon kuulun on Tietojenkäsittelytieteen kandidaatti (TKT).
Projektin dokumentointiin käytetty kieli on suomi.

---

# Lähteet
https://arxiv.org/pdf/2003.06769
https://www.datacamp.com/tutorial/markov-chains-python-tutorial