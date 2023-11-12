from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A王怡蓁的求職相關資訊</h1>"
    homepage += "<a href=/about>個人簡介</a><br>"
    homepage += "<a href=/work>ERP相關工作介紹</a><br>"
    homepage += "<a href=/test>職涯測驗結果</a><br>"
    homepage += "<a href=/me>履歷自傳</a><br>"
    return homepage

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/me")
def me():
    return render_template("me.html")


if __name__ == "__main__":
    app.run()