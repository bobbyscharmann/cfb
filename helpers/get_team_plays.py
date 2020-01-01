"""
Python 3.6.8 script for accessing the www.collegefootballdata.com API
for getting team play as a Pandas dataframe object.

Documentation of JSON GET request may be found here:
https://api.collegefootballdata.com/api/docs/?url=/api-docs.json

This script will return the data as a Pandas dataframe object where each row
is a play record and the column is a JSON property such as 'down' or
'yards_gained'

Permission to use for any purpose granted - would love to hear its purpose.

January 2020, Bob Scharmann, Jr.
"""
import json
import pandas as pd
import requests

def get_team_plays(url="https://api.collegefootballdata.com/plays",
                   year=2019,
                   team="Florida State"):
    """
    Function to get team data from www.collegefootballdata.com API
    """
    params = {"team": team, "year": year}
    my_response = requests.get(url, params=params)
    data = pd.DataFrame()
    # For successful API call, response code will be 200 (OK)
    if my_response.ok:

        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to
        # fetch the binary content. Loads (Load String) takes a Json file and
        # converts into python data structure (dict or list, depending on JSON)
        j_data = json.loads(my_response.content)

        j_data_normalized = pd.io.json.json_normalize(j_data)
        data = pd.DataFrame.from_records(j_data_normalized)
    else:
        # If response code is not ok (200), print the resulting http error code
        # with description
        my_response.raise_for_status()

    return data
