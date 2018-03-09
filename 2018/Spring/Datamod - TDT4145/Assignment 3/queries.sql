-- 1

  -- c) 1
  INSERT INTO director VALUES(1, "Peyton Reed"),(2, "Tom Shadyac");
  --    2
  INSERT INTO film VALUES(1, "Yes Man", 2008, 1);
  --    3
  INSERT INTO actor VALUES(1, "Jim Carrey", 1962);
  --    4
  INSERT INTO actorforfilm VALUES(1,1,"Carl");

  -- d)
  UPDATE actor SET actorname="James Eugene Carrey" WHERE actorname="Jim Carrey";
  -- e) Check only director, or all tables?
  DELETE FROM director WHERE directorname="Tom Shadyac";

-- 2

  -- a)
  SELECT * FROM film;
  -- b)
  SELECT actorname FROM actor WHERE yearofbirth>1960;
  -- c)
  SELECT actorname FROM actor WHERE yearofbirth>1979 AND yearofbirth<1990 ORDER BY actorname ASC;
  -- d)
  SELECT title, filmrole FROM film NATURAL JOIN actorforfilm NATURAL JOIN actor WHERE actorname="Morgan Freeman";
  -- e)
  SELECT DISTINCT title FROM film NATURAL JOIN director JOIN actor ON directorname=actorname;
  -- f)
  SELECT COUNT(*) AS begin_with_c FROM actor WHERE actorname LIKE "C%" ; 
  -- g)
  SELECT genrename, COUNT(genrename) FROM genreforfilm NATURAL JOIN genre GROUP BY genrename;
  -- h)
  SELECT actorname FROM film NATURAL JOIN actorforfilm 
      NATURAL JOIN actor
        WHERE title="Ace Ventura: Pet Detective"
    AND actorname NOT IN 
  (SELECT actorname FROM film NATURAL JOIN actorforfilm 
      NATURAL JOIN actor
        WHERE title="Ace Ventura: When Nature Calls");
  -- i)
  SELECT title, filmID, ROUND(AVG(yearofbirth), 0) AS avg_yearofbirth FROM film
  NATURAL JOIN actorforfilm NATURAL JOIN actor
  GROUP BY filmID HAVING AVG(yearofbirth) > (SELECT AVG(yearofbirth) FROM actor)
  ORDER BY avg_yearofbirth;



