-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT t.`title` AS title, g.`name` AS name
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS tg
ON t.`id` = tg.`show_id`
LEFT JOIN `tv_genres` AS g
ON g.`id` = tg.`genre_id`
ORDER BY title ASC;
