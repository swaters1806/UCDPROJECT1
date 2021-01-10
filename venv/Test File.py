print("helloworld")

list=[1,2,3]

print(list[0:2])

import pandas as pd
import requests
import io

# Username of your GitHub account

username = 'swaters1806'

# Personal Access Token (PAO) from your GitHub account

token = '9c649f6862c546131e079af5693719a3d70fd270'

# Creates a re-usable session object with your creds in-built

github_session = requests.Session()
github_session.auth = (username, token)

# Downloading the csv file from your GitHub

url = "https://raw.githubusercontent.com/dwiknrd/medium-code/master/netflix-eda/netflix_titles.csv"  # Make sure the url is the raw version of the file on GitHub
download = github_session.get(url).content

# Reading the downloaded content and making it a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe to make sure everything is good

print(df.head())
