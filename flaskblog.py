from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '6086dbce01e4a17787cf07135787e954'

posts = [
    {
        'author': 'David Hammaker',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 27, 2018'
    },
    {
        'author': 'Aaron Key',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 28, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
