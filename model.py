from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


def connect_to_db(flask_app, db_uri="postgresql:///puppy_schedule", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the database!")


class Event(db.Model):
    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_time = db.Column(db.DateTime)
    event_type = db.Column(db.String)
    event_location = db.Column(db.String)
    event_comment = db.Column(db.String)

    def to_dict(self):
        return {
            "eventId": self.event_id,
            "eventTime": self.event_time,
            "eventType": self.event_type,
            "eventLocation": self.event_location,
            "eventComment": self.event_comment
        }

    def __repr__(self):
        return f"Event event_id = {self.event_id}, event_type={self.event_type}, event_time = {self.event_time}"


def setup_tables():
    db.create_all()

    test_event = Event(event_time=(datetime.utcnow()),
                       event_type="pee", event_location=None, event_comment=None)
    db.session.add(test_event)

    test_event2 = Event(event_time=(datetime.utcnow()),
                        event_type="pee", event_location="outside", event_comment="Went on the Fresh Patch")
    db.session.add(test_event2)

    db.session.commit()


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    setup_tables()
