import tweepy


CALL_BACK = 'oob'
QUERY = "Pessi"
TWEET_COUNT = 20
MESSAGE = "Penaldo's favorite tea is Penal-tea. He sips it with such grace and asks for seconds. Penaldo is and will always be a fraud in my book I'm afraid"


def retrieveKeys():
    try:
        keys = []
        key_file = open('keys.txt','r')
        line = key_file.readline()
        while line != "":
            arr = line.split()
            keys.append(arr[1])
            line = key_file.readline()
        return keys

    except IOError:
        print("Could not read file")        



def OAuth():
    keys = retrieveKeys()
    print(keys)
    try:
        auth = tweepy.OAuthHandler(keys[0], keys[1], CALL_BACK)
        auth.set_access_token(keys[2], keys[3])
        return auth
    except Exception as e:
        print("There was an error with OAuth")
        return



def main():
    
    auth = OAuth()
    api = tweepy.API(auth)



    penaldo_tweets = api.search(q=QUERY, count=TWEET_COUNT, result_type="recent")

    to_reply = []

    for tweet_no in range(TWEET_COUNT-1):
        tweet = penaldo_tweets[tweet_no]._json
        tweet_id = tweet['id']
        tweet_user = tweet["user"]["screen_name"]
        if tweet_user != "BotPenaldo":
            to_reply.append((tweet_id, tweet_user))


    for tweet in to_reply:
        reply = "@" + tweet[1] + " " + MESSAGE
        api.update_status(status=reply, in_reply_to_status_id=tweet[0], auto_populate_reply_metadata=True)
    
    print("Tweets were successful!")

if __name__ == "__main__":
    main()




