from flask import Flask, render_template, request #use python in HTML 
import requests #Talks to API

librarys_list_params = {
  "token": "uclapi-738dd8c9e77498a-39aefce60ca1db6-50fe1ceb32dc5d4-c03b8b4218e13a8",
} #my UCL API token
librarys_list_response = requests.get("https://uclapi.com/workspaces/surveys", params=librarys_list_params)

librarys = librarys_list_response.json()['surveys'] #gets dictionary of UCL librarys in .json format


app = Flask("MyApp")

@app.route("/") #When someone goes to the homepage, run the function below 
def hello():
    return render_template("UCL_seats.html", librarys=librarys) #use my HTML file in browser and define Librarys in HTML doc in the same way as in my Python doc

@app.route("/library/<library_id>/<map_id>") #When someone goes to homepage/id, run the function below
def library_page(library_id,map_id): #pass these arguments through the function every time someone goes to this page 
	map_image_params = {
	  "token": "uclapi-738dd8c9e77498a-39aefce60ca1db6-50fe1ceb32dc5d4-c03b8b4218e13a8",
	  "survey_id": library_id,
	  "map_id": map_id
	}

	map_image_response = requests.get("https://uclapi.com/workspaces/images/map/live", params=map_image_params) #requests documentation 
	
	 
	map_image = map_image_response.text
	return render_template("mapimage.html", map_image= map_image) 


app.run(debug=True) 