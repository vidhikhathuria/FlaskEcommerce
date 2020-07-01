from flask import render_template, session, request, redirect, flash, url_for
from shop.forms import RegistrationForm, LoginForm
from shop.models import User
from shop import app, db, bcrypt

@app.route('/')
def home():
    return "home page of shop"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email = form.email.data,
                    password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration Page")