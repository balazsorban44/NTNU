CREATE DATABASE o3;
USE o3;


CREATE TABLE director(
  directorID INT NOT NULL,
  directorname VARCHAR(30) NOT NULL,
  CONSTRAINT PK_directorID PRIMARY KEY (directorID)
);


CREATE TABLE film(
  filmID INT NOT NULL,
  title VARCHAR(50) NOT NULL,
  productionyear INT(4) NOT NULL,
  directorID INT,
  CONSTRAINT PK_filmID PRIMARY KEY (filmID),
  CONSTRAINT FK_film_director_directorID FOREIGN KEY (directorID)
    REFERENCES director(directorID)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);


CREATE TABLE actor(
  actorID INT NOT NULL,
  actorname VARCHAR(30) NOT NULL,
  yearofbirth INT(4),
  CONSTRAINT PK_actorID PRIMARY KEY (actorID)
);


CREATE TABLE genre(
  genreID INT NOT NULL,
  genrename VARCHAR(30) NOT NULL,
  genredescription VARCHAR(200),
  CONSTRAINT PK_genreID PRIMARY KEY (genreID)
);


CREATE TABLE genreforfilm(
  genreID INT,
  filmID INT,
  CONSTRAINT FK_genreforfilm_genre_genreID 
    FOREIGN KEY (genreID)
      REFERENCES genre(genreID),
  CONSTRAINT FK_genreforfilm_film_filmID
    FOREIGN KEY (filmID)
      REFERENCES film(filmID)
);


CREATE TABLE actorforfilm(
  filmID INT,
  actorID INT,
  filmrole VARCHAR(30) NOT NULL,
  CONSTRAINT FK_actorforfilm_film_filmID
    FOREIGN KEY (filmID)
      REFERENCES film(filmID),
  CONSTRAINT FK_actorforfilm_actor_actorID 
    FOREIGN KEY (actorID)
      REFERENCES actor(actorID)
);


