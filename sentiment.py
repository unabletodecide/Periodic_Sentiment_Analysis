def analyze(message):	
	from nltk.sentiment.vader import SentimentIntensityAnalyzer
	sid = SentimentIntensityAnalyzer()
	msg_txt = message
	scores = sid.polarity_scores(msg_txt)
	return scores