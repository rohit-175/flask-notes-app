from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('smol email lol', category='error')
        elif len(firstName) < 2:
            flash('that a name?', category='error')
        elif password1 != password2:
            flash('stick to 1 password ninja!', category='error')
        elif len(password1) < 7:
            flash('weak ahh password', category='error')
        else:
            flash('GG', category='success')
        
    return render_template("sign_up.html")