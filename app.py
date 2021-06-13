from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#Set up mongo connection using flask_pymongo

app.config["MONGO_URI"] = '***'
mongo = PyMongo(app)


#create a route called /scrape that will import your scrape_mars.py script and call your scrape function.
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert= True)
    return redirect('/', code=302)

#Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


if __name__ == "__main__":
    app.run()