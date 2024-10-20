use challenge;
SELECT 
    u.id AS user_id,
    u.name,
    u.email,
    SUM(p.views) AS total_views
FROM 
    `users_-_users` u
JOIN 
    `profiles_-_hoja_1` p ON u.id = p.user_id
GROUP BY 
    u.id, u.name, u.email
ORDER BY 
    total_views DESC
LIMIT 3; 