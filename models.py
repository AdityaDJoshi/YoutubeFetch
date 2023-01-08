from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
