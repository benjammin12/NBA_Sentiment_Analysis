import requests
import nba_py
from nba_py import player
import json

# URL = http://stats.nba.com/stats/playergamelog?PlayerID=2544&LeagueID=00&Season=2017-18&SeasonType=Regular+Season
#data = requests.get('http://stats.nba.com/stats/playergamelog?PlayerID=2544&LeagueID=00&Season=2017-18&SeasonType=Regular+Season')


class GameData:
    games = []

    #constructor
    def __init__(self):
        #player id is for lebron james
        james = player.PlayerGameLogs('2544', '00', '2017-18', "Regular Season")

        #get the json array resultSets
        resp = james.json['resultSets']

        #store each of the games in a list
        for x in resp:
            self.games = x['rowSet']

    #Prints out stats for all the games of the selected season
    def print_all_game_stats(self):
        # Print out games with index
        for i in range(len(self.games)):
            print("Game", len(self.games)-i, "stats for player is:", self.games[i])

    #gets the scores from a certain game, 0 the being the most recent
    #to the total amount of games played this season
    #games is a 2d array, each game has stats for the selected player which matched
    #up with the scores on ESPN and NBA stats
    def get_game_data(self,game):
        print("Game Date:", self.games[game][3])
        print("Points:", self.games[game][24])
        print("Assists:", self.games[game][19])
        print("Rebounds:", self.games[game][18])


lebronsGames = GameData()
lebronsGames.print_all_game_stats()
lebronsGames.get_game_data(0)
