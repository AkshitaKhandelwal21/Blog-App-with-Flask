from Application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from Application.forms.userForms import *
from flask_login import logout_user, login_user, current_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    print("inside register")
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form validated")
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print("Password hashed")
        user = User(username=form.username.data, email=form.email.data, phone=form.phone.data, password=hashed_pw)
        print("user data")
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user)
        return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
def account():
    form = UpdateForm()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    if form.validate():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        return redirect(url_for('account'))
    
    return render_template("account.html", form=form)
