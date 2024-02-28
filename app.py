from flask import Flask
app_login = Flask(__name__)
print(__name__)
@app_login.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
  app_login.run(host='0.0.0.0', port=8080)