-- Table definitions for the tournament project.

-- Table contains fields relating to specific players in the tournament
CREATE TABLE Players
( player_id serial primary key,
  player_name varchar(50) NOT NULL,
  num_wins Integer DEFAULT 0,
  num_matches Integer DEFAULT 0
);

-- Table identifies the winners/losers of each match in the tournament
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

-- View lists all players in the tournament ordered by the number of wins
CREATE VIEW Standings AS
  SELECT player_id, player_name, num_wins, num_matches 
  FROM Players 
  ORDER BY num_wins ASC;
