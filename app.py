  
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars 
from splinter import Browser

# Create an instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route('/')
def index():
	
	mars_info = mongo.db.mars_info.find_one()
	return render_template("index.html", mars_info=mars_info)

@app.route('/scrape')
def scrape_info():
	test_dict = mongo.db.mars_info
	test_dict = scrape_mars.scrape_info()
	test_dict.update({}, test_dict, upsert=True)
	
	return redirect("/", code=302)

if __name__ == "__main__":
	app.run(debug=True)