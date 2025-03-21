﻿CREATE TABLE authors
(
   au_id          varchar(12)       PRIMARY KEY,
   au_lname       varchar(40)       NOT NULL,
   au_fname       varchar(20)       NOT NULL,
   phone          char(12)          NOT NULL,
   address        varchar(40)           NULL,
   city           varchar(20)           NULL,
   state          char(2)               NULL,
   zip            char(5)               NULL,
   contract       bit               NOT NULL
);

CREATE TABLE publishers
(
   pub_id         char(4)           PRIMARY KEY,
   pub_name       varchar(40)           NULL,
   city           varchar(20)           NULL,
   state          char(2)               NULL,
   country        varchar(30)           NULL
);

CREATE TABLE titles
(
   title_id       varchar(6)       PRIMARY KEY,
   title          varchar(80)       NOT NULL,
   type           char(12)          NOT NULL,
   pub_id         char(4)           NOT NULL,      
   price          money                 NULL,
   advance        money                 NULL,
   royalty        int                   NULL,
   ytd_sales      int                   NULL,
   notes          varchar(200)          NULL,
   pubdate        datetime          NOT NULL
   DEFAULT (getdate()),
   FOREIGN KEY (pub_id) REFERENCES publishers(pub_id)
   ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE titleauthor
(
   au_id          varchar(12),       
   title_id       varchar(6),        
   au_ord         tinyint               NULL,
   royaltyper     int                   NULL,
   PRIMARY KEY (au_id, title_id),
   FOREIGN KEY (au_id) REFERENCES authors(au_id)
   ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (title_id) REFERENCES titles(title_id)
   ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE stores
(
   stor_id        char(4)           PRIMARY KEY,
   stor_name      varchar(40)           NULL,
   stor_address   varchar(40)           NULL,
   city           varchar(20)           NULL,
   state          char(2)               NULL,
   zip            char(5)               NULL
);

CREATE TABLE sales
(
   stor_id        char(4)           NOT NULL,
   ord_num        varchar(20)       NOT NULL,
   ord_date       datetime          NOT NULL,
   qty            smallint          NOT NULL,
   payterms       varchar(12)       NOT NULL,
   title_id       varchar(6)        NOT NULL,
   PRIMARY KEY (stor_id, ord_num, title_id),
   FOREIGN KEY (stor_id) REFERENCES stores(stor_id)
   ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY (title_id) REFERENCES titles(title_id)
   ON DELETE CASCADE ON UPDATE CASCADE,
);

insert authors
   values('409-56-7008', 'Bennet', 'Abraham', '415 658-9932',
   '6223 Bateman St.', 'Berkeley', 'CA', '94705', 1)
insert authors
   values('213-46-8915', 'Green', 'Marjorie', '415 986-7020',
   '309 63rd St. #411', 'Oakland', 'CA', '94618', 1)
insert authors
   values('238-95-7766', 'Carson', 'Cheryl', '415 548-7723',
   '589 Darwin Ln.', 'Berkeley', 'CA', '94705', 1)
insert authors
   values('998-72-3567', 'Ringer', 'Albert', '801 826-0752',
   '67 Seventh Av.', 'Salt Lake City', 'UT', '84152', 1)
insert authors
   values('899-46-2035', 'Ringer', 'Anne', '801 826-0752',
   '67 Seventh Av.', 'Salt Lake City', 'UT', '84152', 1)
insert authors
   values('722-51-5454', 'DeFrance', 'Michel', '219 547-9982',
   '3 Balding Pl.', 'Gary', 'IN', '46403', 1)
insert authors
   values('807-91-6654', 'Panteley', 'Sylvia', '301 946-8853',
   '1956 Arlington Pl.', 'Rockville', 'MD', '20853', 1)
insert authors
   values('893-72-1158', 'McBadden', 'Heather',
   '707 448-4982', '301 Putnam', 'Vacaville', 'CA', '95688', 0)
insert authors
   values('724-08-9931', 'Stringer', 'Dirk', '415 843-2991',
   '5420 Telegraph Av.', 'Oakland', 'CA', '94609', 0)
insert authors
   values('274-80-9391', 'Straight', 'Dean', '415 834-2919',
   '5420 College Av.', 'Oakland', 'CA', '94609', 1)
insert authors
   values('756-30-7391', 'Karsen', 'Livia', '415 534-9219',
   '5720 McAuley St.', 'Oakland', 'CA', '94609', 1)
insert authors
   values('724-80-9391', 'MacFeather', 'Stearns', '415 354-7128',
   '44 Upland Hts.', 'Oakland', 'CA', '94612', 1)
insert authors
   values('427-17-2319', 'Dull', 'Ann', '415 836-7128',
   '3410 Blonde St.', 'Palo Alto', 'CA', '94301', 1)
insert authors
   values('672-71-3249', 'Yokomoto', 'Akiko', '415 935-4228',
   '3 Silver Ct.', 'Walnut Creek', 'CA', '94595', 1)
insert authors
   values('267-41-2394', 'O''Leary', 'Michael', '408 286-2428',
   '22 Cleveland Av. #14', 'San Jose', 'CA', '95128', 1)
insert authors
   values('472-27-2349', 'Gringlesby', 'Burt', '707 938-6445',
   'PO Box 792', 'Covelo', 'CA', '95428', 3)
insert authors
   values('527-72-3246', 'Greene', 'Morningstar', '615 297-2723',
   '22 Graybar House Rd.', 'Nashville', 'TN', '37215', 0)
insert authors
   values('172-32-1176', 'White', 'Johnson', '408 496-7223',
   '10932 Bigge Rd.', 'Menlo Park', 'CA', '94025', 1)
insert authors
   values('712-45-1867', 'del Castillo', 'Innes', '615 996-8275',
   '2286 Cram Pl. #86', 'Ann Arbor', 'MI', '48105', 1)
insert authors
   values('846-92-7186', 'Hunter', 'Sheryl', '415 836-7128',
   '3410 Blonde St.', 'Palo Alto', 'CA', '94301', 1)
insert authors
   values('486-29-1786', 'Locksley', 'Charlene', '415 585-4620',
   '18 Broadway Av.', 'San Francisco', 'CA', '94130', 1)
insert authors
   values('648-92-1872', 'Blotchet-Halls', 'Reginald', '503 745-6402',
   '55 Hillsdale Bl.', 'Corvallis', 'OR', '97330', 1)
insert authors
   values('341-22-1782', 'Smith', 'Meander', '913 843-0462',
   '10 Mississippi Dr.', 'Lawrence', 'KS', '66044', 0)


insert publishers values('0736', 'New Moon Books', 'Boston', 'MA', 'USA')
insert publishers values('0877', 'Binnet & Hardley', 'Washington', 'DC', 'USA')
insert publishers values('1389', 'Algodata Infosystems', 'Berkeley', 'CA', 'USA')
insert publishers values('9952', 'Scootney Books', 'New York', 'NY', 'USA')
insert publishers values('1622', 'Five Lakes Publishing', 'Chicago', 'IL', 'USA')
insert publishers values('1756', 'Ramona Publishers', 'Dallas', 'TX', 'USA')
insert publishers values('9901', 'GGG&G', 'Minchen', NULL, 'Germany')
insert publishers values('9999', 'Lucerne Publishing', 'Paris', NULL, 'France')


insert titles values ('PC8888', 'Secrets of Silicon Valley', 'popular_comp', '1389',
$20.00, $8000.00, 10, 4095,
'Muckraking reporting on the world''s largest computer hardware and software manufacturers.',
'06/12/94')

insert titles values ('BU1032', 'The Busy Executive''s Database Guide', 'business',
'1389', $19.99, $5000.00, 10, 4095,
'An overview of available database systems with emphasis on common business applications. Illustrated.',
'06/12/91')

insert titles values ('PS7777', 'Emotional Security: A New Algorithm', 'psychology',
'0736', $7.99, $4000.00, 10, 3336,
'Protecting yourself and your loved ones from undue emotional stress in the modern world. Use of computer and nutritional aids emphasized.',
'06/12/91')

insert titles values ('PS3333', 'Prolonged Data Deprivation: Four Case Studies',
'psychology', '0736', $19.99, $2000.00, 10, 4072,
'What happens when the data runs dry?  Searching evaluations of information-shortage effects.',
'06/12/91')

insert titles values ('BU1111', 'Cooking with Computers: Surreptitious Balance Sheets',
'business', '1389', $11.95, $5000.00, 10, 3876,
'Helpful hints on how to use your electronic resources to the best advantage.',
'06/09/91')

insert titles values ('MC2222', 'Silicon Valley Gastronomic Treats', 'mod_cook', '0877',
$19.99, $0.00, 12, 2032,
'Favorite recipes for quick, easy, and elegant meals.',
'06/09/91')

insert titles values ('TC7777', 'Sushi, Anyone?', 'trad_cook', '0877', $14.99, $8000.00,
10, 4095,
'Detailed instructions on how to make authentic Japanese sushi in your spare time.',
'06/12/91')

insert titles values ('TC4203', 'Fifty Years in Buckingham Palace Kitchens', 'trad_cook',
'0877', $11.95, $4000.00, 14, 15096,
'More anecdotes from the Queen''s favorite cook describing life among English royalty. Recipes, techniques, tender vignettes.',
'06/12/91')

insert titles values ('PC1035', 'But Is It User Friendly?', 'popular_comp', '1389',
$22.95, $7000.00, 16, 8780,
'A survey of software for the naive user, focusing on the ''friendliness'' of each.',
'06/30/91')

insert titles values('BU2075', 'You Can Combat Computer Stress!', 'business', '0736',
$2.99, $10125.00, 24, 18722,
'The latest medical and psychological techniques for living with the electronic office. Easy-to-understand explanations.',
'06/30/91')

insert titles values('PS2091', 'Is Anger the Enemy?', 'psychology', '0736', $10.95,
$2275.00, 12, 2045,
'Carefully researched study of the effects of strong emotions on the body. Metabolic charts included.',
'06/15/91')

insert titles values('PS2106', 'Life Without Fear', 'psychology', '0736', $7.00, $6000.00,
10, 111,
'New exercise, meditation, and nutritional techniques that can reduce the shock of daily interactions. Popular audience. Sample menus included, exercise video available separately.',
'10/05/91')

insert titles values('MC3021', 'The Gourmet Microwave', 'mod_cook', '0877', $2.99,
$15000.00, 24, 22246,
'Traditional French gourmet recipes adapted for modern microwave cooking.',
'06/18/91')

insert titles values('TC3218', 'Onions, Leeks, and Garlic: Cooking Secrets of the Mediterranean',
'trad_cook', '0877', $20.95, $7000.00, 10, 375,
'Profusely illustrated in color, this makes a wonderful gift book for a cuisine-oriented friend.',
'10/21/91')

insert titles values ('BU7832', 'Straight Talk About Computers', 'business', '1389',
$19.99, $5000.00, 10, 4095,
'Annotated analysis of what computers can do for you: a no-hype guide for the critical user.',
'06/22/91')

insert titles values('PS1372', 'Computer Phobic AND Non-Phobic Individuals: Behavior Variations',
'psychology', '0877', $21.59, $7000.00, 10, 375,
'A must for the specialist, this book examines the difference between those who hate and fear computers and those who don''t.',
'10/21/91')

insert titles (title_id, title, type, pub_id, notes) values('PC9999', 'Net Etiquette',
'popular_comp', '1389', 'A must-read for computer conferencing.')

insert titleauthor values('409-56-7008', 'BU1032', 1, 60)
insert titleauthor values('486-29-1786', 'PC9999', 1, 100)
insert titleauthor values('712-45-1867', 'MC2222', 1, 100)
insert titleauthor values('172-32-1176', 'PS3333', 1, 100)
insert titleauthor values('213-46-8915', 'BU1032', 2, 40)
insert titleauthor values('238-95-7766', 'PC1035', 1, 100)
insert titleauthor values('213-46-8915', 'BU2075', 1, 100)
insert titleauthor values('998-72-3567', 'PS2091', 1, 50)
insert titleauthor values('899-46-2035', 'PS2091', 2, 50)
insert titleauthor values('998-72-3567', 'PS2106', 1, 100)
insert titleauthor values('722-51-5454', 'MC3021', 1, 75)
insert titleauthor values('899-46-2035', 'MC3021', 2, 25)
insert titleauthor values('807-91-6654', 'TC3218', 1, 100)
insert titleauthor values('274-80-9391', 'BU7832', 1, 100)
insert titleauthor values('427-17-2319', 'PC8888', 1, 50)
insert titleauthor values('846-92-7186', 'PC8888', 2, 50)
insert titleauthor values('756-30-7391', 'PS1372', 1, 75)
insert titleauthor values('724-80-9391', 'PS1372', 2, 25)
insert titleauthor values('724-80-9391', 'BU1111', 1, 60)
insert titleauthor values('267-41-2394', 'BU1111', 2, 40)
insert titleauthor values('672-71-3249', 'TC7777', 1, 40)
insert titleauthor values('267-41-2394', 'TC7777', 2, 30)
insert titleauthor values('472-27-2349', 'TC7777', 3, 30)
insert titleauthor values('648-92-1872', 'TC4203', 1, 100)

insert stores values('7066','Barnum''s','567 Pasadena Ave.','Tustin','CA','92789')
insert stores values('7067','News & Brews','577 First St.','Los Gatos','CA','96745')
insert stores values('7131','Doc-U-Mat: Quality Laundry and Books',
      '24-A Avogadro Way','Remulade','WA','98014')
insert stores values('8042','Bookbeat','679 Carson St.','Portland','OR','89076')
insert stores values('6380','Eric the Read Books','788 Catamaugus Ave.',
      'Seattle','WA','98056')
insert stores values('7896','Fricative Bookshop','89 Madison St.','Fremont','CA','90019')

insert sales values('7066', 'QA7442.3', '09/13/94', 75, 'ON invoice','PS2091')
insert sales values('7067', 'D4482', '09/14/94', 10, 'Net 60','PS2091')
insert sales values('7131', 'N914008', '09/14/94', 20, 'Net 30','PS2091')
insert sales values('7131', 'N914014', '09/14/94', 25, 'Net 30','MC3021')
insert sales values('8042', '423LL922', '09/14/94', 15, 'ON invoice','MC3021')
insert sales values('8042', '423LL930', '09/14/94', 10, 'ON invoice','BU1032')
insert sales values('6380', '722a', '09/13/94', 3, 'Net 60','PS2091')
insert sales values('6380', '6871', '09/14/94', 5, 'Net 60','BU1032')
insert sales values('8042','P723', '03/11/93', 25, 'Net 30', 'BU1111')
insert sales values('7896','X999', '02/21/93', 35, 'ON invoice', 'BU2075')
insert sales values('7896','QQ2299', '10/28/93', 15, 'Net 60', 'BU7832')
insert sales values('7896','TQ456', '12/12/93', 10, 'Net 60', 'MC2222')
insert sales values('8042','QA879.1', '5/22/93', 30, 'Net 30', 'PC1035')
insert sales values('7066','A2976', '5/24/93', 50, 'Net 30', 'PC8888')
insert sales values('7131','P3087a', '5/29/93', 20, 'Net 60', 'PS1372')
insert sales values('7131','P3087a', '5/29/93', 25, 'Net 60', 'PS2106')
insert sales values('7131','P3087a', '5/29/93', 15, 'Net 60', 'PS3333')
insert sales values('7131','P3087a', '5/29/93', 25, 'Net 60', 'PS7777')
insert sales values('7067','P2121', '6/15/92', 40, 'Net 30', 'TC3218')
insert sales values('7067','P2121', '6/15/92', 20, 'Net 30', 'TC4203')
insert sales values('7067','P2121', '6/15/92', 20, 'Net 30', 'TC7777')
