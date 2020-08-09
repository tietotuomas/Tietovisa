# Tietovisa
Tietokantasovellus

http://tietovisa2020.herokuapp.com/

Tällä tietokantasovelluksella on mahdollista luoda kyselyjä opiskelukäyttöön tai esim. tietovisoja ajanvietteeksi. 
Sovelluksessa kysymyksien vastausvaihtoehdot toteutetaan automaattisesti tarkistettavina monivalintointa. 
Kyselyjen, kysymysten tai vastausten vaihtoehtojen (ml. oikeat vastausvaihtoehdot) määrää ei ole rajoitettu.

Perustoiminnot:

- uuden käyttäjän luominen
- kirjautuminen käyttäjätunnuksella ja salasanalla
- kaksi eri luokkaa: peruskäyttäjä ja admin
- adminilla mahdollisuus luoda uusia kyselyjä
- käyttäjillä mahdollisuus valita haluamansa kysely 
- automaattinen palaute kyselyn loputtua (mm. oikeiden vastauksien määrä)

Lisäominaisuuksia:
- tilastojen tarkastelu esim. kuinka usein kysymyksiin on vastattu oikein ja TOP-5 käyttäjät "eniten oikeita vastauksia"
- adminille mahdollisuus poistaa tietyn käyttäjän tiedot tietokannasta
- adminille erillinen näkymä?


<b>Välipalautus 9.8:</b>

Sovellus on vielä kaukana valmiista, mutta käsittääkseni linjassa tavoitteen <i>"sovelluksella on toimiva pohja ja keskeiset 
toiminnot ovat hyvässä vaiheessa"</i> kanssa. 

Tein aluksi kaiken python-koodin routes.py-moduuliin, mutta olen nyt eriyttänyt 
kirjautumisen ja rekisteröinnin tietokantatoiminnot omaan moduuliin, tarkoitus eristää loputkin tietokantatoiminnot möyhemmin. 
Schema.sql-tiedostossa on tällä hetkellä CREATE TABLE-lauseiden lisäksi INSERT INTO-lauseet (tämä ei liene tarkoituksemukaista 
lopullisessa versiossa), joilla tietokantaan on luotu kaksi kyselyä. Olen ohjannut tämän tiedoston sisällön sekä paikalliseen 
että Herokun tietokantaan.

Perustoiminnot löytyvät sovelluksesta jollain tasolla lukuunottamatta adminin mahdollisuutta luoda uusia kyselyjä. Tämä on
tarkoitus luoda seuraavaksi, jonka jälkeen siirryn toteuttamaan "lisäominaisuuksia". Sovelluksen ulkoasuun tai vaadittuun 
tietoturvaan en ole vielä ehtinyt perehtyä - näihin on tarkoitus siirtyä, kunhan kaikki ominaisuudet on luotu.

Sovellusta voi testata herokussa (http://tietovisa2020.herokuapp.com/) luomalla uuden käyttäjätunnuksen ja vastaamalla kyselyihin. 
Tunnettu ongelma sovelluksessa on tilanne, jossa käyttäjä ei vastaa kaikkiin kysymyksiin.
<br/><br/>


![Tietokantakaavio](/db.png)
