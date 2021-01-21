import flask, time, numpy as np

app = flask.Flask(__name__)
timeFormat = "{}/{:0>2}/{:0>2} {:0>2}:{:0>2}:{:0>2}"
nowtime = lambda : timeFormat.format(*time.localtime(time.time())[:6])
startTime = nowtime()

@app.route('/', methods=['POST', 'GET'])
def index():
    return "This server is Opened at {}.<br>And now time is {}.".format(startTime, nowtime())

def main():
    app.run(host="0.0.0.0", port=12800, debug=True)



if __name__ == '__main__':
    main()
