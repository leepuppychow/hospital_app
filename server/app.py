from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/ping', methods=["GET  "])
def ping():
    return "Things are ok!"