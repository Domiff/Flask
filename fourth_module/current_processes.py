import subprocess

from flask import Flask, request


app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def current_processes():
    args = request.args.getlist("arg")
    process = subprocess.run(["ps", args[0], args[1], args[2]], capture_output=True, text=True).stdout

    return f"Results utility <pre>{process}</pre>"


if __name__ == '__main__':
    app.run()
    print(current_processes())