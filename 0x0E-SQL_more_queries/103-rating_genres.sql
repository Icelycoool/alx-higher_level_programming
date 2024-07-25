-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.`name` AS name, SUM(r.`rate`) AS rating
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS tg
ON g.`id` = tg.`genre_id`
INNER JOIN `tv_show_ratings` AS r
ON r.`show_id` = tg.`show_id`
GROUP BY name
ORDER BY rating DESC;
