DROP TABLE IF EXISTS post;

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  post_number INTEGER,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  author TEXT NOT NULL,
  message TEXT NOT NULL
);

drop table if exists users;

create table users (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);
