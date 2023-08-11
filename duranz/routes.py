from flask import render_template, redirect, url_for, flash
from duranz.forms import ProjectRequestForm
from duranz import app
from duranz.send_mail import send_it


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/query_form', methods=['POST'])
def query_form():
    form = ProjectRequestForm()
    if form.validate_on_submit():
        subject = form.project.data
        body = '   =====   \n'.join([ form.name.data, form.email.data, form.project.data, form.detail.data])
        send_it(subject, body)
        flash('Your Query is Sent, Please check your mail for more info')
        return redirect(url_for('home'))
    else:
        flash("something went wrong", 'danger')
        return redirect(url_for('home'))

@app.route('/services')
def services():
    return render_template('query_form.html', title='Duranz Services')


@app.route('/about')
def about():
    form = ProjectRequestForm()
    return render_template('about.html', title='About Duranz',form=form)
