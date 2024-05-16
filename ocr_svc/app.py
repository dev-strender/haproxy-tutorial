from flask import Flask
import time
from os import environ

service_name = environ.get('SVC_NAME')
duration = environ.get('DURATION')
app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(int(duration))
    return {"ISVC_NAME": service_name}

@app.route('/health')
def health():
    return {"status": "alive"}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10080)