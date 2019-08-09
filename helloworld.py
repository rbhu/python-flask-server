from flask import Flask, Response
import time

app = Flask(__name__)
# app.register_blueprint(sse, url_prefix='/streams')
@app.route('/')
def say_hello_world():
    return "hello world"


@app.route('/whoami')
def who_am_i():
    return Response("Reuben Bryn Hughes", mimetype="text")


@app.route('/whatsthetime')
def what_time_is_it():
    def eventStream():
        while True:
            yield get_time() + '\n'
    return Response(eventStream(), mimetype="text/event-stream")


def get_time():
    time.sleep(1)
    s = time.ctime()
    return s


def bootapp():
    app.run(port=8080, debug=True)






