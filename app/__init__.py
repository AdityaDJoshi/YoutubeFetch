from flask import Flask, jsonify
from celery import Celery
import celeryconfig
from flask_sqlalchemy import SQLAlchemy

from models import db, vidDB
app = Flask(__name__)
app.config.from_object('config')
# db = SQLAlchemy(app)


# class vidDB(db.Model):
#     id = db.Column('vid_id', db.String(15), primary_key=True)
#     vidTitle = db.Column(db.String(100))
#     description = db.Column(db.String(500))
#     publishedDatetime = db.Column(db.DateTime(200))
#     thumbnailURL = db.Column(db.String(10))
#     videoURL = db.Column(db.String(40))

#     def __init__(self, id, vidTitle, description, publishedDatetime, thumbnailURL, videoURL):
#         self.id = id
#         self.vidTitle = vidTitle
#         self.description = description
#         self.publishedDatetime = publishedDatetime
#         self.thumbnailURL = thumbnailURL
#         self.videoURL = videoURL


def make_celery(app):
    # create context tasks in celery
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )
    celery.conf.update(app.config)
    celery.config_from_object(celeryconfig)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


celery = make_celery(app)


@app.route('/')
def view():
    return "Hello, Flask is up and running!"


@app.route('/querydb')
def qdb():
    page = db.paginate(db.select(vidDB).order_by(vidDB.id))
    results = {
        "results": [{"title": v.vidTitle, "Video Link": v.videoURL} for v in page.items],
        "pagination": {
            "count": page.total,
        },
    }
    return jsonify(results)

    # return render_template("user/list.html", page=page)


if __name__ == "__main__":
    app.run()
