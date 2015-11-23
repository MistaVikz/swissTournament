#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Matches")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Players")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM Players")
    conn.commit()
    myCount = c.fetchone()[0]
    conn.close()
    return myCount


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Players (player_name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM Standings")
    conn.commit()
    myResult = c.fetchall()
    conn.close()
    return myResult


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    sql1 = "INSERT INTO Matches VALUES (%s, %s)"
    sql2 = "UPDATE Players SET num_wins = num_wins + 1, num_matches = num_matches+1 WHERE player_id = %s"
    sql3 = "UPDATE Players SET num_matches = num_matches+1 WHERE player_id = %s"
    conn = connect()
    c = conn.cursor()
    c.execute(sql1, (winner, loser))
    c.execute(sql2, (winner,))
    c.execute(sql3, (loser,))
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id_one, name_one, id_two,
      name_two)
        id_one: the first player's unique id
        name_one: the first player's name
        id_two: the second player's unique id
        name_two: the second player's name
    """
    sPair = []

    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM Standings")
    currentRound = c.fetchall()

    """ Pick the player from Standings with the most wins. Remove from the list.
    Loops until the list is empty. """
    while len(currentRound) > 0:
        id_one = currentRound[0][0]
        name_one = currentRound[0][1]
        num_wins = currentRound[0][2]

        currentRound.pop(0)

        """ Match the player with the next player in the standings """
        sPair.append([id_one, name_one, currentRound[0][0], currentRound[0][1]])
        currentRound.pop(0)
        
    conn.close()
    return sPair

   
