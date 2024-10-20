use challenge;
SELECT 
    *
FROM 
    `challenges_-_challenges`
WHERE 
    status = 'published'
    AND created_at >= CURDATE() - INTERVAL 3 MONTH
ORDER BY 
    created_at DESC;