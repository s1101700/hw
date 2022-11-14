from flask import Flask, render_template, request




app = Flask(__name__)



@app.route("/")
def index():
    homepage=""
    homepage += "<a href=/about>我的個人簡介</a><br>"
    homepage += "<a href=/ability>能力</a><br>"
        
    homepage += "<a href=/work>相關工作介紹</a><br>"
    
    homepage += "<a href=/test>職涯測驗結果</a><br>"
    
    homepage += "<a href=/company>公司介紹</a><br><br>"
    return homepage



@app.route("/about")
def me():
    return render_template("about.html")



@app.route("/ability")
def leader():
    return render_template("ability.html")   



@app.route("/work")
def work():
    return render_template("work.html")




@app.route("/test")
def test():
    return render_template("test.html")



@app.route("/company")
def job():
    return render_template("company.html")

if __name__ == "__main__":
    app.run()