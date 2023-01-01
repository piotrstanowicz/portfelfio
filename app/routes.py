from app import app


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/user/<username>")
def show_user(username):
    return f"Hello, {username}!"
