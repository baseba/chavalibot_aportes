import tweepy
import time
import  random
import frases

consumer_key = 'acces_key'
consumer_secret = 'secret_key'

access_token = 'token de acceso'
access_token_secret = 'token secreto'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()




"""

mentions = api.mentions_timeline()

for mention in mentions :
    print(mention.id, mention.text
          )

"""

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
def reply_to_tweets():
    print('retrieving and replying to tweets ...')
    last_seen_id = retrieve_last_seen_id('last_id.txt')

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended'
    )


    for mention in reversed(mentions):
        print(f'{str(mention.id)} - {mention.full_text}')
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, 'last_id.txt')

        if 'acabalo' in mention.full_text.lower()  or 'acábalo' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_acabalo)}',
                              mention.id)
        elif 'cheeto' in mention.full_text.lower()  or 'chencho' in mention.full_text.lower():
            print('cheeto')
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_chencho)}',
                          mention.id)
        elif 'dario' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_dario)}',
                          mention.id)
        elif 'orson' in mention.full_text.lower() or 'orslok' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_orson)}',
                          mention.id)
        elif 'marta' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_marta)}',
                          mention.id)
        elif 'nelu' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_nelu)}',
                          mention.id)
        elif 'concha' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_concha)}',
                          mention.id)
        elif 'creador' in mention.full_text.lower():
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_creador)}',
                          mention.id)
        else:
            api.update_status(f'@{mention.user.screen_name} {random.choice(frases.frases_else)}',
                          mention.id)



while True :
    reply_to_tweets()

    if time.strftime("%w:%H:%M") == '1:13:55' or time.strftime("%w:%H:%M") == '4:13:55':
        api.update_status('a liar que en brevas se viene esta wea conchetumareee! https://www.twitch.tv/yointerneto')
    elif time.strftime("%H:%M") == '13:55' or time.strftime("%H:%M") == '21:35' or time.strftime("%H:%M") == '17:20' or time.strftime("%H:%M") == '9:10':
        api.update_status(random.choice(frases.frases_random))
    time.sleep(60)
