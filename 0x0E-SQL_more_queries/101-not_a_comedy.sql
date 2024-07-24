-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT t.title
FROM tv_shows AS t
WHERE t.id NOT IN (
	SELECT tg.show_id
	FROM tv_show_genres AS tg
	INNER JOIN tv_genres AS g ON tg.genre_id = g.id
	WHERE g.name = 'Comedy'
)
ORDER BY t.title ASC;
