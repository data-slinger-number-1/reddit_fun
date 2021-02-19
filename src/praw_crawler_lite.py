# praw crawler
# https://praw.readthedocs.io/en/latest/tutorials/comments.html
#also https://fasttext.cc/docs/en/supervised-tutorial.html

import os
import sys
import time
import praw
from praw.models import MoreComments

import re
from nltk.stem import WordNetLemmatizer

stemmer = WordNetLemmatizer()

def preprocess_text(document):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(document))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        tokens = document.split()
        tokens = [stemmer.lemmatize(word) for word in tokens]
        tokens = [word for word in tokens if word not in en_stop]
        tokens = [word for word in tokens if len(word) > 3]

        preprocessed_text = ' '.join(tokens)

        return preprocessed_text

reddit_username = os.environ['reddit_username']
reddit_password = os.environ['reddit_pass']

app_id = os.environ['app_id']
app_secret = os.environ['reddit_secret']

reddit = praw.Reddit(
    user_agent="'reddit_analytics by /u/%s 0.0.1'" % reddit_username,
    client_id=app_id,
    client_secret=app_secret,
    username=reddit_username,
    password=reddit_password
)

def normalize_text(text):

    text = text.replace("\n", " ")
    text = text.lower()
    return(text)

def grab_comments(subreddit, max = 2000):

    subr = reddit.subreddit(subreddit)
    bcomms = []

    for submission in subr.top(limit=250):
        print(submission.title)
        submission.comments.replace_more(limit=None)
        comment_queue = submission.comments[:]  # Seed with top-level
        while comment_queue:
            comment = comment_queue.pop(0)
            print(comment.body)
            bcomms.append(comment)
            comment_queue.extend(comment.replies)
            if len(bcomms) % 100 == 0:
                print(len(bcomms))
                time.sleep(1)
            if len(bcomms) == 2000:
                print("got 2000")
                return(bcomms)
    return(bcomms)

all_shit = grab_comments("bloomington", 2000)
all_shit = all_shit + grab_comments("BloomingtonModerate", 2000)

print("We got %s comments" % len(all_shit))

output_dir = '~/Dropbox/GlobalGits/reddit_fun/'
with open('%s/output/comments.csv' % (output_dir), 'w') as f:
    f.write("id, created_utc, subreddit, author, body, ups, downs\n")
    for shit in all_shit:
        f.write("%s,%s,%s,%s,,%s,%s\n" % (shit.id, shit.created_utc, shit.subreddit, 
        shit.author, shit.ups, shit.downs ))

with open('%s/output/comments.txt' % (output_dir), 'w') as f:
    for shit in all_shit:
        f.write("__label__%s %s\n" % (shit.subreddit,  normalize_text(shit.body) ))
