from flask import Flask

app = Flask(__name__)

from config.extentions import db
from models import *
from api.routers import *



