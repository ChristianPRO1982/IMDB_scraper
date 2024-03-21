-- requête nécessaire car les urls ne sont pas sélectionné sans les "?"

WITH tt AS (SELECT m2.url
		      FROM movies250 m 
		      JOIN movies250 m2 ON m2.title = m.title
		                       AND m2.url > m.url
		     WHERE m.year = m2.year
		       AND m.duration = m2.duration)
DELETE FROM movies250 
 WHERE url IN (SELECT url FROM tt)