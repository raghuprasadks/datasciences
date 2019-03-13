import tweepy 

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure. 

consumer_key = 'IRHoeizLxZNGNxowQoHRNH7d1'
consumer_secret = 'ZDaOCtrraTQ8C0SZYs7E7SPaHVH1F6mT2cB9JXx5rsqNnctkrs'
access_key = '2395385144-EYdpnWy31HnZPdOK1nDpYwBmp9vZ7rbAzZHkrQv'
access_secret = 'PspWYdRp0X7MiO6Jg8Imsmmlsetlbf97CuRzAFFdrp693'
'''
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
'''
# Function to extract tweets 
def get_tweets(username): 
		
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# 200 tweets to be extracted 
		number_of_tweets=200
		tweets = api.user_timeline(screen_name=username) 

		# Empty Array 
		tmp=[] 

		# create array of tweet information: username, 
		# tweet id, date/time, text 
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
		for j in tweets_for_csv: 

			# Appending tweets to the empty array tmp 
			tmp.append(j) 

		# Printing the tweets 
		print(tmp) 


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("raghukonandur") 
# -*- coding: utf-8 -*-

