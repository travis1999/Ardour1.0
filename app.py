from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, no-store'
    return response

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon/favicon.ico'))

if __name__ == "__main__":
    app.run(debug=True)