from flask import Flask, render_template, request, flash, session, redirect, jsonify, escape
from model import connect_to_db
from datetime import date, datetime
import json
import os
import pprint
import requests
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
