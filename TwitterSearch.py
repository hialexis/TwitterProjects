import twython
from twython import Twython
import json
import pandas as pd
import os

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

