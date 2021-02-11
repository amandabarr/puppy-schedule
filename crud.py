from model import db, Event
from datetime import datetime


def add_event(event_type, event_time=None, event_location=None, event_comment=None):
    event_type = event_type.lower().replace(" ", "_")
    if event_time == None:
        event_time = datetime.utcnow()
    else:
        event_time = datetime.utcfromtimestamp(int(event_time))

    event = Event(event_time=event_time, event_type=event_type,
                  event_location=event_location, event_comment=event_comment)

    db.session.add(event)
    db.session.commit()

    return event


def get_all_events():
    return db.session.query(Event).all()


def import_old_events():
    # open the CSV file

    # read each lines

    # loop through each line

        # split by commas to separate into pieces

        # assign each part to proper event property

        # call add event with that info

    pass


if __name__ == '__main__':
    from server import app
    from model import connect_to_db
    connect_to_db(app)
    add_event("poop")
    print(get_all_events())
