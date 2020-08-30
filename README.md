# Tietovisa
Tietokantasovellus

http://tietovisa2020.herokuapp.com/

Tämä tietokantasovellus soveltuu sekä hyöty- että hupikäyttöön. Ylläpitäjä voi luoda kyselyjä esim. opiskelukäyttöön 
tai tietovisa-hengessä ajanvietteeksi. Ylläpitäjä voi lisäksi tarkistaa sovellukseen rekisteröityneet käyttäjät, poistaa käyttäjän
tiedot sovelluksesta tai asettaa käyttäjän ylläpitäjäksi. Käyttäjät voivat vastata haluamiinsa kyselyihin (kerran per kysely) ja 
tarkastella tilastoja. Kysymyksien vastausvaihtoehdot toteutetaan automaattisesti tarkistettavina monivalintoina.

Perustoiminnot:

- uuden käyttäjätilin luominen
- kirjautuminen käyttäjätunnuksella ja salasanalla
- kaksi eri luokkaa: peruskäyttäjä ja admin
- adminilla mahdollisuus luoda uusia kyselyjä
- adminilla mahdollisuus tarkastella rekisteröityneitä käyttäjiä (käyttäjätunnukset)
- adminilla mahdollisuus poistaa käyttäjän tiedot tietokannasta tai asettaa käyttäjä ylläpitäjäksi
- käyttäjillä mahdollisuus valita haluamansa kysely
- kyselyn täyttämisen jälkeen automaattinen palaute
- tilastointi

Muita toiminnallisuuksia/teknisiä ominaisuuksia:

- käyttäjätilin luonnissa kentät eivät salli tyhjiä tai liian pitkiä syötteitä
- uuden kyselyn laatimista varten luodut kentät eivät salli tyhjiä tai liian pitkiä syötteitä
- sopimaton manuaalinen navigointi selaimen osoiterivin kautta estetty (vain kirjautunut käyttäjä pääsee tarkastelemaan sovelluksen
sivuja, vain admin pääsee kyselyjen luontiin, käyttäjä ei pääse katselemaan tekemättömien kyselyiden tulossivuja, jne)
- etusivu kertoo kyselyjen kokonaismäärän ja näyttää kyselyt, joihin käyttäjä ei ole vielä vastannut
- käyttäjä voi vastata kyselyyn vain kerran (ei pääse vastaamaan uudestaan selaimen taaksepäin-toiminnolla, eikä osoiterivin avulla)
- sovellus ei salli kokonaan tyhjän kyselyn lähettämistä, vähintään yksi vastaus vaaditaan
- vastaamisen jälkeen käyttäjä näkee oikeiden vastauksiensa määrän sekä kysymyskohtaisesti oikeat ja valitsemansa vastaukset
- käyttäjä saa samalla "pisteidensä" perusteella sanallisen palautteen sattumanvaraisesti muutamasta vaihtoehdosta
- tilastoissa rekisteröintitiedot (milloin ja monesko käyttäjä)
- tilastoissa omien oikeiden vastauksien kokonaismäärä ja (enintään) TOP-5 eniten oikeita vastauksia omaavat käyttäjät
- tilastoissa linkit käyttäjän jo tekemiin kyselyihin




Kommentti: (Lopullinen palautus 30.8.2020)

Sovellus sisältää ne ominaisuudet, joita alkuperäisessä suunnitelmassa hahmottelin. Matkan varrella uusia ideoita syntyi lisää ja 
niistäkin sain osan toteutettua. Toteuttamatta jääneisiin ideoihin kuuluu mm. toiminto, joka olisi näyttänyt tilastoissa myös 
TOP-5 prosentuaalisesti eniten oikeita vastauksia omaavat käyttäjät ja toiminto, jolla olisi voinut poistaa tietyn visan sovelluksesta. 
Lisäksi muutama (mielestäni ei-niin-tärkeä) edge case jäi korjaamatta, joita ovat mm:\
Tilanne, jossa kirjautumaton käyttäjä navigoi osoitepalkin kautta new-sivulle, johtaa Not Found-ilmoitukseen.\
Tilanne, jossa Herokun Postgres-tietokannan pääavain hyppää eteenpäin itsestään, johtaa virheelliseen tietoon tilasto-sivulla siitä, 
monesko rekisteröitynyt käyttäjä oli. (Tällaisen tilanteen olen huomannut toistaiseksi vain kerran.)\
Myös ulkoasuun jäi hiomattomia kohtia.

Yleisesti sovelluksen ulkoasusta olsi todennäköisesti tullut elegantimpi esim. Bootstrap-kirjastolla ja toisaalta käyttäjäkokemuksesta 
varmasti "responsiivisempi" JavaScriptiä hieman sekaan laittamalla, mutta päätin toteuttaa sovelluksen selväpiirteisellä HTML/CSS-linjalla 
(ilman pop-uppeja tms). Todettakoon myös, että tämä oli minulle ensimmäinen web-sovellus ja HTML/CSS:n osalta lähdin liikkelle melko lailla
nollista, mitä nyt Lapio-kurssilla olin hieman pintaa raapaissut. Tältä pohjalta tuntui tarkoituksenmukaisemmalta tutustua HTML- ja CSS-kielten
perusteisiin ilman, että olisin lähtenyt lisäksi rakentamaan ulkoasua tai ominaisuuksia Bootstrapin ja/tai JavaScriptin avulla.

"Konepellin alla" olen tyytyväinen sovelluksen tiedostorakenteeseen, tietokantaan, Python-koodiin ja SQL-kyselyihin. 
Html-koodiin jäi parantamisen varaa.

Sovellusta voi testata osoitteessa https://tietovisa2020.herokuapp.com/ luomalla uuden käyttäjätunnuksen ja/tai käyttämällä admin-tason käyttäjätunnusta:
<br/><br/>
<b>Käyttäjätunnus: Sysop

Salasana: admin</b>
<br/><br/>


![Tietokantakaavio](/db.png)
