from flask import Flask, session

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/login")
def login():
    session["user"] = "Satyam"
    return "Session set! Go to <a href='/dashboard'>/dashboard</a>"

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return f"<h2>Welcome to Dashboard, {session['user']}!</h2>"
    return "<h3>Unauthorized! Visit <a href='/login'>/login</a> first.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
