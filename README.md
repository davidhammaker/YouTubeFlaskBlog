# Flask Blog

This project follows a series of YouTube tutorials by Corey Schafer. His tutorials may be found [here](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).

## Usage

_Note: This project is not necessarily intended to be used for any purpose other than practice. However, if you would like to experiment with the app and/or get a taste of what Python/Flask can accomplish, follow the steps below to use the app._

### Dependencies

You will need access to a shell terminal (I am using [GitBash](https://git-scm.com/downloads) for Windows). You will also need to install the latest version of [Python 3](https://www.python.org/downloads/), which must be Python 3.6 or later. This app is incompatible with Python 2 and Python 3.5 or older.

Clone this repository and create a Python [virtual environment](https://docs.python.org/3/library/venv.html). Inside your shell terminal, activate the virtual environment and install Flask, Flask-WTF (for forms), Flask-SQLAlchemy (for databases), Flask-Bcrypt (for hashing passwords), Flask-Login (for login functionality), Pillow (for image modification), and Flask-Mail (for sending emails):

```
$ pip install flask
$ pip install flask-wtf
$ pip install flask-sqlalchemy
$ pip install flask-bcrypt
$ pip install flask-login
$ pip install Pillow
$ pip install flask-mail
```

You will be required to set up environment variables for the email address from which you would like your app to send emails (such as password-reset emails). The app is configured to use environment variables called `EMAIL_USER` for the email address and `EMAIL_PASS` for the password. If you would like to learn how to set up environment variables, Corey Schafer has brief videos that explain the process for [Windows](https://www.youtube.com/watch?v=IolxqkL7cD8) and [Mac and Linux](https://www.youtube.com/watch?v=5iWhQWVXosU). (Note: I was only successful in getting the email feature to work when I followed the "Mac and Linux" tutorial using GitBash for Windows.)

If you are using Gmail, you may need to turn on the "_Allow less secure apps_" option. (For security reasons, this is not recommended. I have created a new Google account to use instead of my regular Google account.) To do this, log into the Google account you are using for the app and navigate to "_Account_" (it should be located [here](https://myaccount.google.com)). Under "_Sign-in & security_", click "_Apps with account access_". There, you should see _"Allow less secure apps: OFF_" (or "_ON_", if you previously turned the option on). Click the switch beside the option to turn it **ON**. Again, this is generally not recommended due to security risks.

### Running the App

When you have acquired/installed all the dependencies, you can run the app from the shell terminal. Once again, ensure that your virtual environment is active, then run the following:

`$ python run.py`

If you see no errors, open an internet browser and navigate to `localhost:5000`. The app should be running at that address.
