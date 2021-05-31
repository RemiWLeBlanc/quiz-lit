""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/remi')
def map():
    return render_template('remi.html')


if __name__ == '__main__':
    app.run(debug=True)

