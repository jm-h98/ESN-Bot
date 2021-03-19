import os
import random
import praw

reddit = praw.Reddit(
    client_id=os.getenv('ClientID'),
    client_secret=os.getenv('ClientSecret'),
    password=os.getenv('PW'),
    user_agent="ESNbot",
    username=os.getenv('User'),
    check_for_async=False
)

def get_meme():
  subs = ["ich_iel", "HistoryMemes", "me_irl", "MettzgereiWinkler", "TIHI", "redneckengineering", "okbrudimongo","okbuddyretard", "cursedimages", "BikiniBottomTwitter", "blursedimages", "mauerstrassenwetten"]
  subreddit = reddit.subreddit(random.choice(subs))
  submissions = []
  submission_buffer = subreddit.hot(limit=25)
  for submission in submission_buffer:
    submissions.append(submission)
  post = random.choice(submissions)
  return post.title + "\n" + post.url


def get_meme_sub(sub):
  subreddit = reddit.subreddit(random.choice(sub))
  submissions = []
  submission_buffer = subreddit.hot(limit=25)
  for submission in submission_buffer:
    submissions.append(submission)
  post = random.choice(submissions)
  return post.title + "\n" + post.url
