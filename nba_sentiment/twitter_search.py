try:
    import json
except ImportError:
    import simplejson as json


from datetime import datetime
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from .nba_tweet import NBATweet


class NBATwitter:

    def __init__(self):
        self.ACCESS_TOKEN = '922879421765292033-MFe0ymt9uhyNWkDpMBclu9eKo74duAV'
        self.ACCESS_SECRET = 'KJrDKS3ui4qSwGMATnVcSFDZB8IDy2UShAdNhJTZSgw48'
        self.CONSUMER_KEY = 'iSfsQLFJX8vgYIPpNG0CGD1lK'
        self.CONSUMER_SECRET = '1LoF8oKZMgh2ml8KYrvLJZdqZ4nuUORXrMLepCi10R1SV5462t'
        self.oauth = OAuth(self.ACCESS_TOKEN, self.ACCESS_SECRET, self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.twitter = Twitter(auth=self.oauth)

    def get_latest_nba_athlete_status(self, text):
        nba_player_query = self.twitter.statuses.user_timeline(screen_name=text)
        nba_tweet = NBATweet(nba_player_query[0]["text"], nba_player_query[0]["created_at"])
        return nba_tweet

    def get_players_latest_ten_tweets(self, text):
        nba_player_query = self.twitter.statuses.user_timeline(screen_name=text)
        nba_status_array = []
        for idx, result in enumerate(nba_player_query):
            nba_status_array[idx] = NBATweet(result["text"], result["created_at"])
        return nba_status_array

    def get_player_tweet_from_date(self, text, days=None, months=None):
        datetime_object = datetime.now()
        if days is not None and months is not None:
            datetime_object = datetime_object.replace(day=days, month=months)
        elif days is not None:
            datetime_object = datetime_object.replace(day=days)
        elif months is not None:
            datetime_object = datetime_object.replace(month=months)

        nba_player_query = self.twitter.statuses.user_timeline(screen_name=text)
        for result in nba_player_query:
            tweet_datetime = datetime.strptime(result["created_at"], '%a %e %b %Y %H:%M:%S %z')
            if datetime_object.date() == tweet_datetime.date():
                return NBATweet(result["text"], result["created_at"])

    def get_variable_latest_nba_player_status_tweets(self, text, num):
        nba_player_query = self.twitter.statuses.user_timeline(screen_name=text)
        nba_status_array = []
        for idx, result in enumerate(nba_player_query):
            if idx < num:
                nba_status_array[idx] = NBATweet(result["text"], result["created_at"])
        return nba_status_array

    def print_player_tweets(self, text):
        query = self.twitter.statuses.user_timeline(screen_name=text)
        for result in query:
            print("(%s) @%s %s" % (result['created_at'], result['user']['screen_name'], result["text"]))


# for result in query['statuses']:
#     print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
#     for result in query2:
#         print("(%s) @%s %s" % (result['created_at'], result['user']['screen_name'], result["text"]))

nba = NBATwitter()
nba.print_player_tweets("StephenCurry30")
