import praw
import time
from prawoauth2 import PrawOAuth2Mini
from tokens import access_token, refresh_token, app_key, app_secret
from settings import user_agent, scopes

to_user="/u/weekerman"
#post_title="Weekly Coders, Hackers & All Tech related thread"
key_words=['weekly','coders','hackers', 'thread']

reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,app_secret=app_secret,access_token=access_token,
	                          refresh_token=refresh_token, scopes=scopes)
reddit_client.login('weekerman', 'wickerman')

def is_posted():
    subreddit = reddit_client.get_subreddit('india')
    for submission in subreddit.get_hot(limit=10):
        print submission.title
        search_title = 'weekly coders'
        if search_title in submission.title.lower() and submission.author == 'avinassh':
            print('in if leg')
            send_message()

def send_message():
    reddit_client.send_message('weekerman', 'Here is a sample subject.', 'Here is a sample text body.')

def main():
  while True:
  	try:
  		is_posted()
  	except praw.errors.OAuthInvalidToken:
  		oauth_helper.refresh()
  	time.sleep(1800)
if __name__ == '__main__':
	main()