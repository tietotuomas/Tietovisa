CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY, 
    topic TEXT
);
CREATE TABLE questions (
    id SERIAL PRIMARY KEY, 
    content TEXT,
    quiz_id INTEGER REFERENCES quizzes
);
CREATE TABLE answers (
    id SERIAL PRIMARY KEY, 
    content TEXT,
    question_id INTEGER REFERENCES questions,
    correct BOOLEAN
);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    admin BOOLEAN,
    created_at TIMESTAMP
);
CREATE TABLE user_answers ( 
    user_id INTEGER REFERENCES users,
    answer_id INTEGER REFERENCES answers
);
INSERT INTO users (username, password, admin, created_at) VALUES ('Sysop', 'pbkdf2:sha256:150000$oe3RO5xV$8ce516a4e8507953ea5ad617b0a76c3291bc7454008525dbac8ddd013a871b09',
TRUE, NOW());
INSERT INTO quizzes (topic) VALUES ('Matematiikkaa englanniksi');
INSERT INTO quizzes (topic) VALUES ('Googlatuin tv-sarja');
INSERT INTO quizzes (topic) VALUES ('Katukuulustelu Helsinki');
INSERT INTO quizzes (topic) VALUES ('Jääkiekkoilijoiden lempinimet');
INSERT INTO questions (content, quiz_id) VALUES ('Mitä on vähentää englanniksi?', 1);
INSERT INTO questions (content, quiz_id) VALUES ('Mitä on yhteenlasku englanniksi?', 1);
INSERT INTO questions (content, quiz_id) VALUES ('Mitä on kertoma englanniksi?', 1);
INSERT INTO questions (content, quiz_id) VALUES ('Mitä on tulo englanniksi?', 1);
INSERT INTO questions (content, quiz_id) VALUES ('Mitä on dividend suomeksi?', 1);
INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli maailmanlaajuisesti googlatuin tv-sarja vuonna 2019?', 2);
INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli maailmanlaajuisesti googlatuin tv-sarja vuonna 2012?', 2);
INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli googlatuin tv-sarja Suomessa vuonna 2018?', 2);
INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli googlatuin tv-sarja USA:ssa vuonna 2015?', 2);
INSERT INTO questions (content, quiz_id) VALUES ('Mikä oli maailmanlaajuisesti toisiksi googlatuin tv-sarja vuonna 2019?', 2);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa sijaitsee Kallvikintie?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa sijaitsee Salpausseläntie?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa sijaitsee Vuorenjuuri?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa sijaitsee Haartmaninkatu?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa Puistokatu?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa sijaitsee Kalastajatorppa?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Missä kaupunginosassa sijaitsee Kaari?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Millä kadulla sijaitsee Marski?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Millä kadulla sijaitsee Venäjän suurlähetystö?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Millä kadulla sijaitsee Kumpulan kampuksen Exactum-rakennus?', 3);
INSERT INTO questions (content, quiz_id) VALUES ('Kuka leijona-legenda tunnetaan myös nimellä "Brother Lion 79"?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Kuka leijona-legenda tunnetaan myös nimellä "Rautakansleri"?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Kuka aktiivipelaaja tunnetaan myös nimellä "Professori"?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Kuka aktiivipelaaja tunnetaan myös nimellä "Sasha"?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Millä nimellä Marko Anttila myös tunnetaan?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Millä nimellä Antti Pihlström myös tunnetaan?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Millä nimellä Veli-Matti Savinainen myös tunnetaan?', 4);
INSERT INTO questions (content, quiz_id) VALUES ('Millä nimellä Mikael Granlund myös tunnetaan?', 4);
INSERT INTO answers (content, question_id, correct) VALUES ('subtract', 1, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('distract', 1, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('submit', 1, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('fraction', 1, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('addiction', 2, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('multiply', 2, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('ordinal', 2, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('addition', 2, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('difference', 3, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('factorial', 3, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('permutation', 3, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('factory', 3, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('prompt', 4, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('product', 4, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('abdominal', 4, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('abduct', 4, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('erotus', 5, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('jakaja', 5, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('jaettava', 5, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('osamäärä', 5, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('American Ninja', 6, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('American Idol', 6, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Better Call Saul', 6, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Game of Thrones', 6, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Big Brother Brasilia', 7, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Gangnam Style', 7, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Breaking bad', 7, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Salatut Elämät', 7, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Salatut Elämät', 8, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Temptation Island Suomi', 8, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Selviytyjät Suomi', 8, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Love Island Suomi', 8, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Fear the Walking Dead', 9, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Breaking Bad', 9, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Better Call Saul', 9, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Prison Break', 9, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Orange is the New Black', 10, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Chernobyl', 10, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Stranger Things', 10, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('The Bold and The Beautiful', 10, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Vuosaaressa', 11, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Eirassa', 11, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Tapaninkylässä', 11, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pihlajistossa', 12, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Mellunmäessä', 12, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Laajasalossa', 12, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Paloheinässä', 13, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Herttoniemessä', 13, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Malminkartanossa', 13, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pasilassa', 14, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Meilahdessa', 14, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pikku Huopalahdessa', 14, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Puistolassa', 15, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Kaisaniemessä', 15, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Ullanlinnassa', 15, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Hakaniemessä', 16, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Niemenmäessä', 16, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Munkkiniemessä', 16, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Konalassa', 17, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Kannelmäessä', 17, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Kalasatamassa', 17, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Kaivokadulla', 18, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Mannerheimintiellä', 18, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Marsalkantiellä', 18, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Vironkadulla', 19, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Itäisellä Puistotiellä', 19, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Tehtaankadulla', 19, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Yliopistonkadulla', 20, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pietari Kalmin kadulla', 20, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Gustaf Hällströmin kadulla', 20, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Veli-Pekka Ketola', 21, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Jukka Tammi', 21, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Juhani Tamminen', 21, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Teemu Selänne', 21, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Olli Jokinen', 22, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Kalervo Kummola', 22, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Raimo Helminen', 22, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Teemu Selänne', 22, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Jesse Puljujärvi', 23, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Sebastian Aho', 23, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Patrik Laine', 23, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Teemu Pukki', 23, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Alexander Ovechkin', 24, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Sami Vatanen', 24, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Jonathan Huberdeau', 24, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Aleksander Barkov', 24, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Mörkö', 25, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Rölli', 25, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Trolli', 25, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pikku Myy', 25, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pille', 26, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pelle', 26, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Muna', 26, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Pillu', 26, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Terminaattori', 27, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Arska', 27, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Commando', 27, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Predaattori', 27, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Bruce', 28, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Finnish Baby Jesus', 28, TRUE);
INSERT INTO answers (content, question_id, correct) VALUES ('Mickey Mouse', 28, FALSE);
INSERT INTO answers (content, question_id, correct) VALUES ('Magic Mike', 28, TRUE);
