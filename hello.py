from flask import Flask
from flask import json
import datetime

app = Flask(__name__)

uptime = f"up since {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
version="0.0.1"

import socket


@app.route("/")
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return "Hello Guys! V2", getNetworkIp()

@app.route("/healthz")
def health():
    ret={
        "status": "OK",
        "version": version,
        "uptime": uptime
    }
    return json.dumps(ret)

if __name__ == "__main__":
    app.run("0.0.0.0",port=8080)
