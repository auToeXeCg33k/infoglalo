--------------------------------------------------------
--  File created - Monday-May-10-2021   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Type AGGREGATE_TOPLIST_ENTRY_T
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TYPE "AGGREGATE_TOPLIST_ENTRY_T" IS OBJECT (username VARCHAR2(20), points NUMBER);

/
--------------------------------------------------------
--  DDL for Type AGGREGATE_TOPLIST_TABLE_T
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TYPE "AGGREGATE_TOPLIST_TABLE_T" 
IS TABLE OF aggregate_toplist_entry_t;


/
--------------------------------------------------------
--  DDL for Table ADOTTVALASZ
--------------------------------------------------------

  CREATE TABLE "ADOTTVALASZ" 
   (	"ID" NUMBER, 
	"VALASZJEL" VARCHAR2(20 BYTE), 
	"KERDESSZOVEG" VARCHAR2(500 BYTE), 
	"VALASZADO" VARCHAR2(20 BYTE), 
	"VALASZSZOVEG" VARCHAR2(500 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table BETUJEL
--------------------------------------------------------

  CREATE TABLE "BETUJEL" 
   (	"JEL" VARCHAR2(1 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table FORDULO
--------------------------------------------------------

  CREATE TABLE "FORDULO" 
   (	"VERSENYID" NUMBER, 
	"KEZDES" DATE, 
	"BESTOF" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table HIRDETES
--------------------------------------------------------

  CREATE TABLE "HIRDETES" 
   (	"ID" NUMBER, 
	"CIM" VARCHAR2(20 BYTE), 
	"SZOVEG" VARCHAR2(200 BYTE), 
	"PLAKAT" BLOB
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" 
 LOB ("PLAKAT") STORE AS SECUREFILE (
  TABLESPACE "USERS" ENABLE STORAGE IN ROW CHUNK 8192
  NOCACHE LOGGING  NOCOMPRESS  KEEP_DUPLICATES 
  STORAGE(INITIAL 106496 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) ;
--------------------------------------------------------
--  DDL for Table JATEKOS
--------------------------------------------------------

  CREATE TABLE "JATEKOS" 
   (	"FELHASZNALONEV" VARCHAR2(20 BYTE), 
	"EMAIL" VARCHAR2(20 BYTE), 
	"ADMIN" NUMBER(1,0), 
	"JELSZO" VARCHAR2(100 BYTE), 
	"NEHEZPONT" NUMBER DEFAULT 0, 
	"SALT" VARCHAR2(100 BYTE), 
	"SZULDATUM" DATE, 
	"KONNYUPONT" NUMBER DEFAULT 0, 
	"KOZEPESPONT" NUMBER DEFAULT 0
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table KERDES
--------------------------------------------------------

  CREATE TABLE "KERDES" 
   (	"SZOVEG" VARCHAR2(500 BYTE), 
	"TEMAKOR" VARCHAR2(20 BYTE), 
	"BETUJEL" VARCHAR2(1 BYTE), 
	"NEHEZSEG" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table KOZOSSEG
--------------------------------------------------------

  CREATE TABLE "KOZOSSEG" 
   (	"ID" NUMBER, 
	"NEV" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table KOZOSSEGTAGJA
--------------------------------------------------------

  CREATE TABLE "KOZOSSEGTAGJA" 
   (	"FELHASZNALONEV" VARCHAR2(20 BYTE), 
	"KOZOSSEG" NUMBER
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table PARBAJ
--------------------------------------------------------

  CREATE TABLE "PARBAJ" 
   (	"ID" NUMBER, 
	"PENDING" NUMBER(1,0), 
	"NYERTES" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table PARBAJKERDESE
--------------------------------------------------------

  CREATE TABLE "PARBAJKERDESE" 
   (	"ID" NUMBER, 
	"SZOVEG" VARCHAR2(500 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table PARBAJRAHIV
--------------------------------------------------------

  CREATE TABLE "PARBAJRAHIV" 
   (	"ID" NUMBER, 
	"JATEKOS" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table PARBAJRAHIVOTT
--------------------------------------------------------

  CREATE TABLE "PARBAJRAHIVOTT" 
   (	"ID" NUMBER, 
	"JATEKOS" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table PARBAJVALASZ
--------------------------------------------------------

  CREATE TABLE "PARBAJVALASZ" 
   (	"PARBAJID" NUMBER, 
	"JATEKOS" VARCHAR2(20 BYTE), 
	"VALASZ" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table TEMAKOR
--------------------------------------------------------

  CREATE TABLE "TEMAKOR" 
   (	"NEV" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table UTKOZET
--------------------------------------------------------

  CREATE TABLE "UTKOZET" 
   (	"VERSENYID" NUMBER, 
	"KEZDES" DATE, 
	"FELHASZNALONEV" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table UTKOZETKERDESE
--------------------------------------------------------

  CREATE TABLE "UTKOZETKERDESE" 
   (	"VERSENYID" NUMBER, 
	"SZOVEG" VARCHAR2(500 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table UTKOZETRESZVETEL
--------------------------------------------------------

  CREATE TABLE "UTKOZETRESZVETEL" 
   (	"VERSENYID" NUMBER, 
	"FELHASZNALONEV" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table UZENET
--------------------------------------------------------

  CREATE TABLE "UZENET" 
   (	"KULDO" VARCHAR2(20 BYTE), 
	"KOZOSSEG" NUMBER, 
	"IDOPONT" TIMESTAMP (0), 
	"SZOVEG" VARCHAR2(500 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table VALASZ
--------------------------------------------------------

  CREATE TABLE "VALASZ" 
   (	"SZOVEG" VARCHAR2(500 BYTE), 
	"BETUJEL" VARCHAR2(1 BYTE), 
	"KERDESSZOVEG" VARCHAR2(500 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table VERSENY
--------------------------------------------------------

  CREATE TABLE "VERSENY" 
   (	"ID" NUMBER, 
	"NEV" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into ADOTTVALASZ
SET DEFINE OFF;
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (5,'B','Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?','TESZT','45');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (6,'C','Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?','ADMIN','59');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (7,'B','Ki volt Az árvízi hajós?','TESZT','Wesselényi Miklós');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (9,'D','Ki volt a kalapos király?','ADMIN','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (0,'C','Mikor volt István, királlyá koronázása?','TESZT','1001. jan.21.');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (1,'A','Mikor volt István, királlyá koronázása?','ADMIN','1001. jan.1.');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (11,'D','Kik voltak a tatárok?','ADMIN','mongolok');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (13,'A','1995-ben ki volt az USA elnöke?','ADMIN','George W. Bush');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (16,'A','Ki nyerte az első magyar aranyérmet a Riói olimpián?','ADMIN','Szász Emese');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (18,'C','Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?','ADMIN','3');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (84,'A','Kinek a regénye a Gergő és az álomfogók?','leopph','Fekete István');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (85,'B','Ki írta Für Elise c. regényt?','leopph','Kaffka Margit');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (86,'C','Melyik irodalmi mű szereplője Csicsó?','leopph','Pál utcai fiúk');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (87,'A','Mi volt Szombahely ókori latin neve?','leopph','Savaria');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (88,'B','Hány gyermeke született Károly Walesi hercegnek?','leopph','négy');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (89,'B','Ki volt Az árvízi hajós?','leopph','Wesselényi Miklós');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (90,'D','Mennyi az elefántok vemhességi ideje?','leopph','22 hónap');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (91,'C','Hányszor erősebb a cápák szemlencséje az embernél?','leopph','7x');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (92,'D','Hány csigolyából áll a zsiráf nyaka?','leopph','27');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (93,'A','Mikor és hol rendezték meg az első nyári olimpiai játékokat?','leopph','1908 London');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (94,'B','Melyik sportolónk beceneve Madár?','leopph','Madár Ferenc');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (95,'B','Melyik város szülötte Vajda Attila kenus?','leopph','Sopron');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (96,'A','Mi volt Petőfi Sándor édesapjának foglalkozása?','leopph','ács');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (97,'A','Hány tagja van a Gyűrű szövetségének "A Gyűrűk urai" c. regényben?','leopph','7');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (98,'B','Mi az alliteráció?','leopph','betűrím');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (99,'B','Ádám melyik csontjából lett Éva?','leopph','bordájából');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (100,'A','Kik voltak a Küklopszok a görög mitológiában?','leopph','egyszemű óriások');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (101,'A','Melyik királyunk nevéhez fűződik az Aranybulla kiadása?','leopph','II. András');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (102,'A','Hány évente kerül megrendezésre a labdarúgó EB?','leopph','egy');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (103,'A','Mikor és hol rendezték meg az első nyári olimpiai játékokat?','leopph','1908 London');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (104,'B','Melyik város szülötte Vajda Attila kenus?','leopph','Sopron');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (105,'B','Melyik sportolónk beceneve Madár?','leopph','Madár Ferenc');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (107,'B','Ádám melyik csontjából lett Éva?','leopph','bordájából');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (110,'D','Szilágyi Áron melyik sportág olimpiai bajnoka?','leopph','ökölvívás');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (111,'D','Kik voltak a tatárok?','leopph','mongolok');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (114,'C','Ki volt Orpheusz felesége?','leopph','Pénelopé');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (115,'B','Ki volt a kalapos király?','TESZT','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (116,'A','Ki volt Gandalf, A Gyűrűk Ura trilógiában?','Sanyi','mágus');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (118,'D','Milyen állat a haris?','Sanyi','hüllő');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (122,'B','Keleti Ágnes melyik sportág olimpiai bajnoka?','Sanyi','torna');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (123,'C','Ki nyerte az első magyar aranyérmet a Riói olimpián?','Sanyi','Gyurta Dániel');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (124,'C','Szilágyi Áron melyik sportág olimpiai bajnoka?','Sanyi','atlétika');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (128,'B','Ki írta Für Elise c. regényt?','Sanyi','Kaffka Margit');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (129,'D','Kinek a regénye "A Mester és Margarita"?','Sanyi','Fjodor Mihajlovics Dosztojevszkij');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (130,'B','Csehov melyik művében szerepel Arkagyina?','Sanyi','Sirály');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (131,'A','Kinek a regénye a Gergő és az álomfogók?','Sanyi','Fekete István');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (132,'C','Kinek a regénye "A Mester és Margarita"?','Sanyi','Lev Tolsztoj');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (133,'D','Ki volt a kalapos király?','Sanyi','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (134,'B','Ki volt Hunyadi Mátyás anyja?','Sanyi','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (135,'C','1995-ben ki volt az USA elnöke?','Sanyi','Bill Clinton');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (137,'A','Milyen állat a haris?','Sanyi','hüllő');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (138,'C','Hányszor erősebb a cápák szemlencséje az embernél?','Sanyi','7x');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (139,'D','Hány csigolyából áll a zsiráf nyaka?','Sanyi','27');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (8,'B','Ki volt Az árvízi hajós?','ADMIN','Wesselényi Miklós');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (10,'C','Ki volt a kalapos király?','TESZT','I. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (12,'D','Kik voltak a tatárok?','TESZT','mongolok');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (14,'B','1995-ben ki volt az USA elnöke?','TESZT','Ronald Reagan');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (15,'A','Ki nyerte az első magyar aranyérmet a Riói olimpián?','TESZT','Szász Emese');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (17,'B','Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?','TESZT','2');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (81,'D','Hány évig élhet egy óriásteknős?','Béla','250-300 évig');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (82,'C','Melyik kontinensen él a jaguár?','Béla','Afrika');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (83,'B','Hol él a koala?','Béla','Ausztráliában');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (106,'A','Melyik sportolónk beceneve Madár?','Béla','Erdei Zsolt');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (108,'B','Ádám melyik csontjából lett Éva?','Béla','bordájából');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (109,'C','Szilágyi Áron melyik sportág olimpiai bajnoka?','Béla','atlétika');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (112,'D','Kik voltak a tatárok?','Béla','mongolok');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (113,'A','Ki volt Orpheusz felesége?','Béla','Eurüdiké');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (117,'C','Ki nyerte az első magyar aranyérmet a Riói olimpián?','Béla','Szász Emese');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (119,'A','Ki volt Gandalf, A Gyűrűk Ura trilógiában?','Béla','mágus');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (120,'B','Hány kötetből áll a Harry Potter?','Béla','7');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (121,'D','Melyik költő verse a Héja-nász az avaron?','Béla','Ady Endre');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (125,'A','Melyik háborúban volt a Barbadossa hadművelet?','Béla','harmadik világháború');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (126,'C','Ki volt Hunyadi Mátyás anyja?','Béla','Anjou Mária');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (127,'D','Ki volt a kalapos király?','Béla','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (136,'B','1995-ben ki volt az USA elnöke?','Józsi bácsi','Ronald Reagan');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (140,'B','Ki volt Hunyadi Mátyás anyja?','Józsi bácsi','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (141,'D','Ki volt a kalapos király?','Józsi bácsi','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (142,'D','Melyik költő verse a Héja-nász az avaron?','Józsi bácsi','Ady Endre');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (143,'A','Milyen állat Vuk, Fekete István regényében?','Józsi bácsi','róka');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (144,'C','Hány kötetből áll a Harry Potter?','Józsi bácsi','8');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (145,'A','Hány évente kerül megrendezésre a labdarúgó EB?','Józsi bácsi','egy');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (146,'D','Hol született Lionel Messi a híres focista?','Józsi bácsi','Spanyolországban');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (147,'B','Melyik sportolónk beceneve Madár?','Józsi bácsi','Madár Ferenc');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (148,'D','Ki volt a kalapos király?','Józsi bácsi','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (149,'B','Melyik háborúban volt a Barbadossa hadművelet?','Józsi bácsi','első világháború');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (150,'B','Ki volt Hunyadi Mátyás anyja?','Józsi bácsi','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (151,'A','Melyik sportolónk beceneve Madár?','Józsi bácsi','Erdei Zsolt');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (152,'C','Hol született Lionel Messi a híres focista?','Józsi bácsi','Argentínában');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (153,'C','Melyik város szülötte Vajda Attila kenus?','Józsi bácsi','Szeged');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (154,'B','Hol él a koala?','Józsi bácsi','Ausztráliában');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (155,'A','Hány évig élhet egy óriásteknős?','Józsi bácsi','150-200 évig');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (156,'C','Melyik kontinensen él a jaguár?','Józsi bácsi','Afrika');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (21,'D','Ki fedezte fel a déli sarkkört?','ADMIN','James Cook');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (22,'D','Ki fedezte fel a déli sarkkört?','TESZT','James Cook');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (25,'C','Hol született Lionel Messi a híres focista?','TESZT','Argentínában');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (26,'B','Hol született Lionel Messi a híres focista?','ADMIN','Brazíliában');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (27,'B','Szilágyi Áron melyik sportág olimpiai bajnoka?','TESZT','tőrvívás');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (31,'C','Melyik háborúban volt a Barbadossa hadművelet?','TESZT','második világháború');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (32,'A','1995-ben ki volt az USA elnöke?','TESZT','George W. Bush');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (33,'B','Ki volt a kalapos király?','TESZT','II. András');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (43,'C','Ki volt a kalapos király?','TESZT','I. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (44,'C','Ki volt a kalapos király?','TESZT','I. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (19,'C','Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?','TESZT','14');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (20,'D','Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?','ADMIN','15');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (45,'C','Ki volt a kalapos király?','TESZT','I. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (49,'C','Melyik háborúban volt a Barbadossa hadművelet?','TESZT','második világháború');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (50,'C','1995-ben ki volt az USA elnöke?','TESZT','Bill Clinton');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (51,'B','Ki volt Hunyadi Mátyás anyja?','TESZT','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (52,'B','Szilágyi Áron melyik sportág olimpiai bajnoka?','ADMIN','tőrvívás');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (65,'D','Ki volt a kalapos király?','ADMIN','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (66,'C','Ki volt a kalapos király?','TESZT','I. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (67,'C','Ki volt Orpheusz felesége?','TESZT','Pénelopé');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (68,'A','Ki volt Orpheusz felesége?','ADMIN','Eurüdiké');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (69,'C','Milyen állat a haris?','ADMIN','hüllő');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (70,'B','Ki volt Az árvízi hajós?','ADMIN','Wesselényi Miklós');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (71,'D','Kik voltak a Küklopszok a görög mitológiában?','ADMIN','egyszemű óriások');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (72,'A','Ki volt Gandalf, A Gyűrűk Ura trilógiában?','ADMIN','mágus');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (73,'D','Ki nyerte az első magyar aranyérmet a Riói olimpián?','ADMIN','Szász Emese');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (74,'D','Melyik költő verse a Héja-nász az avaron?','TESZT3','Ady Endre');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (75,'B','Szilágyi Áron melyik sportág olimpiai bajnoka?','TESZT3','kardvívás');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (76,'B','Hány csigolyából áll a zsiráf nyaka?','TESZT2','7');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (77,'A','Kinek a regénye "A Mester és Margarita"?','TESZT','Mihail Bulgakov');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (78,'C','Kinek a műve az Egyperces novellák?','TESZT','Örkény István');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (79,'B','Hány kötetből áll a Harry Potter?','TESZT','7');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (80,'A','Ki volt Gandalf, A Gyűrűk Ura trilógiában?','TESZT','mágus');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (2,'C','Ki volt Orpheusz felesége?','TESZT','Pénelopé');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (23,'C','Ki volt Orpheusz felesége?','TESZT','Pénelopé');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (24,'A','Ki volt Orpheusz felesége?','ADMIN','Eurüdiké');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (28,'C','1995-ben ki volt az USA elnöke?','TESZT','Bill Clinton');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (29,'B','Ki volt Hunyadi Mátyás anyja?','TESZT','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (30,'D','Ki volt a kalapos király?','TESZT','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (34,'B','Ki volt Hunyadi Mátyás anyja?','TESZT','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (35,'C','1995-ben ki volt az USA elnöke?','TESZT','Bill Clinton');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (36,'C','Melyik háborúban volt a Barbadossa hadművelet?','TESZT','második világháború');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (37,'B','Ki volt a kalapos király?','TESZT','II. András');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (38,'D','Ki volt Hunyadi Mátyás anyja?','TESZT','Mária Terézia');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (39,'A','1995-ben ki volt az USA elnöke?','TESZT','George W. Bush');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (40,'A','Ki volt Hunyadi Mátyás anyja?','TESZT','Morzsinai Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (41,'A','Melyik háborúban volt a Barbadossa hadművelet?','TESZT','harmadik világháború');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (42,'C','Ki volt a kalapos király?','TESZT','I. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (46,'D','Ki volt a kalapos király?','TESZT','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (47,'C','1995-ben ki volt az USA elnöke?','TESZT','Bill Clinton');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (48,'B','Ki volt Hunyadi Mátyás anyja?','TESZT','Szilágyi Erzsébet');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (53,'A','Kik voltak a Küklopszok a görög mitológiában?','TESZT','egyszemű óriások');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (54,'C','Kinek a műve az Egyperces novellák?','TESZT','Örkény István');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (55,'A','Ki volt Gandalf, A Gyűrűk Ura trilógiában?','TESZT','mágus');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (56,'D','Melyik költő verse a Héja-nász az avaron?','TESZT','Ady Endre');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (57,'C','Ki fedezte fel a déli sarkkört?','TESZT','Magellán');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (58,'D','Ki volt Orpheusz felesége?','TESZT','Élektra');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (59,'D','Ki volt a kalapos király?','TESZT','II. József');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (60,'A','Kik voltak a Küklopszok a görög mitológiában?','ADMIN','egyszemű óriások');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (61,'B','Hol él a koala?','ADMIN','Ausztráliában');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (62,'D','Milyen állat a bonobó?','ADMIN','madárfaj');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (63,'A','Mi a deres tapló?','ADMIN','gaz növény');
Insert into ADOTTVALASZ (ID,VALASZJEL,KERDESSZOVEG,VALASZADO,VALASZSZOVEG) values (64,'D','Ki nyerte az első magyar aranyérmet a Riói olimpián?','ADMIN','Hosszú Katinka');
REM INSERTING into BETUJEL
SET DEFINE OFF;
Insert into BETUJEL (JEL) values ('A');
Insert into BETUJEL (JEL) values ('B');
Insert into BETUJEL (JEL) values ('C');
Insert into BETUJEL (JEL) values ('D');
REM INSERTING into FORDULO
SET DEFINE OFF;
Insert into FORDULO (VERSENYID,KEZDES,BESTOF) values (3,to_date('22-MAY-21','DD-MON-RR'),4);
Insert into FORDULO (VERSENYID,KEZDES,BESTOF) values (1,to_date('31-MAY-21','DD-MON-RR'),4);
Insert into FORDULO (VERSENYID,KEZDES,BESTOF) values (2,to_date('27-MAY-21','DD-MON-RR'),6);
REM INSERTING into HIRDETES
SET DEFINE OFF;
Insert into HIRDETES (ID,CIM,SZOVEG) values (7,'BOJLER ELADÓ','eskü buszra kő...
');
Insert into HIRDETES (ID,CIM,SZOVEG) values (6,'Ezt itt a cím','Remélem ezt is elolvassa majd valaki, nem csak teszteli ezt a hirdetést. Olyan rossz, hogy senki nem jut el idáig :(
');
Insert into HIRDETES (ID,CIM,SZOVEG) values (8,'MegaHirdetés','Olyat hirdetek, a fal adja a másikat
');
Insert into HIRDETES (ID,CIM,SZOVEG) values (9,'INGYEN KÓLA','na jó nem...
');
REM INSERTING into JATEKOS
SET DEFINE OFF;
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('leopph','leopph@gmail.com',0,'$2b$12$zBkTZXMPYTvgfCMsN5Kcr.wjSXyfci8G4L3AsWdnykdx4WKoAcqui',3,'$2b$12$zBkTZXMPYTvgfCMsN5Kcr.',to_date('08-NOV-93','DD-MON-RR'),6,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('Sanyi','sanyi@sanyimail.com',0,'$2b$12$3fyF3DooSLQM/aAp/aU7NOuCgmh3R9aWxAvzfUMGuIQshPZUUCTw6',3,'$2b$12$3fyF3DooSLQM/aAp/aU7NO',to_date('01-SEP-39','DD-MON-RR'),5,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('TESZT','teszt@gmail.com',0,'$2b$12$zTp24tZbMAaBC1RQx.7XAOmJysGWs71TDtqR/.Woczc6RrJ78SrqW',3,'$2b$12$zTp24tZbMAaBC1RQx.7XAO',to_date('12-MAY-21','DD-MON-RR'),11,2);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('Béla','bela@gmail.com',0,'$2b$12$TGP7/x4SQzNfJidqAAtuOe92G/yCcxuc7YXq9olrMQ.gr6ddz9Cvm',3,'$2b$12$TGP7/x4SQzNfJidqAAtuOe',to_date('11-JAN-12','DD-MON-RR'),10,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('asd','asd@gmai.com',0,'$2b$12$nQRuToarscHp2DzUf7tWQOryGoPviu.epF.nYtOBCe37hT0sjigQe',0,'$2b$12$nQRuToarscHp2DzUf7tWQO',to_date('01-MAY-21','DD-MON-RR'),4,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('Józsi bácsi','jozsi@gmail.com',0,'$2b$12$XHAGWmzl4ASJR8jNih50NuSJZEU9FdNipmotn9n2ZnDrheQXETG0u',0,'$2b$12$XHAGWmzl4ASJR8jNih50Nu',to_date('07-OCT-65','DD-MON-RR'),7,2);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('ADMIN','admin@gmail.com',1,'$2b$12$DYxnB1/1FXPqNbC/DeoKUOv/Rznn2dZqAB00UZ/rso8eNG3Bplueu',3,'$2b$12$DYxnB1/1FXPqNbC/DeoKUO',to_date('01-MAY-21','DD-MON-RR'),5,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('TESZT2','teszt2@gmail.com',0,'$2b$12$2AQQDWELoh0pd.kTUWYbp.GdxXE6d0.dcEV9Y4OTcQyVK712ekF6C',3,'$2b$12$2AQQDWELoh0pd.kTUWYbp.',to_date('12-JAN-21','DD-MON-RR'),4,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('Atesz','asd@gmail.com',0,'$2b$12$hRbYzm9JRBQfrxIaS34wj.D0aU8RJ5cW4ueeEsg9YdxNu4SpcDlte',0,'$2b$12$hRbYzm9JRBQfrxIaS34wj.',to_date('11-MAY-21','DD-MON-RR'),4,0);
Insert into JATEKOS (FELHASZNALONEV,EMAIL,ADMIN,JELSZO,NEHEZPONT,SALT,SZULDATUM,KONNYUPONT,KOZEPESPONT) values ('TESZT3','teszt3@gmail.com',0,'$2b$12$8YAadSrDw40Kg1cf67RpQeGyUs/L7ZAhwSnEzP2q5bgGWLf/Omj72',0,'$2b$12$8YAadSrDw40Kg1cf67RpQe',to_date('21-MAY-21','DD-MON-RR'),5,0);
REM INSERTING into KERDES
SET DEFINE OFF;
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('A csigák melyik törzsbe tartoznak?','Élővilág','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Minek az energiáját használják fel az élőlények fotoszintéziskor?','Élővilág','D',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány lába van a póknak?','Élővilág','C',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Milyen állat terjeszti a sárgalázat?','Élővilág','C',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány vércsoport létezik?','Élővilág','C',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Milyen állat a bonobó?','Élővilág','C',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hol él a koala?','Élővilág','B',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mi a deres tapló?','Élővilág','D',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány évig élhet egy óriásteknős?','Élővilág','A',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik kontinensen él a jaguár?','Élővilág','A',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Milyen állat a haris?','Élővilág','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány csigolyából áll a zsiráf nyaka?','Élővilág','B',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mennyi az elefántok vemhességi ideje?','Élővilág','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hányszor erősebb a cápák szemlencséje az embernél?','Élővilág','C',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mikor volt István, királlyá koronázása?','Történelem','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Kik voltak a Küklopszok a görög mitológiában?','Történelem','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki volt Az árvízi hajós?','Történelem','B',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki fedezte fel a déli sarkkört?','Történelem','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('1995-ben ki volt az USA elnöke?','Történelem','C',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki volt Hunyadi Mátyás anyja?','Történelem','B',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Kik voltak a tatárok?','Történelem','D',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ádám melyik csontjából lett Éva?','Történelem','B',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik háborúban volt a Barbadossa hadművelet?','Történelem','C',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mikor gyártották az első Trabantot?','Történelem','B',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki volt a kalapos király?','Történelem','D',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki volt Orpheusz felesége?','Történelem','A',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mi volt Szombahely ókori latin neve?','Történelem','A',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány gyermeke született Károly Walesi hercegnek?','Történelem','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik királyunk nevéhez fűződik az Aranybulla kiadása?','Történelem','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mikor és hol rendezték meg az első nyári olimpiai játékokat?','Sport','B',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány évente kerül megrendezésre a labdarúgó EB?','Sport','D',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hol született Lionel Messi a híres focista?','Sport','C',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik sportolónk beceneve Madár?','Sport','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik város szülötte Vajda Attila kenus?','Sport','C',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Pályafutása során összesen hány aranyérmet szerzett Kovács István (Kokó)?','Sport','D',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Szilágyi Áron melyik sportág olimpiai bajnoka?','Sport','A',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki nyerte az első magyar aranyérmet a Riói olimpián?','Sport','A',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Keleti Ágnes melyik sportág olimpiai bajnoka?','Sport','B',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?','Sport','C',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?','Sport','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki Imre Géza párbajtőrvívó felesége?','Sport','A',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány érme van összesen Braun Ákos, cselgáncsozónak?','Sport','C',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mi a foglalkozása Mincza-Nébald Ildikó vivónőnek?','Sport','B',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Milyen magas Kásás Tamás vízilabdázó?','Sport','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik költő verse a Héja-nász az avaron?','Irodalom','D',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány kötetből áll a Harry Potter?','Irodalom','B',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki volt Gandalf, A Gyűrűk Ura trilógiában?','Irodalom','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Milyen állat Vuk, Fekete István regényében?','Irodalom','A',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Kinek a műve az Egyperces novellák?','Irodalom','C',0);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Kinek a regénye Az öreg halász és a tenger?','Irodalom','C',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik király léptet fakó lován Arany balladájában?','Irodalom','B',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mi volt Petőfi Sándor édesapjának foglalkozása?','Irodalom','D',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mi az alliteráció?','Irodalom','B',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány tagja van a Gyűrű szövetségének "A Gyűrűk urai" c. regényben?','Irodalom','B',1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ki írta Für Elise c. regényt?','Irodalom','C',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Csehov melyik művében szerepel Arkagyina?','Irodalom','B',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Melyik irodalmi mű szereplője Csicsó?','Irodalom','D',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Kinek a regénye a Gergő és az álomfogók?','Irodalom','C',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Kinek a regénye "A Mester és Margarita"?','Irodalom','A',2);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ha 1 hurkapálcának két vége van, 2 hurkapálcának négy vége van, akkor hány vége van 1 és fél hurkapálcának ?','IQ','C',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Egy juhásznak 17 báránya volt. Négy kivételével mind elpusztult. Hány maradt életben?','IQ','A',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Egy kosárban 5 alma van. Elveszel belőle kettőt. Mennyi marad neked?','IQ','B',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Lúdas Matyi Döbrögbe bandukol. Vele szembe jön 3 pandúr és 2 paraszt a 10 birkájával. Hányan mennek Döbrögbe?','IQ','B',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Mi az egyenlet megoldása: 6:2(1+2)=?','IQ','C',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('A varrónőnek van egy 16 méteres anyagdarabja, ebből naponta 2 métert levág. Hanyadik nap vágja le az utolsó darabot?','IQ','D',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Nagy úrnak és Nagynénak 4 lánya van. Mindegyik lánynak van egy bátyja. Hány gyereke van Nagyéknak?','IQ','A',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?','IQ','C',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Ausztria és Magyarország határára lezuhan egy repülőgép. Melyik országban temetik el a túlélőket?','IQ','D',-1);
Insert into KERDES (SZOVEG,TEMAKOR,BETUJEL,NEHEZSEG) values ('Hány 9 van 1-től 100-ig?','IQ','D',-1);
REM INSERTING into KOZOSSEG
SET DEFINE OFF;
Insert into KOZOSSEG (ID,NEV) values (4,'Proba');
Insert into KOZOSSEG (ID,NEV) values (7,'Proba4');
Insert into KOZOSSEG (ID,NEV) values (5,'Proba2');
Insert into KOZOSSEG (ID,NEV) values (6,'Proba3');
Insert into KOZOSSEG (ID,NEV) values (8,'Leopph Gaming');
Insert into KOZOSSEG (ID,NEV) values (0,'Forum');
Insert into KOZOSSEG (ID,NEV) values (3,'Animals');
Insert into KOZOSSEG (ID,NEV) values (1,'Social');
Insert into KOZOSSEG (ID,NEV) values (2,'Games');
REM INSERTING into KOZOSSEGTAGJA
SET DEFINE OFF;
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',1);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',2);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',3);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',4);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',5);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',6);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',7);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('ADMIN',8);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('Atesz',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('Béla',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('Józsi bácsi',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('Sanyi',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('Sanyi',3);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('Sanyi',8);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('TESZT',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('TESZT',1);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('TESZT',2);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('TESZT',8);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('TESZT2',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('TESZT3',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('asd',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('leopph',0);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('leopph',3);
Insert into KOZOSSEGTAGJA (FELHASZNALONEV,KOZOSSEG) values ('leopph',8);
REM INSERTING into PARBAJ
SET DEFINE OFF;
Insert into PARBAJ (ID,PENDING,NYERTES) values (0,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (1,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (13,0,'Béla');
Insert into PARBAJ (ID,PENDING,NYERTES) values (2,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (14,0,'Béla');
Insert into PARBAJ (ID,PENDING,NYERTES) values (3,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (5,0,'TESZT');
Insert into PARBAJ (ID,PENDING,NYERTES) values (7,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (8,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (9,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (10,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (11,0,'TESZT');
Insert into PARBAJ (ID,PENDING,NYERTES) values (12,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (4,0,'ADMIN');
Insert into PARBAJ (ID,PENDING,NYERTES) values (6,1,null);
REM INSERTING into PARBAJKERDESE
SET DEFINE OFF;
Insert into PARBAJKERDESE (ID,SZOVEG) values (0,'Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (1,'Ki volt a kalapos király?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (2,'Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (3,'Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (4,'Ki volt Orpheusz felesége?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (5,'Hol született Lionel Messi a híres focista?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (6,'Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (7,'Hányszor erősebb a cápák szemlencséje az embernél?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (8,'Hol született Lionel Messi a híres focista?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (11,'Kinek a regénye "A Mester és Margarita"?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (12,'Mikor és hol rendezték meg az első nyári olimpiai játékokat?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (13,'Melyik sportolónk beceneve Madár?');
Insert into PARBAJKERDESE (ID,SZOVEG) values (14,'Ki volt Orpheusz felesége?');
REM INSERTING into PARBAJRAHIV
SET DEFINE OFF;
Insert into PARBAJRAHIV (ID,JATEKOS) values (1,'ADMIN');
Insert into PARBAJRAHIV (ID,JATEKOS) values (0,'TESZT');
Insert into PARBAJRAHIV (ID,JATEKOS) values (13,'leopph');
Insert into PARBAJRAHIV (ID,JATEKOS) values (2,'TESZT');
Insert into PARBAJRAHIV (ID,JATEKOS) values (14,'Béla');
Insert into PARBAJRAHIV (ID,JATEKOS) values (3,'TESZT');
Insert into PARBAJRAHIV (ID,JATEKOS) values (5,'TESZT');
Insert into PARBAJRAHIV (ID,JATEKOS) values (4,'TESZT');
Insert into PARBAJRAHIV (ID,JATEKOS) values (6,'ADMIN');
REM INSERTING into PARBAJRAHIVOTT
SET DEFINE OFF;
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (1,'TESZT');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (0,'ADMIN');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (13,'Béla');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (2,'ADMIN');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (14,'leopph');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (3,'ADMIN');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (5,'ADMIN');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (4,'ADMIN');
Insert into PARBAJRAHIVOTT (ID,JATEKOS) values (6,'TESZT');
REM INSERTING into PARBAJVALASZ
SET DEFINE OFF;
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (0,'TESZT','B');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (0,'ADMIN','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (2,'ADMIN','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (1,'ADMIN','D');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (13,'leopph','B');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (14,'leopph','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (2,'TESZT','B');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (1,'TESZT','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (13,'Béla','A');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (14,'Béla','A');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (5,'TESZT','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (5,'ADMIN','B');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (1,'ADMIN','D');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (1,'TESZT','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (4,'TESZT','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (4,'ADMIN','A');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (3,'TESZT','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (3,'ADMIN','D');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (4,'TESZT','C');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (4,'ADMIN','A');
Insert into PARBAJVALASZ (PARBAJID,JATEKOS,VALASZ) values (6,'ADMIN','D');
REM INSERTING into TEMAKOR
SET DEFINE OFF;
Insert into TEMAKOR (NEV) values ('IQ');
Insert into TEMAKOR (NEV) values ('Irodalom');
Insert into TEMAKOR (NEV) values ('Sport');
Insert into TEMAKOR (NEV) values ('Történelem');
Insert into TEMAKOR (NEV) values ('Élővilág');
REM INSERTING into UTKOZET
SET DEFINE OFF;
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (2,to_date('10-MAY-21','DD-MON-RR'),'ADMIN');
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (2,to_date('10-MAY-21','DD-MON-RR'),'TESZT');
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (2,to_date('10-MAY-21','DD-MON-RR'),'TESZT2');
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (2,to_date('10-MAY-21','DD-MON-RR'),'leopph');
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (1,to_date('09-MAY-21','DD-MON-RR'),'TESZT2');
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (1,to_date('09-MAY-21','DD-MON-RR'),'ADMIN');
Insert into UTKOZET (VERSENYID,KEZDES,FELHASZNALONEV) values (1,to_date('09-MAY-21','DD-MON-RR'),'TESZT3');
REM INSERTING into UTKOZETKERDESE
SET DEFINE OFF;
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Egy juhásznak 17 báránya volt. Négy kivételével mind elpusztult. Hány maradt életben?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Hány csigolyából áll a zsiráf nyaka?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Hány lába van a póknak?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Ki volt Az árvízi hajós?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Ki volt Gandalf, A Gyűrűk Ura trilógiában?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Ki volt Orpheusz felesége?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Ki volt a kalapos király?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Kik voltak a Küklopszok a görög mitológiában?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Kinek a műve az Egyperces novellák?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Kinek a regénye "A Mester és Margarita"?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Melyik költő verse a Héja-nász az avaron?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Milyen állat a haris?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (1,'Szilágyi Áron melyik sportág olimpiai bajnoka?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (2,'Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (2,'Ki volt Gandalf, A Gyűrűk Ura trilógiában?');
Insert into UTKOZETKERDESE (VERSENYID,SZOVEG) values (2,'Milyen állat a haris?');
REM INSERTING into UTKOZETRESZVETEL
SET DEFINE OFF;
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (1,'ADMIN');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (1,'TESZT');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (1,'TESZT2');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (1,'TESZT3');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (2,'ADMIN');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (2,'Béla');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (2,'Sanyi');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (2,'TESZT');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (2,'TESZT2');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (2,'leopph');
Insert into UTKOZETRESZVETEL (VERSENYID,FELHASZNALONEV) values (3,'Béla');
REM INSERTING into UZENET
SET DEFINE OFF;
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('Sanyi',8,to_timestamp('10-MAY-21 04.30.10.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'Heló heló heló sziasztok');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('Sanyi',3,to_timestamp('10-MAY-21 04.31.49.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'én nagyon szeretem a tejet');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('leopph',3,to_timestamp('10-MAY-21 04.32.38.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'és a kakaót is?');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('Sanyi',3,to_timestamp('10-MAY-21 04.33.36.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'Azt is');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('Sanyi',8,to_timestamp('10-MAY-21 04.30.43.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'heló heló mizujs');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('TESZT',0,to_timestamp('09-MAY-21 11.38.24.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),'hello');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('ADMIN',4,to_timestamp('09-MAY-21 11.59.26.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),'lol');
Insert into UZENET (KULDO,KOZOSSEG,IDOPONT,SZOVEG) values ('TESZT',0,to_timestamp('09-MAY-21 01.00.03.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'szia mizujs');
REM INSERTING into VALASZ
SET DEFINE OFF;
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('puhatestűek','A','A csigák melyik törzsbe tartoznak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('gerinchúrosok','B','A csigák melyik törzsbe tartoznak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('egysejtűek','C','A csigák melyik törzsbe tartoznak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('ízeltlábúak','D','A csigák melyik törzsbe tartoznak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('víz','A','Minek az energiáját használják fel az élőlények fotoszintéziskor?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('hő','B','Minek az energiáját használják fel az élőlények fotoszintéziskor?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('szél','C','Minek az energiáját használják fel az élőlények fotoszintéziskor?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('napfény','D','Minek az energiáját használják fel az élőlények fotoszintéziskor?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('4','A','Hány lába van a póknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('6','B','Hány lába van a póknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('8','C','Hány lába van a póknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('12','D','Hány lába van a póknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('cecelégy','A','Milyen állat terjeszti a sárgalázat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('patkány','B','Milyen állat terjeszti a sárgalázat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('szúnyog','C','Milyen állat terjeszti a sárgalázat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('darázs','D','Milyen állat terjeszti a sárgalázat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('2','A','Hány vércsoport létezik?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('3','B','Hány vércsoport létezik?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('4','C','Hány vércsoport létezik?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5','D','Hány vércsoport létezik?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('hüllőfaj','A','Milyen állat a bonobó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('sárkányfaj','B','Milyen állat a bonobó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('majomfaj','C','Milyen állat a bonobó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('madárfaj','D','Milyen állat a bonobó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ázsiában','A','Hol él a koala?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ausztráliában','B','Hol él a koala?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Afrikában','C','Hol él a koala?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Dél-Amerikában','D','Hol él a koala?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('gaz növény','A','Mi a deres tapló?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('műveletlen ember','B','Mi a deres tapló?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('rovarféle','C','Mi a deres tapló?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('gombafajta','D','Mi a deres tapló?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('150-200 évig','A','Hány évig élhet egy óriásteknős?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('100-150 évig','B','Hány évig élhet egy óriásteknős?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('200-250 évig','C','Hány évig élhet egy óriásteknős?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('250-300 évig','D','Hány évig élhet egy óriásteknős?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Amerika','A','Melyik kontinensen él a jaguár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ausztrália','B','Melyik kontinensen él a jaguár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Afrika','C','Melyik kontinensen él a jaguár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ázsia','D','Melyik kontinensen él a jaguár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('hüllő','A','Milyen állat a haris?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('kétéltű','B','Milyen állat a haris?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('hal','C','Milyen állat a haris?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('madár','D','Milyen állat a haris?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('0','A','Hány csigolyából áll a zsiráf nyaka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('7','B','Hány csigolyából áll a zsiráf nyaka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('17','C','Hány csigolyából áll a zsiráf nyaka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('27','D','Hány csigolyából áll a zsiráf nyaka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5 hónap','A','Mennyi az elefántok vemhességi ideje?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('9 hónap','B','Mennyi az elefántok vemhességi ideje?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('12 hónap','C','Mennyi az elefántok vemhességi ideje?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('22 hónap','D','Mennyi az elefántok vemhességi ideje?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('3x','A','Hányszor erősebb a cápák szemlencséje az embernél?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5x','B','Hányszor erősebb a cápák szemlencséje az embernél?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('7x','C','Hányszor erősebb a cápák szemlencséje az embernél?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('10x','D','Hányszor erősebb a cápák szemlencséje az embernél?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Cseresznyéskert','A','Csehov melyik művében szerepel Arkagyina?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Sirály','B','Csehov melyik művében szerepel Arkagyina?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Három nővér','C','Csehov melyik művében szerepel Arkagyina?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ványa bácsi','D','Csehov melyik művében szerepel Arkagyina?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1001. jan.1.','A','Mikor volt István, királlyá koronázása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1001. jan.11.','B','Mikor volt István, királlyá koronázása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1001. jan.21.','C','Mikor volt István, királlyá koronázása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1000. jan 1.','D','Mikor volt István, királlyá koronázása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('egyszemű óriások','A','Kik voltak a Küklopszok a görög mitológiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('félig ember, félig ló alakú lények','B','Kik voltak a Küklopszok a görög mitológiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('emberevő óriások','C','Kik voltak a Küklopszok a görög mitológiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('kígyó hajú nőalakok','D','Kik voltak a Küklopszok a görög mitológiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Széchenyi István','A','Ki volt Az árvízi hajós?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Wesselényi Miklós','B','Ki volt Az árvízi hajós?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Deák Ferenc','C','Ki volt Az árvízi hajós?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kossuth Lajos','D','Ki volt Az árvízi hajós?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kolumbusz','A','Ki fedezte fel a déli sarkkört?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Marco Polo','B','Ki fedezte fel a déli sarkkört?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Magellán','C','Ki fedezte fel a déli sarkkört?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('James Cook','D','Ki fedezte fel a déli sarkkört?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('George W. Bush','A','1995-ben ki volt az USA elnöke?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ronald Reagan','B','1995-ben ki volt az USA elnöke?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Bill Clinton','C','1995-ben ki volt az USA elnöke?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Donald Trump','D','1995-ben ki volt az USA elnöke?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Morzsinai Erzsébet','A','Ki volt Hunyadi Mátyás anyja?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Szilágyi Erzsébet','B','Ki volt Hunyadi Mátyás anyja?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Anjou Mária','C','Ki volt Hunyadi Mátyás anyja?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Mária Terézia','D','Ki volt Hunyadi Mátyás anyja?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('pogányok','A','Kik voltak a tatárok?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('törökök','B','Kik voltak a tatárok?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('poroszok','C','Kik voltak a tatárok?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('mongolok','D','Kik voltak a tatárok?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('szegycsontjából','A','Ádám melyik csontjából lett Éva?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('bordájából','B','Ádám melyik csontjából lett Éva?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('medencecsontjából','C','Ádám melyik csontjából lett Éva?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('ádámcsutkájából','D','Ádám melyik csontjából lett Éva?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('harmadik világháború','A','Melyik háborúban volt a Barbadossa hadművelet?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('első világháború','B','Melyik háborúban volt a Barbadossa hadművelet?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('második világháború','C','Melyik háborúban volt a Barbadossa hadművelet?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('százéves háború','D','Melyik háborúban volt a Barbadossa hadművelet?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1960-ban','A','Mikor gyártották az első Trabantot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1957-ben','B','Mikor gyártották az első Trabantot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1972-ben','C','Mikor gyártották az első Trabantot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1948-ben','D','Mikor gyártották az első Trabantot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('IV. Károly','A','Ki volt a kalapos király?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('II. András','B','Ki volt a kalapos király?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('I. József','C','Ki volt a kalapos király?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('II. József','D','Ki volt a kalapos király?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Eurüdiké','A','Ki volt Orpheusz felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Aphrodité','B','Ki volt Orpheusz felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Pénelopé','C','Ki volt Orpheusz felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Élektra','D','Ki volt Orpheusz felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Savaria','A','Mi volt Szombahely ókori latin neve?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Arrabona','C','Mi volt Szombahely ókori latin neve?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Solva','D','Mi volt Szombahely ókori latin neve?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('egy','A','Hány gyermeke született Károly Walesi hercegnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('négy','B','Hány gyermeke született Károly Walesi hercegnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('három','C','Hány gyermeke született Károly Walesi hercegnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('kettő','D','Hány gyermeke született Károly Walesi hercegnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('II. András','A','Melyik királyunk nevéhez fűződik az Aranybulla kiadása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('IV. Béla','B','Melyik királyunk nevéhez fűződik az Aranybulla kiadása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('V. István','C','Melyik királyunk nevéhez fűződik az Aranybulla kiadása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('IV. Károly','D','Melyik királyunk nevéhez fűződik az Aranybulla kiadása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1908 London','A','Mikor és hol rendezték meg az első nyári olimpiai játékokat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1896 Athén','B','Mikor és hol rendezték meg az első nyári olimpiai játékokat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1748 Budapest','C','Mikor és hol rendezték meg az első nyári olimpiai játékokat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('932 Los Angeles','D','Mikor és hol rendezték meg az első nyári olimpiai játékokat?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('kettő','B','Hány évente kerül megrendezésre a labdarúgó EB?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('négy','D','Hány évente kerül megrendezésre a labdarúgó EB?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Peruban','A','Hol született Lionel Messi a híres focista?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Brazíliában','B','Hol született Lionel Messi a híres focista?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Argentínában','C','Hol született Lionel Messi a híres focista?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Spanyolországban','D','Hol született Lionel Messi a híres focista?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Erdei Zsolt','A','Melyik sportolónk beceneve Madár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Madár Ferenc','B','Melyik sportolónk beceneve Madár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kovács István','C','Melyik sportolónk beceneve Madár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Cseh László','D','Melyik sportolónk beceneve Madár?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Győr','A','Melyik város szülötte Vajda Attila kenus?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Sopron','B','Melyik város szülötte Vajda Attila kenus?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Szeged','C','Melyik város szülötte Vajda Attila kenus?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Pécs','D','Melyik város szülötte Vajda Attila kenus?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('10','A','Pályafutása során összesen hány aranyérmet szerzett Kovács István (Kokó)?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('8','B','Pályafutása során összesen hány aranyérmet szerzett Kovács István (Kokó)?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('15','C','Pályafutása során összesen hány aranyérmet szerzett Kovács István (Kokó)?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('13','D','Pályafutása során összesen hány aranyérmet szerzett Kovács István (Kokó)?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('kardvívás','A','Szilágyi Áron melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('tőrvívás','B','Szilágyi Áron melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('atlétika','C','Szilágyi Áron melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('ökölvívás','D','Szilágyi Áron melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Szász Emese','A','Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Szilágyi Áron','B','Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Gyurta Dániel','C','Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Hosszú Katinka','D','Ki nyerte az első magyar aranyérmet a Riói olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('torna','B','Keleti Ágnes melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('úszás','D','Keleti Ágnes melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5','A','Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('2','B','Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('3','C','Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('4','D','Hány aranyérmet gyűjtött Hosszú Katinka a Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('12','A','Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('13','B','Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('14','C','Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('15','D','Hány érmet szereztek a magyarok a 2016-os Riói Olimpián?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kökény Beatrix','A','Ki Imre Géza párbajtőrvívó felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Bíró Blanka','B','Ki Imre Géza párbajtőrvívó felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Szekeres Klára','C','Ki Imre Géza párbajtőrvívó felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Keleti Ágnes','D','Ki Imre Géza párbajtőrvívó felesége?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('4','B','Hány érme van összesen Braun Ákos, cselgáncsozónak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('2','D','Hány érme van összesen Braun Ákos, cselgáncsozónak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('orvos','A','Mi a foglalkozása Mincza-Nébald Ildikó vivónőnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('ügyvéd','B','Mi a foglalkozása Mincza-Nébald Ildikó vivónőnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('marketing manager','C','Mi a foglalkozása Mincza-Nébald Ildikó vivónőnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('személyi edző','D','Mi a foglalkozása Mincza-Nébald Ildikó vivónőnek?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('204cm','A','Milyen magas Kásás Tamás vízilabdázó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('208cm','B','Milyen magas Kásás Tamás vízilabdázó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('196cm','C','Milyen magas Kásás Tamás vízilabdázó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('200cm','D','Milyen magas Kásás Tamás vízilabdázó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Pannonia','B','Mi volt Szombahely ókori latin neve?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('3','C','Hány érme van összesen Braun Ákos, cselgáncsozónak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5','A','Hány érme van összesen Braun Ákos, cselgáncsozónak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('egy','A','Hány évente kerül megrendezésre a labdarúgó EB?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('három','C','Hány évente kerül megrendezésre a labdarúgó EB?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('kardvívás','A','Keleti Ágnes melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('atlétika','C','Keleti Ágnes melyik sportág olimpiai bajnoka?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('2','A','Ha 1 hurkapálcának két vége van, 2 hurkapálcának négy vége van, akkor hány vége van 1 és fél hurkapálcának ?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('3','B','Ha 1 hurkapálcának két vége van, 2 hurkapálcának négy vége van, akkor hány vége van 1 és fél hurkapálcának ?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('4','C','Ha 1 hurkapálcának két vége van, 2 hurkapálcának négy vége van, akkor hány vége van 1 és fél hurkapálcának ?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5','D','Ha 1 hurkapálcának két vége van, 2 hurkapálcának négy vége van, akkor hány vége van 1 és fél hurkapálcának ?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('4','A','Egy juhásznak 17 báránya volt. Négy kivételével mind elpusztult. Hány maradt életben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('13','B','Egy juhásznak 17 báránya volt. Négy kivételével mind elpusztult. Hány maradt életben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('17','C','Egy juhásznak 17 báránya volt. Négy kivételével mind elpusztult. Hány maradt életben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('21','D','Egy juhásznak 17 báránya volt. Négy kivételével mind elpusztult. Hány maradt életben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('0','A','Egy kosárban 5 alma van. Elveszel belőle kettőt. Mennyi marad neked?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('2','B','Egy kosárban 5 alma van. Elveszel belőle kettőt. Mennyi marad neked?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('3','C','Egy kosárban 5 alma van. Elveszel belőle kettőt. Mennyi marad neked?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5','D','Egy kosárban 5 alma van. Elveszel belőle kettőt. Mennyi marad neked?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1','A','Lúdas Matyi Döbrögbe bandukol. Vele szembe jön 3 pandúr és 2 paraszt a 10 birkájával. Hányan mennek Döbrögbe?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('6','B','Lúdas Matyi Döbrögbe bandukol. Vele szembe jön 3 pandúr és 2 paraszt a 10 birkájával. Hányan mennek Döbrögbe?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('15','C','Lúdas Matyi Döbrögbe bandukol. Vele szembe jön 3 pandúr és 2 paraszt a 10 birkájával. Hányan mennek Döbrögbe?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('16','D','Lúdas Matyi Döbrögbe bandukol. Vele szembe jön 3 pandúr és 2 paraszt a 10 birkájával. Hányan mennek Döbrögbe?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1','A','Mi az egyenlet megoldása: 6:2(1+2)=?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('6','B','Mi az egyenlet megoldása: 6:2(1+2)=?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('9','C','Mi az egyenlet megoldása: 6:2(1+2)=?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('12','D','Mi az egyenlet megoldása: 6:2(1+2)=?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('16','A','A varrónőnek van egy 16 méteres anyagdarabja, ebből naponta 2 métert levág. Hanyadik nap vágja le az utolsó darabot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('9','B','A varrónőnek van egy 16 méteres anyagdarabja, ebből naponta 2 métert levág. Hanyadik nap vágja le az utolsó darabot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('8','C','A varrónőnek van egy 16 méteres anyagdarabja, ebből naponta 2 métert levág. Hanyadik nap vágja le az utolsó darabot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('7','D','A varrónőnek van egy 16 méteres anyagdarabja, ebből naponta 2 métert levág. Hanyadik nap vágja le az utolsó darabot?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('5','A','Nagy úrnak és Nagynénak 4 lánya van. Mindegyik lánynak van egy bátyja. Hány gyereke van Nagyéknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('6','B','Nagy úrnak és Nagynénak 4 lánya van. Mindegyik lánynak van egy bátyja. Hány gyereke van Nagyéknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('7','C','Nagy úrnak és Nagynénak 4 lánya van. Mindegyik lánynak van egy bátyja. Hány gyereke van Nagyéknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('8','D','Nagy úrnak és Nagynénak 4 lánya van. Mindegyik lánynak van egy bátyja. Hány gyereke van Nagyéknak?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('30','A','Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('45','B','Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('59','C','Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('75','D','Egy moszat olyan gyorsan szaporodik, hogy minden percben megkétszerezi önmagát. Ha egy tavat 60 perc alatt terít be, hány perc alatt teríti be a felét?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ausztria','A','Ausztria és Magyarország határára lezuhan egy repülőgép. Melyik országban temetik el a túlélőket?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Magyarország','B','Ausztria és Magyarország határára lezuhan egy repülőgép. Melyik országban temetik el a túlélőket?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Mindkettő','C','Ausztria és Magyarország határára lezuhan egy repülőgép. Melyik országban temetik el a túlélőket?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Egyiksem','D','Ausztria és Magyarország határára lezuhan egy repülőgép. Melyik országban temetik el a túlélőket?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('1','A','Hány 9 van 1-től 100-ig?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('9','B','Hány 9 van 1-től 100-ig?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('10','C','Hány 9 van 1-től 100-ig?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('20','D','Hány 9 van 1-től 100-ig?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kosztolányi Dezső','A','Melyik költő verse a Héja-nász az avaron?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('József Attila','B','Melyik költő verse a Héja-nász az avaron?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Arany János','C','Melyik költő verse a Héja-nász az avaron?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ady Endre','D','Melyik költő verse a Héja-nász az avaron?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('6','A','Hány kötetből áll a Harry Potter?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('7','B','Hány kötetből áll a Harry Potter?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('8','C','Hány kötetből áll a Harry Potter?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('9','D','Hány kötetből áll a Harry Potter?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('mágus','A','Ki volt Gandalf, A Gyűrűk Ura trilógiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('törp','B','Ki volt Gandalf, A Gyűrűk Ura trilógiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('elf','C','Ki volt Gandalf, A Gyűrűk Ura trilógiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('hobbit','D','Ki volt Gandalf, A Gyűrűk Ura trilógiában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('róka','A','Milyen állat Vuk, Fekete István regényében?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('farkas','B','Milyen állat Vuk, Fekete István regényében?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('nyúl','C','Milyen állat Vuk, Fekete István regényében?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('gólya','D','Milyen állat Vuk, Fekete István regényében?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ady Endre','A','Kinek a műve az Egyperces novellák?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kosztolányi Dezső','B','Kinek a műve az Egyperces novellák?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Örkény István','C','Kinek a műve az Egyperces novellák?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Móricz Zsigmond','D','Kinek a műve az Egyperces novellák?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Jack London','A','Kinek a regénye Az öreg halász és a tenger?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('William Faulkner','B','Kinek a regénye Az öreg halász és a tenger?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ernest Hemingway','C','Kinek a regénye Az öreg halász és a tenger?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('George Bernard Shaw','D','Kinek a regénye Az öreg halász és a tenger?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Richárd király','A','Melyik király léptet fakó lován Arany balladájában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Edward király','B','Melyik király léptet fakó lován Arany balladájában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Edgár király','C','Melyik király léptet fakó lován Arany balladájában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Lear király','D','Melyik király léptet fakó lován Arany balladájában?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('ács','A','Mi volt Petőfi Sándor édesapjának foglalkozása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('asztalos','B','Mi volt Petőfi Sándor édesapjának foglalkozása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('takács','C','Mi volt Petőfi Sándor édesapjának foglalkozása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('mészáros','D','Mi volt Petőfi Sándor édesapjának foglalkozása?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('keresztrím','A','Mi az alliteráció?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('betűrím','B','Mi az alliteráció?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('bokorrím','C','Mi az alliteráció?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('párosrím','D','Mi az alliteráció?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('7','A','Hány tagja van a Gyűrű szövetségének "A Gyűrűk urai" c. regényben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('9','B','Hány tagja van a Gyűrű szövetségének "A Gyűrűk urai" c. regényben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('12','C','Hány tagja van a Gyűrű szövetségének "A Gyűrűk urai" c. regényben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('16','D','Hány tagja van a Gyűrű szövetségének "A Gyűrűk urai" c. regényben?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kertész Imre','A','Ki írta Für Elise c. regényt?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kaffka Margit','B','Ki írta Für Elise c. regényt?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Szabó Magda','C','Ki írta Für Elise c. regényt?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Örkény István','D','Ki írta Für Elise c. regényt?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Kincskereső kisködmön','A','Melyik irodalmi mű szereplője Csicsó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Tüskevár','B','Melyik irodalmi mű szereplője Csicsó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Pál utcai fiúk','C','Melyik irodalmi mű szereplője Csicsó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Légy jó mindhalálig','D','Melyik irodalmi mű szereplője Csicsó?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Fekete István','A','Kinek a regénye a Gergő és az álomfogók?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Esterházy Péter','B','Kinek a regénye a Gergő és az álomfogók?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Böszörményi Gyula','C','Kinek a regénye a Gergő és az álomfogók?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Karinthy Frigyes','D','Kinek a regénye a Gergő és az álomfogók?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Mihail Bulgakov','A','Kinek a regénye "A Mester és Margarita"?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Ivan Turgenyev','B','Kinek a regénye "A Mester és Margarita"?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Lev Tolsztoj','C','Kinek a regénye "A Mester és Margarita"?');
Insert into VALASZ (SZOVEG,BETUJEL,KERDESSZOVEG) values ('Fjodor Mihajlovics Dosztojevszkij','D','Kinek a regénye "A Mester és Margarita"?');
REM INSERTING into VERSENY
SET DEFINE OFF;
Insert into VERSENY (ID,NEV) values (3,'Verseny3');
Insert into VERSENY (ID,NEV) values (1,'Verseny1');
Insert into VERSENY (ID,NEV) values (2,'Verseny2');
--------------------------------------------------------
--  DDL for Index PARBAJRAHIVOTT_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "PARBAJRAHIVOTT_PK" ON "PARBAJRAHIVOTT" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index PARBAJRAHIV_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "PARBAJRAHIV_PK" ON "PARBAJRAHIV" ("ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C0010093
--------------------------------------------------------

  CREATE UNIQUE INDEX "SYS_C0010093" ON "VALASZ" ("BETUJEL", "KERDESSZOVEG") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Trigger ADD_POINTS
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "ADD_POINTS" 
AFTER INSERT
ON ADOTTVALASZ
FOR EACH ROW
DECLARE
    difficulty NUMBER;
    mult NUMBER;
    correct_ans VARCHAR(1);
    
BEGIN
    SELECT nehezseg INTO difficulty FROM KERDES
    WHERE szoveg = :NEW.kerdesszoveg;
    
    SELECT betujel INTO correct_ans FROM KERDES
    WHERE szoveg = :NEW.kerdesszoveg;
    
    IF correct_ans = :NEW.valaszjel THEN
        mult := 1;
    ELSE
        mult := -1;
    END IF;
    
    CASE difficulty
        WHEN 0 THEN UPDATE JATEKOS SET konnyupont = konnyupont + mult * 1 WHERE felhasznalonev = :NEW.valaszado;
        WHEN 1 THEN UPDATE JATEKOS SET kozepespont = kozepespont + mult * 2 WHERE felhasznalonev = :NEW.valaszado;
        WHEN 2 THEN UPDATE JATEKOS SET nehezpont = nehezpont + mult * 3 WHERE felhasznalonev = :NEW.valaszado;
    END CASE;
END;
/
ALTER TRIGGER "ADD_POINTS" ENABLE;
--------------------------------------------------------
--  DDL for Trigger ADD_TO_FORUM
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "ADD_TO_FORUM" 
AFTER INSERT ON JATEKOS
FOR EACH ROW
BEGIN
  INSERT INTO KOZOSSEGTAGJA(felhasznalonev, kozosseg) VALUES(:NEW.felhasznalonev, 0);
END;
/
ALTER TRIGGER "ADD_TO_FORUM" ENABLE;
--------------------------------------------------------
--  DDL for Trigger ADJUST_POINTS
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "ADJUST_POINTS" 
AFTER UPDATE OF nehezseg
ON KERDES
FOR EACH ROW
 WHEN (NEW.nehezseg != OLD.nehezseg) DECLARE
    CURSOR c IS SELECT DISTINCT valaszado FROM ADOTTVALASZ
    WHERE ADOTTVALASZ.kerdesszoveg = :NEW.szoveg;
    
BEGIN
    FOR jatekos IN c LOOP
        IF :OLD.nehezseg = 0 AND :NEW.nehezseg = 1 THEN
            UPDATE JATEKOS SET konnyupont = konnyupont-1, kozepespont = kozepespont+2;
        ELSIF :OLD.nehezseg = 0 AND :NEW.nehezseg = 2 THEN
            UPDATE JATEKOS SET konnyupont = konnyupont-1, nehezpont = nehezpont+3;
        ELSIF :OLD.nehezseg = 1 AND :NEW.nehezseg = 0 THEN
            UPDATE JATEKOS SET konnyupont = konnyupont+1, kozepespont = kozepespont-2;
        ELSIF :OLD.nehezseg = 1 AND :NEW.nehezseg = 2 THEN
            UPDATE JATEKOS SET kozepespont = kozepespont-2, nehezpont = nehezpont+3;
        ELSIF :OLD.nehezseg = 2 AND :NEW.nehezseg = 0 THEN
            UPDATE JATEKOS SET konnyupont = konnyupont+1, nehezpont = nehezpont-3;
        ELSIF :OLD.nehezseg = 2 AND :NEW.nehezseg = 1 THEN
            UPDATE JATEKOS SET kozepespont = kozepespont+2, nehezpont = nehezpont-3;
        END IF;
    END LOOP;
END;
/
ALTER TRIGGER "ADJUST_POINTS" ENABLE;
--------------------------------------------------------
--  DDL for Trigger AUTO_INC_ADOTTVALASZ
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "AUTO_INC_ADOTTVALASZ" 
BEFORE INSERT ON ADOTTVALASZ
FOR EACH ROW
DECLARE
    max_id NUMBER;
    
BEGIN
    SELECT max(id) INTO max_id FROM ADOTTVALASZ;
    
    IF max_id IS NULL THEN
        :NEW.id := 0;
    ELSE
        :NEW.id := max_id + 1;
    END IF;
END;
/
ALTER TRIGGER "AUTO_INC_ADOTTVALASZ" ENABLE;
--------------------------------------------------------
--  DDL for Trigger AUTO_INC_HIRDETES
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "AUTO_INC_HIRDETES" 
BEFORE INSERT ON HIRDETES
FOR EACH ROW

DECLARE
    max_id NUMBER;

BEGIN
    SELECT max(id) INTO max_id FROM HIRDETES;

    IF max_id IS NULL THEN
        :NEW.id := 0;
    ELSE
        :NEW.id := max_id + 1;
    END IF;
END;
/
ALTER TRIGGER "AUTO_INC_HIRDETES" ENABLE;
--------------------------------------------------------
--  DDL for Trigger AUTO_INC_PARBAJ
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "AUTO_INC_PARBAJ" 
BEFORE INSERT ON PARBAJ
FOR EACH ROW

DECLARE
    max_id NUMBER;
    
BEGIN
    SELECT max(id) INTO max_id FROM PARBAJ;
    
    IF max_id IS NULL THEN
        :NEW.id := 0;
    ELSE
        :NEW.id := max_id + 1;
    END IF;
END;
/
ALTER TRIGGER "AUTO_INC_PARBAJ" ENABLE;
--------------------------------------------------------
--  DDL for Trigger BLOCK_NEG_POINTS
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "BLOCK_NEG_POINTS" 
BEFORE INSERT OR UPDATE OF KONNYUPONT, KOZEPESPONT, NEHEZPONT
ON JATEKOS
FOR EACH ROW
BEGIN
    IF :NEW.konnyupont < 0 THEN
        :NEW.konnyupont := 0;
    END IF;

    IF :NEW.kozepespont < 0 THEN
        :NEW.kozepespont := 0;
    END IF;

    IF :NEW.nehezpont < 0 THEN
        :NEW.nehezpont := 0;
    END IF;
END;
/
ALTER TRIGGER "BLOCK_NEG_POINTS" ENABLE;
--------------------------------------------------------
--  DDL for Trigger CALC_DIFFICULTY
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "CALC_DIFFICULTY" 
FOR INSERT OR UPDATE OR DELETE
ON ADOTTVALASZ
FOLLOWS ADD_POINTS
COMPOUND TRIGGER
    TYPE row_level_info_t IS TABLE OF VARCHAR(500) INDEX BY BINARY_INTEGER;

    g_row_level_info row_level_info_t;
    num_ans NUMBER;
    num_correct_ans NUMBER;
    cur_kerdesszoveg VARCHAR(500);

    AFTER EACH ROW IS    
    BEGIN
        IF INSERTING OR UPDATING THEN
            g_row_level_info(g_row_level_info.COUNT + 1) := :NEW.kerdesszoveg;
        ELSE
            g_row_level_info(g_row_level_info.COUNT + 1) := :OLD.kerdesszoveg;
        END IF;
    END AFTER EACH ROW;

    AFTER STATEMENT IS
    BEGIN       
        IF g_row_level_info.COUNT > 0 THEN
            FOR ind in 1 .. g_row_level_info.COUNT
            LOOP
                SELECT COUNT(id) INTO num_ans FROM ADOTTVALASZ WHERE kerdesszoveg = g_row_level_info(ind);

                IF num_ans < 10 THEN
                    CONTINUE;
                END IF;

                SELECT COUNT(ADOTTVALASZ.id) INTO num_correct_ans FROM ADOTTVALASZ
                INNER JOIN KERDES ON ADOTTVALASZ.kerdesszoveg = KERDES.szoveg
                WHERE ADOTTVALASZ.kerdesszoveg = g_row_level_info(ind) AND ADOTTVALASZ.valaszjel = KERDES.betujel;

                IF num_correct_ans / num_ans > 0.66 THEN
                    UPDATE KERDES SET nehezseg = 0 WHERE szoveg = g_row_level_info(ind);
                ELSIF num_correct_ans / num_ans > 0.33 THEN
                    UPDATE KERDES SET nehezseg = 1 WHERE szoveg = g_row_level_info(ind);
                ELSE
                    UPDATE KERDES SET nehezseg = 2 WHERE szoveg = g_row_level_info(ind);
                END IF;
            END LOOP;
        END IF;
    END AFTER STATEMENT;
END CALC_DIFFICULTY ;
/
ALTER TRIGGER "CALC_DIFFICULTY" ENABLE;
--------------------------------------------------------
--  DDL for Trigger DRAW_QUESTION
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "DRAW_QUESTION" 
AFTER INSERT ON PARBAJ
FOR EACH ROW
DECLARE
    rand_szoveg VARCHAR(500);

BEGIN
    SELECT szoveg INTO rand_szoveg FROM (SELECT szoveg FROM KERDES WHERE temakor != 'IQ' ORDER BY DBMS_RANDOM.VALUE) WHERE rownum = 1;
    INSERT INTO PARBAJKERDESE(id, szoveg) VALUES(:NEW.id, rand_szoveg);
END;
/
ALTER TRIGGER "DRAW_QUESTION" ENABLE;
--------------------------------------------------------
--  DDL for Trigger PARBAJ_TO_ADOTT
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE TRIGGER "PARBAJ_TO_ADOTT" 
AFTER INSERT ON PARBAJVALASZ
FOR EACH ROW 
DECLARE
    kerdes_szoveg VARCHAR(500);
    valasz_szoveg VARCHAR(500);
    
BEGIN
    SELECT parbajkerdese.szoveg INTO kerdes_szoveg FROM parbajkerdese WHERE id = :NEW.parbajid;
    SELECT valasz.szoveg INTO valasz_szoveg FROM VALASZ WHERE kerdesszoveg = kerdes_szoveg AND betujel = :NEW.valasz;
    INSERT INTO adottvalasz(id, valaszjel, kerdesszoveg, valaszado, valaszszoveg) VALUES(-1, :NEW.valasz, kerdes_szoveg, :NEW.jatekos, valasz_szoveg);
END;
/
ALTER TRIGGER "PARBAJ_TO_ADOTT" ENABLE;
--------------------------------------------------------
--  DDL for Procedure ADD_PARBAJ
--------------------------------------------------------
set define off;

  CREATE OR REPLACE EDITIONABLE PROCEDURE "ADD_PARBAJ" 
(challenger VARCHAR, challenged VARCHAR)
AS 
    inserted_id NUMBER;

BEGIN
  INSERT INTO PARBAJ(id, pending, nyertes) VALUES(-1, 1, null) returning id INTO inserted_id;
  INSERT INTO PARBAJRAHIVOTT(id, jatekos) VALUES(inserted_id, challenged);
  INSERT INTO PARBAJRAHIV(id, jatekos) VALUES(inserted_id, challenger);
END ADD_PARBAJ;


/
--------------------------------------------------------
--  DDL for Function AGGREGATE_POINTS
--------------------------------------------------------

  CREATE OR REPLACE EDITIONABLE FUNCTION "AGGREGATE_POINTS" (easy_mult NUMBER, med_mult NUMBER, hard_mult NUMBER)
RETURN AGGREGATE_TOPLIST_TABLE_T
AS

    ret AGGREGATE_TOPLIST_TABLE_T;

BEGIN
    SELECT aggregate_toplist_entry_t(FELHASZNALONEV, easy_mult * KONNYUPONT + med_mult * KOZEPESPONT + hard_mult * NEHEZPONT)
    BULK COLLECT INTO ret
    FROM JATEKOS;

  RETURN ret;


END AGGREGATE_POINTS;


/
--------------------------------------------------------
--  Constraints for Table VALASZ
--------------------------------------------------------

  ALTER TABLE "VALASZ" MODIFY ("KERDESSZOVEG" NOT NULL ENABLE);
  ALTER TABLE "VALASZ" ADD CONSTRAINT "SYS_C0010093" PRIMARY KEY ("BETUJEL", "KERDESSZOVEG")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table PARBAJKERDESE
--------------------------------------------------------

  ALTER TABLE "PARBAJKERDESE" ADD PRIMARY KEY ("ID", "SZOVEG")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table FORDULO
--------------------------------------------------------

  ALTER TABLE "FORDULO" MODIFY ("BESTOF" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table UTKOZETRESZVETEL
--------------------------------------------------------

  ALTER TABLE "UTKOZETRESZVETEL" ADD PRIMARY KEY ("VERSENYID", "FELHASZNALONEV")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table VERSENY
--------------------------------------------------------

  ALTER TABLE "VERSENY" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "VERSENY" MODIFY ("NEV" NOT NULL ENABLE);
  ALTER TABLE "VERSENY" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table BETUJEL
--------------------------------------------------------

  ALTER TABLE "BETUJEL" ADD PRIMARY KEY ("JEL")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "BETUJEL" MODIFY ("JEL" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table JATEKOS
--------------------------------------------------------

  ALTER TABLE "JATEKOS" MODIFY ("KOZEPESPONT" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("KONNYUPONT" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("SALT" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("NEHEZPONT" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("SZULDATUM" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" ADD UNIQUE ("EMAIL")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "JATEKOS" ADD PRIMARY KEY ("FELHASZNALONEV")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "JATEKOS" MODIFY ("JELSZO" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("ADMIN" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("EMAIL" NOT NULL ENABLE);
  ALTER TABLE "JATEKOS" MODIFY ("FELHASZNALONEV" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table KOZOSSEG
--------------------------------------------------------

  ALTER TABLE "KOZOSSEG" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "KOZOSSEG" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table HIRDETES
--------------------------------------------------------

  ALTER TABLE "HIRDETES" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HIRDETES" MODIFY ("CIM" NOT NULL ENABLE);
  ALTER TABLE "HIRDETES" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table ADOTTVALASZ
--------------------------------------------------------

  ALTER TABLE "ADOTTVALASZ" MODIFY ("VALASZSZOVEG" NOT NULL ENABLE);
  ALTER TABLE "ADOTTVALASZ" MODIFY ("VALASZADO" NOT NULL ENABLE);
  ALTER TABLE "ADOTTVALASZ" MODIFY ("KERDESSZOVEG" NOT NULL ENABLE);
  ALTER TABLE "ADOTTVALASZ" MODIFY ("VALASZJEL" NOT NULL ENABLE);
  ALTER TABLE "ADOTTVALASZ" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table KOZOSSEGTAGJA
--------------------------------------------------------

  ALTER TABLE "KOZOSSEGTAGJA" ADD PRIMARY KEY ("FELHASZNALONEV", "KOZOSSEG")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table UTKOZETKERDESE
--------------------------------------------------------

  ALTER TABLE "UTKOZETKERDESE" ADD PRIMARY KEY ("VERSENYID", "SZOVEG")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table UZENET
--------------------------------------------------------

  ALTER TABLE "UZENET" ADD PRIMARY KEY ("KULDO", "KOZOSSEG", "IDOPONT")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "UZENET" MODIFY ("IDOPONT" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table PARBAJRAHIVOTT
--------------------------------------------------------

  ALTER TABLE "PARBAJRAHIVOTT" ADD CONSTRAINT "PARBAJRAHIVOTT_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "PARBAJRAHIVOTT" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "PARBAJRAHIVOTT" MODIFY ("JATEKOS" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table PARBAJVALASZ
--------------------------------------------------------

  ALTER TABLE "PARBAJVALASZ" MODIFY ("VALASZ" NOT NULL ENABLE);
  ALTER TABLE "PARBAJVALASZ" MODIFY ("JATEKOS" NOT NULL ENABLE);
  ALTER TABLE "PARBAJVALASZ" MODIFY ("PARBAJID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table PARBAJ
--------------------------------------------------------

  ALTER TABLE "PARBAJ" ADD PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "PARBAJ" MODIFY ("PENDING" NOT NULL ENABLE);
  ALTER TABLE "PARBAJ" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table KERDES
--------------------------------------------------------

  ALTER TABLE "KERDES" ADD PRIMARY KEY ("SZOVEG")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "KERDES" MODIFY ("SZOVEG" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table PARBAJRAHIV
--------------------------------------------------------

  ALTER TABLE "PARBAJRAHIV" ADD CONSTRAINT "PARBAJRAHIV_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "PARBAJRAHIV" MODIFY ("JATEKOS" NOT NULL ENABLE);
  ALTER TABLE "PARBAJRAHIV" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table UTKOZET
--------------------------------------------------------

  ALTER TABLE "UTKOZET" ADD PRIMARY KEY ("VERSENYID", "FELHASZNALONEV")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
--------------------------------------------------------
--  Constraints for Table TEMAKOR
--------------------------------------------------------

  ALTER TABLE "TEMAKOR" ADD PRIMARY KEY ("NEV")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "TEMAKOR" MODIFY ("NEV" NOT NULL ENABLE);
--------------------------------------------------------
--  Ref Constraints for Table ADOTTVALASZ
--------------------------------------------------------

  ALTER TABLE "ADOTTVALASZ" ADD CONSTRAINT "ADOTTVALASZ_FK1" FOREIGN KEY ("VALASZADO")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
  ALTER TABLE "ADOTTVALASZ" ADD CONSTRAINT "ADOTTVALASZ_FK2" FOREIGN KEY ("KERDESSZOVEG")
	  REFERENCES "KERDES" ("SZOVEG") ON DELETE CASCADE ENABLE;
  ALTER TABLE "ADOTTVALASZ" ADD CONSTRAINT "ADOTTVALASZ_FK3" FOREIGN KEY ("VALASZJEL", "KERDESSZOVEG")
	  REFERENCES "VALASZ" ("BETUJEL", "KERDESSZOVEG") ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table FORDULO
--------------------------------------------------------

  ALTER TABLE "FORDULO" ADD CONSTRAINT "SYS_C0010089" FOREIGN KEY ("VERSENYID")
	  REFERENCES "VERSENY" ("ID") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table KERDES
--------------------------------------------------------

  ALTER TABLE "KERDES" ADD CONSTRAINT "SYS_C0010081" FOREIGN KEY ("TEMAKOR")
	  REFERENCES "TEMAKOR" ("NEV") ON DELETE CASCADE ENABLE;
  ALTER TABLE "KERDES" ADD CONSTRAINT "SYS_C0010082" FOREIGN KEY ("BETUJEL")
	  REFERENCES "BETUJEL" ("JEL") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table KOZOSSEGTAGJA
--------------------------------------------------------

  ALTER TABLE "KOZOSSEGTAGJA" ADD CONSTRAINT "SYS_C0010113" FOREIGN KEY ("FELHASZNALONEV")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
  ALTER TABLE "KOZOSSEGTAGJA" ADD CONSTRAINT "SYS_C0010114" FOREIGN KEY ("KOZOSSEG")
	  REFERENCES "KOZOSSEG" ("ID") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PARBAJ
--------------------------------------------------------

  ALTER TABLE "PARBAJ" ADD CONSTRAINT "SYS_C0010071" FOREIGN KEY ("NYERTES")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PARBAJKERDESE
--------------------------------------------------------

  ALTER TABLE "PARBAJKERDESE" ADD CONSTRAINT "SYS_C0010110" FOREIGN KEY ("ID")
	  REFERENCES "PARBAJ" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "PARBAJKERDESE" ADD CONSTRAINT "SYS_C0010111" FOREIGN KEY ("SZOVEG")
	  REFERENCES "KERDES" ("SZOVEG") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PARBAJRAHIV
--------------------------------------------------------

  ALTER TABLE "PARBAJRAHIV" ADD CONSTRAINT "PARBAJRAHIV_FK1" FOREIGN KEY ("ID")
	  REFERENCES "PARBAJ" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "PARBAJRAHIV" ADD CONSTRAINT "PARBAJRAHIV_FK2" FOREIGN KEY ("JATEKOS")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PARBAJRAHIVOTT
--------------------------------------------------------

  ALTER TABLE "PARBAJRAHIVOTT" ADD CONSTRAINT "PARBAJRAHIVOTT_FK1" FOREIGN KEY ("ID")
	  REFERENCES "PARBAJ" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "PARBAJRAHIVOTT" ADD CONSTRAINT "PARBAJRAHIVOTT_FK2" FOREIGN KEY ("JATEKOS")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table PARBAJVALASZ
--------------------------------------------------------

  ALTER TABLE "PARBAJVALASZ" ADD CONSTRAINT "PARBAJVALASZ_FK1" FOREIGN KEY ("PARBAJID")
	  REFERENCES "PARBAJ" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "PARBAJVALASZ" ADD CONSTRAINT "PARBAJVALASZ_FK2" FOREIGN KEY ("JATEKOS")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
  ALTER TABLE "PARBAJVALASZ" ADD CONSTRAINT "PARBAJVALASZ_FK3" FOREIGN KEY ("VALASZ")
	  REFERENCES "BETUJEL" ("JEL") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table UTKOZET
--------------------------------------------------------

  ALTER TABLE "UTKOZET" ADD CONSTRAINT "SYS_C0010091" FOREIGN KEY ("VERSENYID")
	  REFERENCES "VERSENY" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "UTKOZET" ADD CONSTRAINT "SYS_C0010092" FOREIGN KEY ("FELHASZNALONEV")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table UTKOZETKERDESE
--------------------------------------------------------

  ALTER TABLE "UTKOZETKERDESE" ADD CONSTRAINT "SYS_C0010104" FOREIGN KEY ("VERSENYID")
	  REFERENCES "VERSENY" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "UTKOZETKERDESE" ADD CONSTRAINT "SYS_C0010105" FOREIGN KEY ("SZOVEG")
	  REFERENCES "KERDES" ("SZOVEG") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table UTKOZETRESZVETEL
--------------------------------------------------------

  ALTER TABLE "UTKOZETRESZVETEL" ADD CONSTRAINT "SYS_C0010101" FOREIGN KEY ("VERSENYID")
	  REFERENCES "VERSENY" ("ID") ON DELETE CASCADE ENABLE;
  ALTER TABLE "UTKOZETRESZVETEL" ADD CONSTRAINT "SYS_C0010102" FOREIGN KEY ("FELHASZNALONEV")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table UZENET
--------------------------------------------------------

  ALTER TABLE "UZENET" ADD CONSTRAINT "SYS_C0010098" FOREIGN KEY ("KULDO")
	  REFERENCES "JATEKOS" ("FELHASZNALONEV") ON DELETE CASCADE ENABLE;
  ALTER TABLE "UZENET" ADD CONSTRAINT "SYS_C0010099" FOREIGN KEY ("KOZOSSEG")
	  REFERENCES "KOZOSSEG" ("ID") ON DELETE CASCADE ENABLE;
--------------------------------------------------------
--  Ref Constraints for Table VALASZ
--------------------------------------------------------

  ALTER TABLE "VALASZ" ADD CONSTRAINT "SYS_C0010094" FOREIGN KEY ("BETUJEL")
	  REFERENCES "BETUJEL" ("JEL") ON DELETE CASCADE ENABLE;
  ALTER TABLE "VALASZ" ADD CONSTRAINT "SYS_C0010095" FOREIGN KEY ("KERDESSZOVEG")
	  REFERENCES "KERDES" ("SZOVEG") ON DELETE CASCADE ENABLE;
