import os
import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# The youtube search function provided by google oauthlib
# requires oauth credentials json downloaded from google developers console
# rename the file as YOUR_CLIENT_SECRET_FILE


def fun1():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="cricket"
    )
    response = request.execute()

    print(response)
    f = open("response.json", "w")
    f.write(str(response))
    f.close()

# searching using python requests

# create a file named 'api-key.json' in current directory
# { "key": "key here" }


def fun2(numOfResults=25, searchTerm="ios"):

    key = json.load(open('api-key.json'))['key']
    # numOfResults = "25"
    # searchTerm = "ios"
    publishedAfter = "2023-01-01T06:51:11Z"
    url = "https://www.googleapis.com/youtube/v3/search?key="+key + \
        "&type=video&part=snippet&maxResults=" + \
        str(numOfResults)+"&q="+searchTerm+"&publishedAfter="+publishedAfter
    response = requests.get(url)
    print(response.text)
    print("############")
    print(response.json())

    with open("response.json", "w") as outfile:
        json.dump(response.json(), outfile)
    return response.json()
