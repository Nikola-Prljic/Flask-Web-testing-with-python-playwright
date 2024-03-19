DROP TABLE IF EXISTS post;

CREATE TABLE post (
  id INT PRIMARY KEY AUTO_INCREMENT,
  post_number INT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  author TEXT NOT NULL,
  message TEXT NOT NULL
);

drop table if exists users;

CREATE TABLE users (
  id integer primary key autoincrement,
  username VARCHAR(10) not null,
  password VARCHAR(50) not null,
  UNIQUE(password),
);
