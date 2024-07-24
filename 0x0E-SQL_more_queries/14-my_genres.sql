-- Displays a list all genres of the show Dexter.
SELECT g.`name` AS name
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS tg
ON t.`id` = tg.`show_id`
INNER JOIN `tv_genres` AS g
ON g.`id` = tg.`genre_id`
WHERE t.`title` = 'Dexter'
ORDER BY name ASC;
