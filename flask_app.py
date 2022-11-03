# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')


if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=8080, debug=False)