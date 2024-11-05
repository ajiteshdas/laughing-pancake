from flask import Flask, render_template, request
from models import InputForm
import praw
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    form = InputForm(request.form)
    return render_template('index.html',form=form)

@app.route("/submit", methods=['POST','GET'])
def form_submit():
    
    #app.logger.info(data)
    USERNAME = str(request.form['Username'])
    PASSWORD = str(request.form['Password'])
    CLIENT_ID = str(request.form['Client_ID'])
    CLIENT_SECRET = str(request.form['Client_Secret'])
    Query = str(request.form['Query'])
    NoOfQuery = int(request.form['NoOfQuery'])

    urls = dict(url=[],question=[])

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        password=PASSWORD,
        user_agent="testapp by u/"+USERNAME,
        username=USERNAME
    )

    subreddit = reddit.subreddit('all')
    top_subreddit = subreddit.search(Query,limit=NoOfQuery)

    for submission in top_subreddit:
        url = submission.permalink
        submission = reddit.submission(url='https://www.reddit.com'+url)
        urls['url'].append('https://www.reddit.com'+url)
        urls['question'].append(submission.selftext)

    df = pd.DataFrame(urls)
    df.to_csv('queries.csv',index=False)

    
    return 'your queries are downloaded'


if __name__ == "__main__":
    app.run(debug=True)