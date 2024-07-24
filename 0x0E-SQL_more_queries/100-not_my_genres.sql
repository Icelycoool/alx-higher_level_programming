-- Lists all genres not linked to the show Dexter.
SELECT g.name
FROM tv_genres AS g
WHERE g.id NOT IN (
	SELECT tg.genre_id
	FROM tv_show_genres AS tg
	INNER JOIN tv_shows AS t ON tg.show_id = t.id
	WHERE t.title = 'Dexter'
)
ORDER BY g.name ASC;
