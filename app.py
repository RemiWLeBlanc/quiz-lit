""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/remi')
def map():
    return render_template('remi.html')

@app.route('/remi', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        a = request.form['answer']
        s = request.form['solution']
        # return render_template('remi.html', answer=a, solution=s)
        return render_template('remi.html', equality = check_equality(s,a), checked=True, ans=a, sol=s)

    return render_template('remi.html', checked=False)

def check_equality(sol, ans):
    if sol.lower() == ans.lower():
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True)

