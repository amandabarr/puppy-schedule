from flask import Flask, render_template, request, flash, session, redirect, jsonify, escape
from model import connect_to_db
from datetime import date, datetime
from dotenv import load_dotenv
import crud
import json
import os
import pprint
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def root():
    events = [event for event in crud.get_all_events()]
    return render_template("base.html", events=events)


@app.route("/api/test")
def test():
    return "test"


@app.route("/api/test2")
def test2():
    return "test2"


@app.route("/api/events")
def get_events():
    all_events = crud.get_all_events()
    return jsonify([event.to_dict() for event in all_events])


@app.route("/api/events/add", methods=["POST"])
def add_event():
    event_type = request.form["eventType"]
    event_time = request.form.get("eventTime", None)
    event_location = request.form.get("eventLocation", None)
    event_comment = request.form.get("eventComment", None)
    event = crud.add_event(event_type, event_time,
                           event_location, event_comment)
    return jsonify(event.to_dict())


if __name__ == '__main__':
    load_dotenv()
    connect_to_db(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
