from flask import Flask, render_template, url_for
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
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
