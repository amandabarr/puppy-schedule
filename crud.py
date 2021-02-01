from model import db, Event
from datetime import datetime


def add_event(event_type, event_time=None):
    event_type = event_type.lower().replace(" ", "_")
    if event_time == None:
        event_time = datetime.utcnow()
    else:
        event_time = datetime.utcfromtimestamp(int(event_time))

    event = Event(event_time=event_time, event_type=event_type)

    db.session.add(event)
    db.session.commit()

    return event


def get_all_events():
    return db.session.query(Event).all()


if __name__ == '__main__':
    from server import app
    from model import connect_to_db
    connect_to_db(app)
    add_event("poop")
    print(get_all_events())
