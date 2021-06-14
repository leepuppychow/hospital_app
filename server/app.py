import os
from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/api/v1/ping', methods=["GET  "])
def ping():
    return "Things are ok!"