import imports as imports
import auth as auth
import headers as headers
import create_url as create_url
import connect as connect
import custom_2

# #Inputs for the request
#
# keyword = "#floodwatch #flood"
# start_time = "2020-03-01T00:00:00.000Z"
# end_time = "2022-03-31T00:00:00.000Z"
# max_results = 100

# Inputs for tweets
bearer_token = auth.auth()
headers = headers.create_headers(bearer_token)
keyword = "(#flood OR #floodalert) has:geo point_radius:[ -4.0613741 53.181157 25mi]"
start_list = ['2011-01-01T00:00:00.000Z']
              # '2020-01-01T00:00:00.000Z',
              # '2021-01-01T00:00:00.000Z']

end_list = ['2022-01-01T00:00:00.000Z']
            # '2020-12-31T00:00:00.000Z',
            # '2021-12-31T00:00:00.000Z']
max_results = 500

# Total number of tweets we collected from the loop
total_tweets = 0

# Create file
csvFile = open("data.csv", "a", newline="", encoding='utf-8')
csvWriter = imports.csv.writer(csvFile)

# Create headers for the data you want to save, in this example, we only want save these columns in our dataset
csvWriter.writerow(
    ['author id', 'created_at', 'geo', 'id', 'lang', 'like_count', 'quote_count', 'reply_count', 'retweet_count',
     'source', 'tweet', 'long', 'lat'])
csvFile.close()

for i in range(0, len(start_list)):

    # Inputs
    count = 0  # Counting tweets per time period
    max_count = 100000  # Max tweets per time period
    flag = True
    next_token = None

    # Check if flag is true
    while flag:
        print('here')
        # Check if max_count reached
        if count >= max_count:
            break
        print("-------------------")
        print("Token: ", next_token)
        url = create_url.create_url(keyword, start_list[i], end_list[i], max_results)
        json_response = connect.connect_to_endpoint(url[0], headers, url[1], next_token)
        result_count = json_response['meta']['result_count']

        if 'next_token' in json_response['meta']:
            # Save the token to use for next call
            next_token = json_response['meta']['next_token']
            print("Next Token: ", next_token)
            if result_count is not None and result_count > 0 and next_token is not None:
                print("Start Date: ", start_list[i])
                custom_2.append_to_csv(json_response, "data.csv")
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                imports.time.sleep(5)
                # If no next token exists
        else:
            if result_count is not None and result_count > 0:
                print("-------------------")
                print("Start Date: ", start_list[i])
                custom_2.append_to_csv(json_response, "data.csv")
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                imports.time.sleep(5)

            # Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        imports.time.sleep(5)

        with open('data.json', 'w') as f:
            imports.json.dump(json_response, f)

print("Total number of results: ", total_tweets)