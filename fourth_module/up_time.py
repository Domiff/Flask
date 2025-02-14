import sys
import subprocess

from flask import Flask, request


app = Flask(__name__)


@app.route("/uptime")
def up_time():
    result = subprocess.run(["uptime", "-p"],
                            capture_output=True, text=True).stdout

    return f"Current uptime is {result}"


if __name__ == '__main__':
    app.run()
