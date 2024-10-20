SELECT 
    u.id,
    u.video, 
    p.onboarding_goal,
    u.updated_at,
    u.created_at, 
    r.name
FROM 
    `users_-_users` u
JOIN 
    `profiles_-_hoja_1` p ON u.id = p.user_id
JOIN 
    `resumes_-_resumes` r ON u.id = r.user_id
WHERE 
    (p.onboarding_goal = 'be_discovered-[hire]' OR p.onboarding_goal = 'be_discovered-[collaborate]')
    AND r.type = 'pitch_video'
    AND u.video <> 'NULL'
    AND r.video <> ''
    AND r.created_at >= NOW() - INTERVAL 6 MONTH -- Solo trae los ultimos 6 meses, los datasets no tienen created_at < 2 meses
GROUP BY 
    u.id, u.video, p.onboarding_goal, u.updated_at, u.created_at, r.name;