# reddit_fun

## Setup

Make sure you define these environmental variables:

reddit_username: your username on Reddit
reddit_pass: your password
reddit_secret: your secret for the reddit API. See TODO for more on setting this up.

### Python Virtual Enviroment

User the requirements.txt file to set this up

## Files Explained

### me_model.py

Checks predictions for training set. Generally not of great interest but we are looking at what's deemed 'relevant'.

### praw_crawler_lite.py

Grab the comments

### praw_crawler.py

More some early experimental code, you don't really need it.

### someExplore.R

R based exploration

### train_moddel.py

Actually this 'shuffles' our comments

### funtests.ipynb

A really basic Jupyter notebook.
