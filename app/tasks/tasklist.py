# # from models import vidDB
# from models import vidDB
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import celery
from datetime import datetime
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vidDB.sqlite3'
db = SQLAlchemy(app)


class vidDB(db.Model):
    id = db.Column('vid_id', db.String(15), primary_key=True)
    vidTitle = db.Column(db.String(100))
    description = db.Column(db.String(500))
    publishedDatetime = db.Column(db.DateTime(200))
    thumbnailURL = db.Column(db.String(10))
    videoURL = db.Column(db.String(40))

    def __init__(self, id, vidTitle, description, publishedDatetime, thumbnailURL, videoURL):
        self.id = id
        self.vidTitle = vidTitle
        self.description = description
        self.publishedDatetime = publishedDatetime
        self.thumbnailURL = thumbnailURL
        self.videoURL = videoURL


@celery.task()
def print_hello():
    logger = print_hello.get_logger()
    logger.info("Hello")


@celery.task()
def number_writer():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    x = requests.get(
        "http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5")
    print(x.text)

    f = open("demofile3.txt", "a")
    f.write(x.text+str(current_time)+'\n')
    f.close()
    logger = number_writer.get_logger()
    logger.info(x.text+str(current_time)+'\n')


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


@celery.task()
def videofetch():
    f = open('ios response.json')
    j = json.load(f)
    f.close()
    # j = fun2()
    # print(j['items'])
    for i in j['items']:
        print("videoURL:", 'https://youtu.be/'+i['id']['videoId'])
        print("thumbnailURL", i['snippet']['thumbnails']['default']['url'])
        print('publishedDatetime', i['snippet']['publishedAt'])
        print('Description', i['snippet']['description'])
        print('vidTitle', i['snippet']['title'])
        print("id:", i['id']['videoId'])

        temp = vidDB(i['id']['videoId'], i['snippet']
                     ['title'], i['snippet']['description'], datetime.fromisoformat(i['snippet']['publishedAt'][:-1] + '+00:00'), i['snippet']['thumbnails']['default']['url'], 'https://youtu.be/'+i['id']['videoId'])
    #     db.session.add(temp)
    # db.session.commit()


videofetch()
