from flask import Flask, render_template, url_for, redirect, request
from data import services as s_list
from forms import LoginForm, RegisterForm, MessageForm
from mail import send

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


@app.route('/services/')
def services():
    return render_template("services.html", service_list=s_list)


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = MessageForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.name.data, form.email.data, form.message.data)

        return redirect(url_for("home"))
    return render_template('contact.html', form=form)


@app.route('/order/')
def order():
    return render_template("order.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.username.data)
        print(form.password.data)

        return redirect(url_for('home'))

    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, host="192.168.8.104")