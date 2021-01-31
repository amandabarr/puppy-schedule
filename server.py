from flask import Flask, render_template, request, flash, session, redirect, jsonify, escape
from model import connect_to_db
from datetime import date, datetime
import crud
import json
import os
import pprint


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def root():
    return """
    <html>
    <body>
    <h1>I am the landing page</h1>
    </body>
    </html>
    """


@app.route("/api/events")
def get_events():
    all_events = crud.get_all_events()
    print(all_events)
    return jsonify([event.to_dict() for event in all_events])


@app.route("/api/events/add", methods=["POST"])
def add_event():
    event_type = request.form["eventType"]
    event_time = request.form.get("eventTime", None)
    crud.add_event(event_type, event_time)
    return "foo"


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
