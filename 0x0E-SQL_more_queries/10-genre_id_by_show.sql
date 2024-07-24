-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS g
ON g.`show_id` = s.`id`
ORDER BY s.`title`, g.`genre_id` ASC;
