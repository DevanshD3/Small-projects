# We need a python scripts that do the following for Twitter.
# 1. Take names of profiles from a metadata table
# 2. Get all the posts from all those profiles / groups from last 1 week
# 3. Keep the posts, pictures in seperate tables
import tweepy as tp
from datetime import datetime
import xlsxwriter
import xlrd 

def get_data(profile_name):
    tweet_element = []
    tweet_list = []
    dt_string = '2020-6-02 23:59:59'
    dt_object = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
    tweets = api.user_timeline(id = profile_name, count=10000) 
    for tweet in tweets:
        if datetime.timestamp(tweet.created_at) >= datetime.timestamp(dt_object):
            tweet_element.append(tweet.text) 
            tweet_element.append(tweet.retweet_count) 
            tweet_element.append(tweet.favorite_count)
            tweet_list.append(tweet_element)
            tweet_element = []
    print(tweet_list)
    return tweet_list

def write_data(tweet_list, profile_name):
    with xlsxwriter.Workbook(f'test {profile_name}.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        for row_num, data in enumerate(tweet_list):
            worksheet.write_row(row_num, 0, data)
    tweet_list = []
    print('Done!')

auth = tp.OAuthHandler('Nqio70OhqAWkb4RTuJL4qh66A','bv7sLqqd1EJZp12aE59SWsgV6TJrMdighq74wpZXF9YJ1bYDdF')
auth.set_access_token('1234242643040718848-7LxppWqEGHyP7nGtH8iMDkqajnIl5v','kHgFEujjKabTrXLdOUyApTGTG0wGr1IFZTG8m0KvALE55')
api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

loc = "metadata.xlsx"
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
for char in sheet.get_rows():
    profile_name = (str(char[0])[5:-1]).lower()
    write_data(get_data(profile_name[1:]), profile_name[1:])

