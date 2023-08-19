from flask import *
import bg


app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/portfolio",methods=["POST"])
def portfolio():
    fullname = request.form['fname']
    job = request.form['job']
    profile = request.files['profile']
    projects = request.form['project'].split(",")
    skills = request.form['skill'].split(",")
    cvlink = request.form['cv']
    about = request.form['about']
    imagepath = "static/profile.png"
    bg.bgremover(imagepath,imagepath)
    profile.save(imagepath)
    fb = request.form['fb']
    ig = request.form['ig']
    linkedin = request.form['linkedin']
    github = request.form['github']
    return render_template("portfolio.html",fullname=fullname,job=job,profile=imagepath,projects=projects,skills=skills,cvlink=cvlink,about=about,fb=fb,ig=ig,github=github,linkedin=linkedin)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")