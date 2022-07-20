# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata

def append_to_csv(json_response, fileName):
    # A counter variable
    counter = 0

    # Open OR create the target CSV file
    csvFile = open(fileName, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    # Loop through each tweet
    for tweet in json_response['data']:

        # We will create a variable for each since some of the keys might not exist for some tweets
        # So we will account for that

        # 1. Author ID
        author_id = tweet['author_id']

        # 2. Time created
        created_at = dateutil.parser.parse(tweet['created_at'])

        # 3. Geolocation
        if ('geo' in tweet):
            geo = tweet['geo']['place_id']
        else:
            geo = " "

        # 3. Geolocation
        # is there a geo key in the tweet data?
        if ('geo' in tweet):
            # geo = tweet['geo']['place_id']
            geo = 'geo ref available'
        else:
            geo = " "

        # # 3. Geolocation, coordinates
        # needs extra because these coord keys do not exists in all tweets.
        long = ''
        lat = ''
        # is there a geo->coorrdinates key in the tweet data?
        try:
            x = tweet['geo']['coordinates']
        except:
            x = False
        if x:
            long = tweet['geo']['coordinates']['coordinates'][0]
            lat = tweet['geo']['coordinates']['coordinates'][1]

        # if there is not, look in the additional includes data for a places key
        else:
            for x in json_response['includes']['places']:
            #  is there a geo key in the tweet data? there should be due to has:geo above, but exceptions seen.
                try:
                    y = tweet['geo']
                except:
                    y = False
                try:
                    z = x['id']
                except:
                    z = False
                # if there is, and the attached places id can be matched to the id in the includes info
                # then look further into the nested dict for the bounding box long and lat. find the center point
                #if y and (x['geo']['id']) == (tweet['geo']['place_id']):

                if y and z == (tweet['geo']['place_id']):
                    long = ((x['geo']['bbox'][0] + x['geo']['bbox'][2]) / 2)
                    lat = ((x['geo']['bbox'][1] + x['geo']['bbox'][3]) / 2)

        # 4. Tweet ID
        tweet_id = tweet['id']

        # 5. Language
        lang = tweet['lang']

        # 6. Tweet metrics
        retweet_count = tweet['public_metrics']['retweet_count']
        reply_count = tweet['public_metrics']['reply_count']
        like_count = tweet['public_metrics']['like_count']
        quote_count = tweet['public_metrics']['quote_count']

        # 7. source
        source = tweet['source']

        # 8. Tweet text
        text = tweet['text']

        # Assemble all data in a list
        res = [author_id, created_at, geo, tweet_id, lang, like_count, quote_count, reply_count, retweet_count, source,
               text, long, lat]

        # Append the result to the CSV file
        csvWriter.writerow(res)
        counter += 1

    # When done, close the CSV file
    csvFile.close()

    # Print the number of tweets for this iteration
    print("# of Tweets added from this response: ", counter)