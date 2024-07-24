-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.`title` AS title
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS tg
ON t.`id` = tg.`show_id`
INNER JOIN `tv_genres` AS g
ON g.`id` = tg.`genre_id`
WHERE g.`name` = 'Comedy'
ORDER BY title;
