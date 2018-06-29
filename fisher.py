from flask import Flask,make_response
import json

app = Flask(__name__)
app.config.from_object('config')


@app.route("/hello/")
def hello():
    return "Hello World"


@app.route("/plain/")
def t_plain():
    response = make_response("<html></html>", 200)
    headers = {
        'content-type': 'text/plain'
    }
    response.headers = headers
    return response


@app.route("/json/")
def t_json():
    headers = {
        'content-type': 'text/json'
    }
    response = make_response(json.dumps(headers), 200)
    response.headers = headers
    return response


@app.route("/simple/")
def t_simple():
    headers = {
        'content-type': 'text/json'
    }
    return json.dumps(headers), 200, headers


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=app.config['DEBUG'])
