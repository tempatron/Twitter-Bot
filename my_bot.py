import tweepy
import time

print('my twitter bot')

CONSUMER_KEY = 'AA'
CONSUMER_SECRET = 'BB'
ACCESS_KEY = 'CC'
ACCESS_SECRET = 'DD'
# Replace with your keys

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

print(mentions[0].text)

for mention in mentions:
    if '#helloworld' in mention.text.lower():
        print('found hello world')

FILE_NAME = 'last_seen.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_helloworld():
    print('Retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back..')
            api.update_status('@' + mention.user.screen_name +
                              '#HelloWorld back to you!!', mention.id)


def reply_to_chaipeelo():
    print('Retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#chaipeelo' in mention.full_text.lower():
            print('#ChaiPeelo found ')
            print('responding back..')
            api.update_status('@' + mention.user.screen_name +
                              '#ChaiPeelo back to you!!', mention.id)


while True:
    reply_to_helloworld()
    time.sleep(15)
    reply_to_chaipeelo()
    time.sleep(15)
