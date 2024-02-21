from flask import Flask, render_template
import git

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/dashboard")
def contact():
    return "hi"


@app.route("/git_update", methods=['POST'])
def git_update():
    repo = git.Repo('./Flask-Project')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
    #say