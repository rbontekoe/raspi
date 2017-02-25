from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import myhat as mh
from flask_nav import Nav
from flask_nav.elements import Navbar, View

app = Flask(__name__)
bootstrap = Bootstrap(app)

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
	hum = mh.name()
	return render_template('index.html', test=hum)

@app.route('/cons')
def cons():
	pres = mh.name()
	temp = mh.temp()
	hum = mh.hum()
	all = {"pres": pres, "temp": temp, "hum": hum}
	return render_template('cons.html', test=all)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
