import json
import tweepy
from tweepy import OAuthHandler, API
from discord_webhook import DiscordWebhook

# OPEN CONFIG FILE
config = dict()
with open('config.json') as CONFIG:
    config = json.load(CONFIG)

# PARSE CONFIG FILE
consumer = config['consumer']
consumer_s = config['consumer_s']
token = config['token']
token_s = config['token_s']
bool_only_author = config['bool_only_author']
users = config['usernames_to_watch']
webhooks = config['webhook_urls']

# 0AUTH
auth = OAuthHandler(consumer, consumer_s)
auth.set_access_token(token, token_s)
auth.secure = True
api = API(auth) 

# VALIDATE USERS TO FOLLOW AND CREATE USERS OBJECT
feed = []
for username in users:
    try:
        user = api.get_user(screen_name=username)
        feed.append(str(user.id))
    except Exception as f:
        print("[%s] -> Failed to add %s to feed! (%s)" % (username, str(f),))
        continue

    print("[%s] -> Successfully added %s to feed!" % (username, username,))

# CLASS OUR STREAM LISTENER
class MyStreamListener(tweepy.StreamListener):
    
    # ON STATUS
    def on_status(self, status):
        if bool_only_author:
            if status.author.screen_name not in users:
                return 

        webhook = DiscordWebhook(
            url=webhooks,
            username="%s @%s" % (status.author.name, status.author.screen_name,),
            avatar_url=status.author.profile_image_url,
            content= "https://twitter.com/%s/status/%s" % (status.author.screen_name, status.id,)
            )
        _ = webhook.execute()
    
    # ON ERROR - RESETS STREAM
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return True        

# INITIALIZE THE LISTENER AND STREAM
while True:
    try:
        print("[LISTENING TO STREAM]")
        myStreamListener = MyStreamListener()
        myStream = Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(follow=feed)
    except Exception as f:
        print("[ERROR] -> %s" % (f,))
        print("[RESTARTING]")
