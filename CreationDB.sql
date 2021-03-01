CREATE TABLE "JTANGUY"."SALARIES"
( "num" SMALLINT PRIMARY KEY,
  "nom" VARCHAR2(15) NOT NULL,
  "prenom" VARCHAR2(15) NOT NULL,
  "adresseIP" VARCHAR2(15) UNIQUE NOT NULL);

CREATE TABLE "JTANGUY"."PROXY"
( "id" SMALLINT PRIMARY KEY,
  "adresseIP" VARCHAR2(15),
  "jourheure" TIMESTAMP,
  "URL" VARCHAR2(250),
  foreign key ("adresseIP") references "SALARIES"("adresseIP"));


CREATE SEQUENCE sequence_num START WITH 1 INCREMENT BY 1;

INSERT INTO "JTANGUY"."SALARIES" ("num", "nom", "prenom", "adresseIP") values (sequence_num.nextVal, 'DUPOND', 'Marie', '192.168.2.2');
INSERT INTO "JTANGUY"."SALARIES" ("num", "nom", "prenom", "adresseIP") values (sequence_num.nextVal, 'DUBOIS', 'Paul', '192.168.2.1');
INSERT INTO "JTANGUY"."SALARIES" ("num", "nom", "prenom", "adresseIP") values (sequence_num.nextVal, 'DURANT', 'Quentin', '192.168.2.3');
INSERT INTO "JTANGUY"."SALARIES" ("num", "nom", "prenom", "adresseIP") values (sequence_num.nextVal, 'LEJAUNE', 'Laurence', '192.168.2.100');

CREATE SEQUENCE sequence_id START WITH 1 INCREMENT BY 1;
