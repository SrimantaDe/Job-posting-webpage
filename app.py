from flask import Flask, render_template
job_list=[
{
  "job_id":1,
  "Job_title":"Data Analyst",
  "Location":"Bengaluru, India",
  "salary":"Rs. 10,00,000"
},
  {
    "job_id":2,
    "Job_title":"Data Engineer",
    "Location":"Pune, India",
    "salary":"Rs. 12,00,000"
  },
  {
    "job_id":3,
    "Job_title":"Data Scientist",
    "Location":"Gurugram, India"
  },
  {
    "job_id":4,
    "Job_title":"AI Engineer",
    "Location":"Bengaluru, India",
    "salary":"Rs. 14,00,000"
  }
  
]

app_login = Flask(__name__)
print(__name__)
@app_login.route("/")
def hello_world():
    return render_template("home.html",jobs=job_list,company_name="Sid's Startup")

if __name__ == "__main__":
  app_login.run(host='0.0.0.0', port=8080)