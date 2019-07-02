# Periodic_Sentiment_Analysis
This is a script that extracts most recent data using Twitter API from Twitter. It inserts the data like (tweetid, tweet, datetime, etc.) to an excel sheet along with an extra column called Sentiment that gives the sentiment score of that tweet's text using VADER analysis from nltk corpus.

(ProTip: Use virtualenv or venv and perform following action in your environment.)

#Step 1:
<br>pip install -r requirements.txt
<br>(Resolve any errors that you get by installing corresponding libraries in the OS.)

#Step 2:
<br>Edit automated_sentiment.py -- Go to API KEY credentials part and paste your details.
<br>Edit your search query - currently it is "mangoes" - you can replace it with any username, text or hashtag.
<br>Edit the count of tweets to retrieve. Currently it is 50. (Free developer account allows 350 tweets extraction per day.)

#Step 3:
<br>python automated_sentiment.py
<br>You will see a pie chart of positive negative and neutral tweets of all the data in the excel sheet created.
![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
<br>Next time you run Step 3, it will automatically append data to the same excel sheet.
<br>
<br>If you run it every hour (if API allows) or every 6 hours - you will get a consolidated list of all tweets about your search query made during the entire day.
