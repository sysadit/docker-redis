import time
import redis
from flask import Flask

app = Flask(__name__)
# 'redis' di sini adalah nama service yang didefinisikan di docker-compose.yml
# Docker DNS otomatis menerjemahkan nama service jadi IP internal container.
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"<h1>Tugas Docker Berhasil!</h1><p>Counter ini disimpan di Redis: {count} kali dilihat.</p>"
