-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE Players
( player_id serial primary key,
  player_name varchar(50) NOT NULL,
  num_wins Integer DEFAULT 0,
  num_matches Integer DEFAULT 0
);

CREATE TABLE Matches
( winner_id Integer NOT NULL,
  loser_id Integer NOT NULL,
  CONSTRAINT matches_pk PRIMARY KEY (winner_id, loser_id),
  CONSTRAINT fk_player1
    FOREIGN KEY (winner_id)
    REFERENCES Players(player_id),
  CONSTRAINT fk_player2
    FOREIGN KEY (loser_id)
    REFERENCES Players(player_id)
);

CREATE VIEW Standings AS
  SELECT player_id, player_name, num_wins, num_matches 
  FROM Players 
  ORDER BY num_wins ASC;
