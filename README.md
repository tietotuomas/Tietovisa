# Tietovisa
Tietokantasovellus

http://tietovisa2020.herokuapp.com/

Tämä tietokantasovellus soveltuu sekä hyöty- että hupikäyttöön. Ylläpitäjä voi luoda kyselyjä esim. opiskelukäyttöön 
tai tietovisa-hengessä ajanvietteeksi. Käyttäjät voivat vastata haluamiinsa kyselyihin (kerran per kysely) ja tarkastella 
tilastoja. Kysymyksien vastausvaihtoehdot toteutetaan automaattisesti tarkistettavina monivalintointa.

Perustoiminnot:

- uuden käyttäjätilin luominen
- kirjautuminen käyttäjätunnuksella ja salasanalla
- kaksi eri luokkaa: peruskäyttäjä ja admin
- adminilla mahdollisuus luoda uusia kyselyjä
- käyttäjillä mahdollisuus valita haluamansa kysely
- kyselyn täyttämisen jälkeen automaattinen palaute
- tilastointi

Muita toiminnallisuuksia/teknisiä ominaisuuksia:

- käyttäjätilin kentät eivät salli tyhjiä tai liian pitkiä syötteitä
- uuden kyselyn laatimista varten luodut kentät eivät salli tyhjiä tai liian pitkiä syötteitä
- sopimaton manuaalinen navigointi selaimen osoiterivin kautta estetty (vain kirjautunut käyttäjä pääsee tarkastelemaan sovelluksen
sivuja, vain admin pääsee kyselyjen luontiin jne)
- etusivu kertoo kyselyjen kokonaismäärän ja näyttää kyselyt, joihin käyttäjä ei ole vielä vastannut
- käyttäjä voi vastata kyselyyn vain kerran (ei pääse vastaamaan uudestaan selaimen taaksepäin-toiminnolla, eikä osoiterivin avulla)
- sovellus ei salli kokonaan tyhjän kyselyn lähettämistä, vähitään yksi vastaus vaaditaan
- vastaamisen jälkeen käyttäjä näkee oikeiden vastauksiensa määrän sekä kysymyskohtaisesti oikeat ja valitsemansa vastaukset
- käyttäjä saa samalla "pisteidensä" perusteella sanallisen palautteen sattumanvaraisesti muutamasta vaihtoehdosta
- tilastoissa rekisteröintitiedot (milloin ja monesko käyttäjä)
- tilastoissa omien oikeiden vastauksien kokonaismäärä ja (enintään) TOP-5 eniten oikeita vastauksia omaavat käyttäjät
<br></br>
- <i>tilastoissa omat kysely-kohtaiset pisteet</i>
- <i>tilastoissa TOP-5 prosentuaalisesti eniten oikeita vastauksia omaavat käyttäjät</i>
- <i>adminille mahdollisuus poistaa tietyn käyttäjän tiedot tietokannasta</i>



<b>Välipalautus 23.8:</b>

Sovellus on näkemykseni mukaan hyvin aikataulussa. Olen pyrkinyt lisäämään toimintoja ja korjaamaan puutteita saadun palautteen perusteella,
tietysti myös omaan suunnitelmaan pohjautuen. Suunnitelmakin on ketterän kehityksen nimissä matkan aikana hieman mukautunut, mutta 
alkuperäinen visio on toteunut silti melko hyvin. Yläpuolella on listattuna sovelluksesta löytyviä toiminnallisuuksia ja ominaisuuksia.
Kursivoidut kohdat ovat puuttuvia ominaisuuksia, joita yritän viimeisen viikon aikana toteuttaa. Jos aikaa niiden ja mahdollisten parannus-
ehdotusten jäljiltä jää, myös sovelluksen ulkoasua olisi tarkoitus hieman hioa.

Sovellusta voi testata osoitteessa https://tietovisa2020.herokuapp.com/ luomalla uuden käyttäjätunnuksen ja/tai käyttämällä admin-tason käyttäjätunnusta:
<b>Käyttäjätunnus: Sysop
Salasana: admin</b>
<br/><br/>


![Tietokantakaavio](/db.png)
