from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    title = "Welcome to my website!"
    return render_template("home.html", title=title)

@app.route('/about')
def about():
    title = "A bit about me."
    return render_template("about.html", title=title)

@app.route('/projects')
def projects():
    title = "Here are some of my projects from my past jobs and Tufts."
    return render_template("projects.html", title=title)

@app.route('/contact')
def contact():
    title = "Feel free to reach out via email or LinkedIn."
    return render_template("contact.html", title=title)


@app.route('/api/info')
def api_info():
    info = {
        "home": "Welcome to my website!",
        "about": "A bit about me.",
        "projects": "Here are some of my projects from my past jobs and Tufts.",
        "contact": "Feel free to reach out via email or LinkedIn."
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)

