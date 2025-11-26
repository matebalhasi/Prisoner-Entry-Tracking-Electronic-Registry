CREATE DATABASE PrisonDB;

CREATE TABLE Prison (
    Prison_ID SERIAL PRIMARY KEY,
    Prison_Name VARCHAR(100) NOT NULL,
    Prison_Location VARCHAR(200),
	Warden INT References Prison_Guard(Guard_ID)
);

CREATE TABLE Block (
    Block_ID SERIAL PRIMARY KEY,
    Status int REFERENCES Block_Status(Status_ID),
    Block_Name VARCHAR(50),
    Prison_ID INT REFERENCES Prison(Prison_ID)
);

CREATE TABLE Block_Status(
	Status_ID SERIAL PRIMARY KEY,
	Status_Name VARCHAR(50)
);

CREATE TABLE Cell (
    Cell_Number SERIAL PRIMARY KEY,
    Block_ID INT REFERENCES Block(Block_ID)
);

CREATE TABLE Prison_Guard (
    Guard_ID SERIAL PRIMARY KEY,
    Birth_Date DATE,
    F_Name VARCHAR(50),
    L_Name VARCHAR(50),
    Rank VARCHAR(50),
    Prison_ID INT REFERENCES Prison(Prison_ID),
    Block_ID INT REFERENCES Block(Block_ID)
);

CREATE TABLE Prisoner (
    ID SERIAL PRIMARY KEY,
    Birth_Date DATE,
    F_Name VARCHAR(50),
    L_Name VARCHAR(50),
    Danger_Level VARCHAR(50),
    Prison_ID INT REFERENCES Prison(Prison_ID),
    Cell_Number INT REFERENCES Cell(Cell_Number)
);

CREATE TABLE Crimes (
    Crime_ID SERIAL PRIMARY KEY,
    Crime_Name VARCHAR(100)
);

CREATE TABLE Charges (
    Charge_ID SERIAL PRIMARY KEY,
    Sentence VARCHAR(100),
    Crimes_Committed VARCHAR(200),
    Prisoner_ID INT REFERENCES Prisoner(ID),
    Crime_ID INT REFERENCES Crimes(Crime_ID)
);

CREATE TABLE Sentences (
    Sentence_ID SERIAL PRIMARY KEY,
    Sentence_Type VARCHAR(100),
    Duration INT,
    Start_Date DATE,
    End_Date DATE,
    Charge_ID INT REFERENCES Charges(Charge_ID)
);

CREATE TABLE Appeals (
    Appeal_Number SERIAL PRIMARY KEY,
    Appeal_Date DATE,
    Location VARCHAR(100),
    Judge VARCHAR(100),
    Prisoner_ID INT REFERENCES Prisoner(ID),
    Sentence_ID INT REFERENCES Sentences(Sentence_ID)
);

CREATE TABLE Prisoner_Log (
    Log_ID SERIAL PRIMARY KEY,
    Deleted_At TIMESTAMP NOT NULL DEFAULT NOW(),
    ID INT,
    Birth_Date DATE,
    F_Name VARCHAR(50),
    L_Name VARCHAR(50),
    Danger_Level VARCHAR(50),
    Prison_ID INT,
    Cell_Number INT
);
CREATE OR REPLACE FUNCTION log_prisoner_delete()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO Prisoner_Log(ID, Birth_Date, F_Name, L_Name, Danger_Level, Prison_ID, Cell_Number)
    VALUES (OLD.ID, OLD.Birth_Date, OLD.F_Name, OLD.L_Name, OLD.Danger_Level, OLD.Prison_ID, OLD.Cell_Number);

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_prisoner_delete
AFTER DELETE ON Prisoner
FOR EACH ROW
EXECUTE FUNCTION log_prisoner_delete();

