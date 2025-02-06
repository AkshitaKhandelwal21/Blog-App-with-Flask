from Application import app, db, bcrypt
from flask import render_template
from Application.forms.forms import *


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, phone=form.phone.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
    return render_template("register.html", form=form)
