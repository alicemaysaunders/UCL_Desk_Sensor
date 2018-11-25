from flask import Flask, render_template, request #use python in HTML 
import requests #Talks to API

params = {
  "token": "uclapi-738dd8c9e77498a-39aefce60ca1db6-50fe1ceb32dc5d4-c03b8b4218e13a8",
} #my UCL API token
r = requests.get("https://uclapi.com/workspaces/surveys", params=params)

librarys = r.json()['surveys'] #gets dictionary of UCL librarys 

app = Flask("MyApp")

@app.route("/") #When someone goes to the homepage, run the function below 
def hello():
    return render_template("UCL_seats.html", librarys=librarys) #use my HTML file in browser and define Librarys in HTML doc in the same way as in my Python doc

@app.route("/library/<id>") #When someone goes to homepage/id, run the function below
def library_page(id):
	params = {
	  "token": "uclapi-738dd8c9e77498a-39aefce60ca1db6-50fe1ceb32dc5d4-c03b8b4218e13a8",
	  "survey_id": 22,
	  "map_id": 3
	}

	r = requests.get("https://uclapi.com/workspaces/images/map/live", params=params)
	print(r.json())

app.run(debug=True) 