GRANT ALL PRIVILEGES ON mydb.* TO niki@0.0.0.0;

DROP TABLE IF EXISTS post;

CREATE TABLE post (
  id INT PRIMARY KEY AUTO_INCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  author TEXT NOT NULL,
  message TEXT NOT NULL
);

drop table if exists users;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(10) not null,
  password VARCHAR(50) not null,
  UNIQUE(username)
);

FLUSH PRIVILEGES;
