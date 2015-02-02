from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'How deploy image in multiple server by using fig! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
