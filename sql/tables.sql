CREATE DATABASE final_project; -psql-
DROP TABLE IF EXISTS note;
CREATE TABLE note (
       id SERIAL PRIMARY KEY,
       name TEXT UNIQUE NOT NULL,
       added DATE,
       description TEXT
       );
insert into note(name,added,description) values ('science','12-08-2020','oil foats on water');
insert into note(name,added,description) values ('social','10-08-2020','first world war_1914_1919');
insert into note(name,added,description) values ('bi0logy','18-08-2020','mitochondria-powerhouse');  
