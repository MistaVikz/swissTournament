# swissTournament
Database schema for a Swiss Pairing Tournament in Python and PSQL

Included Files:
  - tournament.sql (Creates tables and views to store information for a swiss pariring tournament.)
  - tournament_test.py (Test cases that demonstrate the implementation of tournament.py.)
  - tournament.py (A library of functions used by tournament_test.py to access the database.)
  
Setup Instructions:
  1.  Access the files:
      i.    Run the vagrant virutal machine.
      ii.   Use cd /vagrant/tournament to switch to the tournament directory.
  
  2.  Initial Setup:
      NOTE: If the follow steps have already be performed, proceed to 3.
      i.    Use the command: psql to enter the psql command line.
      ii.   Use the command: CREATE DATABASE tournament; to create the tournament database.
      iii.  Use the command: \c tournament; to connect to the tournament database.
      iv.   Use the command: \i tournament.sql to create the tables and views in tournament.sql
  
  3.  Run the Test Cases:
      i.  Return to the tournament directory if necessary.
      ii. From the tournament directory use the command: python tournament_test.py
      
Supported Test Cases (in tournament_test.py):
  - testDeleteMatches(): 
      tournament.py functions:  deleteMatches() 
      Description:  Removes all the match records from the database.
    
  - testDelete(): 
      tournament.py functions:  deleteMatches(), deletePlayers()
      Description:  Removes all the match records and player records from the database.
    
  - testCount():
      tournament.py functions:  deleteMatches(), deletePlayers(), countPlayers()
      Description:  Removes all the matches and player records, then counts the number of 
                      registered players.
    
  - testRegister():
      tournament.py functions:  deleteMatches(), deletePlayers(), countPlayers(), 
                                registerPlayers()
      Description:  Removes all the matches and player records, registers a new players, then 
                    counts the number of registered players.
    
  - testRegisterCountDelete():
      tournament.py functions:  deleteMatches(), deletePlayers(), countPlayers(), 
                                registerPlayers()
      Description:  Removes all the matches and player records, registers 4 new players, counts 
                    the number of registered players, the removes all the matches and player
                    records.
    
  - testStandingsBeforeMatch():
      tournament.py functions:  deleteMatches(), deletePlayers(), registerPlayers(), 
                                playerStandings()
      Description:  Removes all the matches and player records, registers 2 new players,
                    retrieves the current standings, and tests that they are registered correctly
                    with no matches.
    
  - testReportMatches():
      tournament.py functions:  deleteMatches(), deletePlayers(), registerPlayers(), 
                                playerStandings(), reportMatch()
      Description:  Removes all the matches and player records, registers 4 new players,
                    retrieves the current standings. Then records two matches and retrieves the
                    standings after the matches. Tests that each player has 1 match recorded,
                    each winner has 1 win recorded, and each loser has 0 wins recorded.
  - testPairings():
      tournament.py functions:  deleteMatches(), deletePlayers(), registerPlayers(), 
                                playerStandings(), reportMatch(), swissPairing() 
      Description:  Removes all the matches and player records, registers 4 new players,
                    and retrieves the current standings. Then records two matches and runs the swiss
                    pairing algorithm. Then tests that the algorithm returns two pairs, with the players
                    that have one win paired together.
  
Limitations:
  The database schema supports a single swiss tournament with a even number of players. Does not support
  byes for a odd number of players, multiple tournaments, ties, or matching via opponent's match wins.
    
  
  
  
