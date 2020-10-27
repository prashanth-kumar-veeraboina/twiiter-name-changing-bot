import tweepy  # go to tweepy documentation
import os  # operating system
import time
def create_api():

  consumer_key=os.getenv('consumer_key')    #these keys wiil be given in heroku  
  
  consumer_secret=os.getenv('consumer_secret')  #api secret key in tweeter developer
  access_token=os.getenv('access_token')  #generate access tokens
  access_token_secret=os.getenv('access_token_secret')
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)  ## we are adding two more arguments
  api.verify_credentials()  

 ## print("API created")
  return api

def follower_count(user):

   emoji_number={0:'0️⃣',1:'1️⃣',2:'2️⃣',3:'3️⃣',4:'4️⃣',
                  5:'5️⃣', 6:'6️⃣',7:'7️⃣',8:'8️⃣', 9:'9️⃣'}
                           

   uf_splits=[int(i) for i in str(user.followers_count)] #list comprehension spliting followers

   emoji_followers= ''.join([emoji_number[j] for j in uf_splits  if j in emoji_number.keys()])#followers in emojies
   return(emoji_followers)

api = create_api()
while True:
  user=api.get_user('prashan95113660')
  api.update_profile(name=f'prashanthkumar {follower_count(user)}')
  print(f'ypdating twitter name:PRASHANTH|{follower_count(user)}Followers')
  print('Waiting to refresh')
  time.sleep(60) 
