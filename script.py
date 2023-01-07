from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
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


@app.route('/')
def add_task():
    temp = vidDB('yQ8jlAdCZoY', 'Android vs Apple iOS #shorts', "Apple #iphome #apple #techbar #india #android.", datetime.fromisoformat(
        '2023-01-05T15:40:13Z'[:-1] + '+00:00'), "https://i.ytimg.com/vi/yQ8jlAdCZPY/default.jpg", "https://youtube.com")
    db.session.add(temp)
    db.session.commit()
    return jsonify({'status': 'ok'})
