import praw
from prawoauth2 import PrawOAuth2Mini

reddit_client = praw.Reddit('Project by /u/weekerman')
oauth_helper = PrawOAuth2Mini(reddit_client, app_key=app_key,app_secret=app_secret,access_token=access_token,
	                          refresh_token=refresh_token, scopes=scopes)

# login code goes here

subreddit = reddit_client.get_subreddit(subreddit)
comments = subreddit.get_comments()

def main()
  while True:
         