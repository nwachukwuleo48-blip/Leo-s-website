from flask import Flask, render_template, jsonify
app=Flask(__name__)
JOBS= [
   {
     "id":1,
     "title":"Data Analyst",
     "location":"Kaduna, Nigeria",
     "salary":"$200,000"
   },  
   {
     "id":2,
     "title":"Data Analyst",
     "location":"Abuja, Nigeria",
     "salary":"$ 10,000"
   },  
   {
     "id"
     :3,
     "title":"Data Science",
     "location":"Lagos, Nigeria",
     "salary":"$100,000"
   },  
    {
     "id":4,
     "title":"Machine Learning",
     "location":"PH, Nigeria",
     "salary":"$500,000"
   } ,
   {
     "id":4,
     "title":"Machine Learning",
     "location":"PH, Nigeria",
     "salary":"Remote"
   } 





]

@app.route("/")
def hello_leo():
    return render_template("home.html",jobs=JOBS, company_name="Leo")
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)




if __name__=='__main__':
    app.run(debug=True)
