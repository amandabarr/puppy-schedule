from flask import Flask, render_template, request, flash, session, redirect, jsonify, escape
from model import connect_to_db
from datetime import date, datetime
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
    event_type = "pee"
    events = [event for event in crud.get_all_events(
    ) if event.event_type == event_type]
    return render_template("base.html", event_type=event_type, events=events)


@app.route("/api/test")
def test():
    return "test"


@app.route("/api/events")
def get_events():
    all_events = crud.get_all_events()
    return jsonify([event.to_dict() for event in all_events])


@app.route("/api/events/add", methods=["POST"])
def add_event():
    event_type = request.form["eventType"]
    event_time = request.form.get("eventTime", None)
    event = crud.add_event(event_type, event_time)
    return jsonify(event.to_dict())


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
