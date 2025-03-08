from flask import Flask, render_template, g
from database.database import get_db
from database.dest_images import dest_images
from datetime import datetime as dt


app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'slite_db'):
        g.sqlite_db.close()

@app.route('/')
def main():
    today = dt.now()
    today_f = today.strftime("%Y-%m-%d")
    db = get_db()
    cur = db.execute(f'SELECT * FROM cheapest_flights WHERE time_now = "{today_f}"')
    cheap_flights = cur.fetchall()
    return render_template('main.html', cheap_flights=cheap_flights, dest_images=dest_images)

@app.route('/visa_usa')
def visa_usa():
    return render_template('visa_usa.html')


if __name__ == "__main__":
    app.run(debug=True)
