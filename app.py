from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/visa_usa')
def visa_usa():
    return render_template('visa_usa.html')


if __name__ == "__main__":
    app.run(debug=True)
