from flask import *

app = Flask(__name__)

contacts = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/makeportfolio", methods=['POST'])
def make():
    global contacts
    name = request.form['name']
    job = request.form['job']
    file = request.files['img']
    file.save("static/images/images.jpg")
    img = "/static/images/images.jpg"
    aboutme = request.form['aboutme']
    skills = request.form['skills'].split()
    github = request.form['githubusername']
    contacts = dict(zip(request.form['platform'].split(","),request.form['platform'].split(",")))
    print(contacts)
    return render_template("portfolio.html",name=name,job=job,img=img,aboutme=aboutme,skills=skills,githubusername=github,contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)