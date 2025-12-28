import sys
import logging
import argparse
import json
from datetime import datetime
from flask import Flask, request, Request

# No warnings for werkzeug
logging.getLogger("werkzeug").setLevel(logging.ERROR)

app = Flask(__name__)
args = None

# Turn off CSRF token
app.config["WTF_CSRF_ENABLED"] = False

def get_headers(request: Request) -> str:
    """
    Returns the headers of the request (including method) as
    string representation.
    """
    headers = ""
    for k, v in request.headers:
        headers += f"{k}: {v}\r\n"
    headers += "\r\n"
    return headers


@app.route("/")
def index():
    """
    Echo request as HTTP 1.1 text representation, including header
    and body.
    """
    top = "{} {} HTTP/1.1\r\n".format(request.method, request.path)
    headers = get_headers(request)
    body = request.get_data()
    data = (top + headers + body.decode("utf-8"))

    if args.stdout:
        print(" *\n * request at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print(data)

    return data.replace("\r\n", "<br>")


@app.route("/json")
def json_output():
    """
    Echo request headers and body in JSON format.
    """
    data = {
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
        "body": request.get_data().decode("utf-8"),
    }
    if args.stdout:
        print(" *\n * request at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        print(json.dumps(data, indent=4))
    return data


def main():
    global args

    parser = argparse.ArgumentParser(description="light server for echoing back HTTP requests")
    parser.add_argument("--stdout", action="store_true", help="print HTTP request data to stdout")
    args = parser.parse_args()

    print(
        " * echoserver is for development and debugging purposes only,", file=sys.stderr
    )
    print(
        " * don't expect this to be a production grade solution.\n *", file=sys.stderr
    )
    app.run(debug=False)


if __name__ == "__main__":
    main()
