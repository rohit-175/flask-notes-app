from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email not registered.', category='error')    
    
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name','').strip()
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists.', category='error')
        elif len(email) < 4:
            flash('smol email lol', category='error')
        elif len(first_name) < 2:
            flash('that a name?', category='error')
        elif password1 != password2:
            flash('stick to 1 password ninja!', category='error')
        elif len(password1) < 7:
            flash('weak ahh password', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('GG', category='success')
            return redirect(url_for('views.home'))
            
        
    return render_template("sign_up.html")