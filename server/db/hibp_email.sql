DROP TABLE emails;

CREATE TABLE emails (
    ID SERIAL PRIMARY KEY,
    email VARCHAR(255),
    num_of_breaches INT
)