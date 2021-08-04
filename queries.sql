SELECT c.id,
    u.username,
    c.created_at,
    c.content
FROM comments AS c
    INNER JOIN users AS u ON u.id = c.user_id
    INNER JOIN posts AS p ON p.id = c.post_id
    WHERE p.id = 7;

SELECT p.id,
    p.title,
    p.publicated_at,
    t.tag,
    c.category,
    l.`language`
FROM posts AS p
    INNER JOIN languages AS l  ON l.id = p.language_id
    INNER JOIN categories AS c ON c.id = p.category_id
    INNER JOIN posts_tags AS pt ON pt.post_id = p.id
    INNER JOIN tags AS t ON t.id = pt.tag_id
    WHERE p.id LIKE '%'
ORDER BY p.publicated_at DESC;


SELECT posts.id,
    categories.category
FROM categories
    INNER JOIN posts ON categories.id = posts.category_id;

SELECT posts_tags.post_id,
    tags.tag
FROM tags
    INNER JOIN posts_tags ON tags.id = posts_tags.tag_id
    INNER JOIN posts ON posts_tags.post_id = posts.id;