CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    password TEXT
)

CREATE TABLE quiz (
    id INTEGER PRIMARY KEY,
    name TEXT,
    time_to_complete INTEGER
)

CREATE TABLE questions (
    quiz_id INTEGER,
    description TEXT
)

CREATE TABLE answers (
    question_id INTEGER,
    description TEXT,
    is_true BOOLEAN
)

--история проведения опросов по пользователю
CREATE TABLE user_history (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    time_spend INTEGER
)

CREATE TABLE user_answers (
    answer_id INTEGER,
    complete_time INTEGER
)