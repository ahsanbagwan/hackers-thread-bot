import praw
from prawoauth2 import PrawOAuth2Mini
from tokens import access_token, refresh_token, app_key, app_secret
from settings import user_agent, scopes

to_user="/u/weekerman"

reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,app_secret=app_secret,access_token=access_token,
	                          refresh_token=refresh_token, scopes=scopes)

# login code goes here
def isPosted():
    subreddit = reddit_client.get_subreddit(subreddit)
    comments = subreddit.get_comments()

def main():
  while True:
  	try:
  		isPosted()
  	except praw.errors.OAuthInvalidToken:
  		oauth_helper.refresh()
  		
if __name__ == '__main__':
	main()