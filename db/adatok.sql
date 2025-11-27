-- Egy börtön, Alcatraz
INSERT INTO Prison (Prison_ID, Prison_Name, Prison_Location) VALUES
('010', 'Alcatraz', 'USA San Francisco');

-- Block státuszok
INSERT INTO Block_Status (Status_ID, Status_name) VALUES
('100', 'Alacsony'),
('200', 'Közepes'),
('300', 'Magas');

-- Blokkok mind az egy börtönhöz, státuszokkal
INSERT INTO Block (Block_ID, Status, Block_Name, Prison_ID) VALUES
('1001', 100, 'A blokk', '010'),
('1002', 200, 'B blokk', '010'),
('1003', 300, 'C blokk', '010'),
('1004', 300, 'Szigorúan Ellenőrzött Részleg', '010'),
('1005', 200, 'Karantén Zona', '010'),
('1006', 100, 'Különleges Figyelmet igénylők Osztálya', '010');

-- Cellák
INSERT INTO Cell (Cell_Number, Block_ID) VALUES
('001', 1001),
('002', 1001),
('003', 1002),
('004', 1002),
('005', 1003),
('006', 1003),
('007', 1004),
('008', 1004),
('009', 1005),
('010', 1005),
('011', 1006),
('012', 1006);

-- Őrök (Prison_ID minden esetben 010)
INSERT INTO Prison_Guard (Guard_ID, Birth_Date, F_Name, L_Name, Rank, Prison_ID, Block_ID) VALUES
('1100', '2000-04-25','László','Molnár','Őr','010',1001),
('1101', '1990-09-15','Ferenc','Bíró','Őr','010',1002),
('2100', '1992-03-05','Tamás','Fekete','Őr','010',1003),
('2101', '1975-10-01','István','Orosz','Őr','010',1004),
('3100', '1980-08-10','Károly','Szűcs','Őr','010',1005),
('3101', '1977-12-20','Balázs','Gulyás','Őr','010',1006),
('4100', '1985-05-11','Zoltán','Papp','Őr','010',1001),
('4101', '1993-11-30','Attila','Sipos','Őr','010',1002),
('5100', '1996-02-28','Jenő','Veres','Őr','010',1003),
('5101', '1980-01-31','Márton','Balla','Őr','010',1004);

-- Fogvatartottak (Prison_ID minden esetben 010)
INSERT INTO Prisoner (ID, Birth_Date, F_Name, L_Name, Danger_Level, Prison_ID, Cell_Number) VALUES
('1201','2000-01-13','János','Kovács','Közepes','010','001'),
('1202','1999-03-22','Miklós','Nagy','Alacsony','010','002'),
('1203','1995-12-01','Dávid','Szabó','Magas','010','003'),
('1204','1998-06-14','Dániel','Tóth','Közepes','010','004'),
('1205','2001-09-30','Tamás','Horváth','Alacsony','010','005'),
('1206','1997-02-10','Róbert','Varga','Alacsony','010','006'),
('1207','2000-04-19','Vilmos','Kiss','Magas','010','007'),
('1208','1999-07-25','András','Molnár','Közepes','010','008'),
('1209','1996-01-17','Tamás','Németh','Magas','010','009'),
('1210','2002-05-08','Richárd','Farkas','Alacsony','010','010'),
('2201','1994-09-11','Sámuel','Balogh','Közepes','010','001'),
('2202','1998-12-29','Antal','Kelemen','Magas','010','002'),
('2203','2000-03-06','György','Lakatos','Közepes','010','003'),
('2204','1995-07-22','Kristóf','Papp','Alacsony','010','004'),
('2205','1999-10-18','Jónás','Farkas','Magas','010','005'),
('2206','2001-02-28','Károly','Kovács','Alacsony','010','006'),
('2207','1997-08-09','Jázmin','Török','Alacsony','010','007'),
('2208','1996-11-24','Márton','Szalai','Alacsony','010','008'),
('2209','1994-05-13','Péter','Kocsis','Magas','010','009'),
('2210','2000-07-02','Sándor','Oláh','Közepes','010','010');

-- Bűncselekmények
INSERT INTO Crimes (Crime_ID, Crime_Name) VALUES
('101', 'Emberölés'),
('102', 'Rablás'),
('103', 'Kábítószer kereskedelem'),
('104', 'Csalás'),
('105', 'Sikkasztás'),
('106', 'Garázdaság'),
('107', 'Zsarolás'),
('108', 'Korrupció'),
('109', 'Adócsalás'),
('110', 'Közúti baleset okozása ittasan vagy gondatlanságból');

-- Vádak
INSERT INTO Charges (Charge_ID, Sentence, Crimes_Committed) VALUES
('201', 'Életfogytig tartó szabadságvesztés','Emberölés'),
('202', '15 év szabadságvesztés','Rablás'),
('203', '1 év szabadságvesztés','Kábítószer kereskedelem'),
('204', '5 év szabadságvesztés','Csalás'),
('205', '3 év szabadságvesztés','Sikkasztás'),
('206', '2 év felfüggesztett szabadságvesztés','Garázdaság'),
('207', '6 hónap szabadságvesztés','Zsarolás'),
('208', '8 hónap szabadságvesztés','Korrupció'),
('209', '1 év felfüggesztett szabadságvesztés','Adócsalás'),
('210', '1 év közmunkára átváltható szabadságvesztés','Közúti baleset okozása ittasan vagy gondatlanságból');

-- Ítéletek
INSERT INTO Sentences (Sentence_ID, Sentence_Type, Duration, Start_Date, End_Date) VALUES
('301', 'Életfogytig tartó szabadságvesztés', 10950, '2000-02-11', '2030-02-11'),
('302', '15 év szabadságvesztés', 5475, '2001-04-15', '2016-04-15'),
('303', '10 év szabadságvesztés', 3650, '2005-06-01', '2015-06-01'),
('304', '5 év szabadságvesztés', 1825, '2010-03-20', '2015-03-20'),
('305', '3 év szabadságvesztés', 1095, '2018-11-01', '2021-11-01'),
('306', '2 év felfüggesztett szabadságvesztés', 0, '2019-02-10', '2019-02-10'),
('307', '1 év szabadságvesztés', 365, '2020-07-01', '2021-07-01'),
('308', '6 hónap szabadságvesztés', 182, '2022-01-15', '2022-07-15'),
('309', 'Próbára bocsátás', 0, '2021-05-10', '2021-05-10'),
('310', '20 év tartós elzárás', 7300, '1999-12-01', '2019-12-01');

-- Fellebbezések
INSERT INTO Appeals (Appeal_Number, Appeal_Date, Location, Judge) VALUES
('401', '2010-04-15', 'Edinburgh Sheriff Court', 'Lady Dorrian'),
('402', '2012-06-20', 'Old Bailey, London', 'Sir Brian Leveson'),
('403', '2014-09-05', 'Supreme Court, New York', 'Justice Sonia Sotomayor'),
('404', '2015-11-12', 'Los Angeles County Court', 'Judge John Kronstadt'),
('405', '2016-02-28', 'High Court of Justice, London', 'Lady Justice Arden'),
('406', '2017-08-14', 'Edinburgh Sheriff Court', 'Lord Woolman'),
('407', '2018-05-21', 'Supreme Court, Washington D.C.', 'Justice Elena Kagan'),
('408', '2019-03-10', 'Old Bailey, London', 'Judge Nicholas Hilliard'),
('409', '2020-07-30', 'Los Angeles County Court', 'Judge Michael Feuer'),
('410', '2021-01-18', 'High Court of Justice, London', 'Lord Justice Popplewell');


INSERT INTO Guard_Shifts (Guard_ID, Shift_Day, Shift_Type, Start_Time, End_Time) VALUES
(1100, 'hétfő', 'day', '06:00', '18:00'),
(1100, 'szerda', 'night', '18:00', '06:00'),
(1101, 'hétfő', 'day', '06:00', '18:00'),
(1101, 'szerda', 'night', '18:00', '06:00'),
(2100, 'kedd', 'day', '06:00', '18:00'),
(2100, 'csütörtök', 'night', '18:00', '06:00'),
(2101, 'kedd', 'day', '06:00', '18:00'),
(2101, 'csütörtök', 'night', '18:00', '06:00'),
(3100, 'hétfő', 'day', '06:00', '18:00'),
(3100, 'szerda', 'night', '18:00', '06:00'),
(3101, 'hétfő', 'day', '06:00', '18:00'),
(3101, 'szerda', 'night', '18:00', '06:00'),
(4100, 'kedd', 'day', '06:00', '18:00'),
(4100, 'csütörtök', 'night', '18:00', '06:00'),
(4101, 'kedd', 'day', '06:00', '18:00'),
(4101, 'csütörtök', 'night', '18:00', '06:00'),
(5100, 'hétfő', 'day', '06:00', '18:00'),
(5100, 'szerda', 'night', '18:00', '06:00'),
(5101, 'hétfő', 'day', '06:00', '18:00'),
(5101, 'szerda', 'night', '18:00', '06:00');
