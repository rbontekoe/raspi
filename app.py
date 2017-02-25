from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from flask_nav import Nav
from flask_nav.elements import Navbar, View

import myname as mn

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'AppliGate',
        View('Home', 'index'),
	View('Consultancy', 'cons'),
    )

nav.init_app(app)

@app.route('/')
def index():
	name = mn.name()
	return render_template('index.html', test=name)

@app.route('/cons')
def cons():
	return render_template('cons.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
