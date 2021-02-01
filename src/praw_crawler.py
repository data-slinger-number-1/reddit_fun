# praw crawler
# https://praw.readthedocs.io/en/latest/tutorials/comments.html
import praw
import os


reddit_username = 'BobDope'
reddit_password = os.environ['reddit_pass']

app_id = 'V5ZGRnUFVkQGiw'
app_secret = os.environ['reddit_secret']

reddit = praw.Reddit(
    user_agent="'reddit_analytics by /u/BobDope 0.0.1'",
    client_id=app_id,
    client_secret=app_secret,
    username="BobDope",
    password=reddit_password
)

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)


submission = reddit.submission(id="3g1jfi")

for top_level_comment in submission.comments:
    print(top_level_comment.body)


from praw.models import MoreComments

for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)


submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)



submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
    for second_level_comment in top_level_comment.replies:
        print(second_level_comment.body)

submission.comments.replace_more(limit=None)
comment_queue = submission.comments[:]  # Seed with top-level
while comment_queue:
    comment = comment_queue.pop(0)
    print(comment.body)
    comment_queue.extend(comment.replies)

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)


#also

for submission in reddit.subreddit("all").hot(limit=25):
    print(submission.title)

for comment in reddit.subreddit("redditdev").comments(limit=25):
    print(comment.author)

