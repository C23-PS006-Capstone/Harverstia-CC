CREATE TABLE records (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    title VARCHAR(25) NOT NULL,
    attachment VARCHAR(255),
    date DATETIME NOT NULL,
    article TEXT
);