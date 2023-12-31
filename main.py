from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/community/')
def community():
    return render_template('community.html')


@app.route('/list/')
def list():
    return render_template('list.html')



if __name__ == '__main__':
    app.run(debug=True)

