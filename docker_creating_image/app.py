import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(host='redisdb', port=6379, db=0)


@app.route('/home')
def home():
    return f"<h1>Welcome {r.incr('hits')} </h1>"

