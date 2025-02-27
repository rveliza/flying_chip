from flask import Flask, render_template, g
from database.database import get_db

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'slite_db'):
        g.sqlite_db.close()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/visa_usa')
def visa_usa():
    return render_template('visa_usa.html')


if __name__ == "__main__":
    app.run(debug=True)
