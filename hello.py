from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/index")
def index():
    return "<p>Index Page</>"


@app.route('/login')
def login():
    return 'login'


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@app.route('/user/<name>')
def show_user_profile(name):
    # show the user profile for that user
    return f'User {escape(name)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    print(url_for('show_user_profile', name='test name'))