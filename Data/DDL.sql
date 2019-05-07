
/* Remove all tables and start fresh */

DROP TABLE IF EXISTS Stars;
DROP TABLE IF EXISTS Videos;
DROP TABLE IF EXISTS LastGames;
DROP TABLE IF EXISTS PlayerSTATs;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Teams;


/* Create Tables */

CREATE TABLE IF NOT EXISTS Teams (
        TeamAbbreviation CHAR(3),
        TeamName VARCHAR(25),
        PRIMARY KEY(TeamAbbreviation)
);

CREATE TABLE IF NOT EXISTS Users (
        UserID INT NOT NULL AUTO_INCREMENT,
		UserName VARCHAR(12),
        Password VARCHAR(50),
        Team CHAR(3),
        FOREIGN KEY(Team) REFERENCES Teams(TeamAbbreviation),
        PRIMARY KEY(UserID)
);


CREATE TABLE IF NOT EXISTS Players (
        PlayerID INT NOT NULL AUTO_INCREMENT,
        PlayerNumber INT,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Position VARCHAR(5),
        Team CHAR(3),
        FOREIGN KEY(Team) REFERENCES Teams(TeamAbbreviation),
        PRIMARY KEY(PlayerID)
);

CREATE TABLE IF NOT EXISTS PlayerSTATs (
        PlayerID INT NOT NULL,
        PPG DECIMAL(4,2),
        APG DECIMAL(4,2),
        RPG DECIMAL(4,2),
        SPG DECIMAL(4,2),
        BPG DECIMAL(4,2),
        TOVPG DECIMAL(4,2),
        FT_PERC DECIMAL(4,2),
        FG_PERC DECIMAL(4,2),
        FOREIGN KEY(PlayerID) REFERENCES Players(PlayerID),
        PRIMARY KEY(PlayerID)
);

CREATE TABLE IF NOT EXISTS LastGames (
	GameID INT NOT NULL AUTO_INCREMENT,
	Team CHAR(3) NOT NULL,
	WIN BOOLEAN,
	AT_HOME BOOLEAN NOT NULL,
	OpposingTeam CHAR(3) NOT NULL,
	Score VARCHAR(25),
	FOREIGN KEY(Team) REFERENCES Teams(TeamAbbreviation),
	FOREIGN KEY(OpposingTeam) REFERENCES Teams(TeamAbbreviation),
	PRIMARY KEY(GameID)
);

CREATE TABLE IF NOT EXISTS Videos (
        VideoID INT NOT NULL AUTO_INCREMENT,
        Team CHAR(3) NOT NULL,
        VideoUrlId VARCHAR(50),
        FOREIGN KEY(Team) REFERENCES Teams(TeamAbbreviation),
        PRIMARY KEY(VideoID)
);

CREATE TABLE IF NOT EXISTS Stars(
        StarID INT NOT NULL AUTO_INCREMENT,
        PlayerID INT,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Team CHAR(3),
        FOREIGN KEY(Team) REFERENCES Teams(TeamAbbreviation),
        FOREIGN KEY(PlayerID) REFERENCES Players(PlayerID),
        PRIMARY KEY(StarID)
);

