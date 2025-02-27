from flask import Flask, render_template, g
from database.database import get_db

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'slite_db'):
        g.sqlite_db.close()

@app.route('/')
def main():
    db = get_db()
    cur = db.execute('SELECT * FROM cheapest_flights')
    cheap_flights = cur.fetchall()
    return render_template('main2.html', cheap_flights=cheap_flights)

@app.route('/visa_usa')
def visa_usa():
    return render_template('visa_usa.html')


if __name__ == "__main__":
    app.run(debug=True)
