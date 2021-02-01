
import requests
import sys

base_url = 'https://www.reddit.com/'
import os

reddit_username = 'BobDope'
reddit_password = os.environ['reddit_pass']

app_id = 'V5ZGRnUFVkQGiw'
app_secret = os.environ['reddit_secret']

data = {'grant_type': 'password', 'username': reddit_username, 'password': reddit_password}

client_auth = requests.auth.HTTPBasicAuth(app_id, app_secret)

response = requests.post(base_url + 'api/v1/access_token',
                  data=data,
                  headers={'user-agent': 'reddit_analytics by BobDope 0.0.1'},
                  auth=client_auth)

values = response.json()

api_url = 'https://oauth.reddit.com'

token = 'bearer {}'.format(values['access_token'])

headers = {'Authorization': token, 'User-Agent': 'reddit_analytics by BobDope 0.0.1'}


payload = {'q': 'puppies', 'limit': 10}
response = requests.get(api_url + '/subreddits/search', headers=headers, params=payload)
js = response.json()

print(js.keys())

print(response.text)

sr = []
for i in range(js['data']['dist']):
    sr.append(js['data']['children'][i]['data']['display_name'])

print(sr)


payload = {'t': 'all'}
r = requests.get(api_url + '/r/puppies/top', headers=headers, params=payload)
print(r.text)

payload = {'t': 'all', 'limit': 5}
imghtml = ''
for s in sr:
    imghtml += '<h3 style="clear:both">{}</h3><div>'.format(s)
    r = requests.get(api_url + '/r/{}/top'.format(s), headers=headers, params=payload)
    js = r.json()
    for i in range(js['data']['dist']):
        if js['data']['children'][i]['data']['thumbnail'] == '':
            continue
        imghtml += '<span style="float:left"><a href="{}"><img src="{}" title="{}" target="_blank" \></a></span>'.format(
            js['data']['children'][i]['data']['url'],
            js['data']['children'][i]['data']['thumbnail'],
            js['data']['children'][i]['data']['title'],
        )
    imghtml += '</div>'

posty = js['data']['children'][0]

id36 = posty['data']['id']
js['data']['children'][0]

js['data']['children'][0]['data']['id']
'ktfnx7'

#sort	
#one of (confidence, top, new, controversial, old, random, qa, live)
payload = { 'limit': 100}
sr = '/r/puppies' # for example

#url = api_url + '/r/' + sr + '/comments/' + id
#response = requests.get(url ,  headers=headers, params=payload)
#response.text

response = requests.get(api_url + '/' + sr + '/comments/' + id , headers=headers, params=payload)
js = response.json()

with open('../pups.html', 'w') as f:
    f.write(imghtml)



def fetch_latest_posts(headers, subreddit, how_many):
    pass

# how to crawl and just get all comments, don't worry about threading (yet)

# how to pre-process the text (keep the raw though)

def preprocess_text(text):
    pass

# get comments.
