from flask import Flask
from os import environ
import requests

LB_URL = environ.get('LB_URL')
app = Flask(__name__)

@app.route('/ocr')
def ocr():
    ocr_res = requests.get(LB_URL)
    return ocr_res.json()
    

@app.route('/receipt')
def receipt():
    ocr_res = requests.get(f"{LB_URL}/ocr")
    receipt_res = requests.get(f"{LB_URL}/receipt")
    return receipt_res.json()


@app.route('/health')
def health():
    return {"status": "alive"}



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)