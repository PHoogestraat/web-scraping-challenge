from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
from splinter import Browser

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_data_dic = mongo.db.collection.find_one()

    # Return template and data 
    #####################################################################   Test change back to index 
    return render_template("index.html", mars_data_dic=mars_data_dic)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape_info():

    # Run the scrape function
    mars_data_dic = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data_dic, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
