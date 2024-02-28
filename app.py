from flask import Flask, render_template
app_login = Flask(__name__)
print(__name__)
@app_login.route("/")
def hello_world():
    return render_template("home.html")

if __name__ == "__main__":
  app_login.run(host='0.0.0.0', port=8080)