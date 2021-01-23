from model import db, Event
from datetime import datetime


def add_event(event_type, event_time=datetime.now()):
    event = Event(event_time=event_time, event_type=event_type)

    db.session.add(event)
    db.session.commit()

    return event


if __name__ == '__main__':
    from server import app
