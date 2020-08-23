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
