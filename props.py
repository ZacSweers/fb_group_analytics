__author__ = 'hsweers'

# Access token can be obtained by doing the following:
# - Log into facebook
# - Go to this url: https://developers.facebook.com/tools/explorer
token = "api_token"

# Only necessary if you want to get an extended access token
# You'll have to make a facebook app and generate a token with it
# You'll also need to get the following two values from it
app_id = "id_goes_here"
secret_key = "key_goes_here"

# Unique ID of the group to search.
group_id = "group_id"

# Start date, in unix time (our group was made 2/13/12)
# You can use this to convert: http://goo.gl/4QMFbW
start_date = 1282694400

# Return the top ____ most liked ____
num_of_items = 100