# This is your backend file. You can create access to your html files here
# you can also create APIs using this same format but accessing those APIs for data
# are recommended in JS files. If the site isn't so backend intensive then I keep things
# monolithic. However if you're making a full platform split the API routes and the display routes
# between 2 apps. They will be highlighted below

from flask import *
from dotenv import load_dotenv
import os
import requests

#loads in environment variables from the .env file to do local work
load_dotenv()

#assigns env variables to variable
client_id = os.environ["client"]
client_secret = os.environ["secret"]

#initializes your app
app = Flask(__name__)


#these are routes, so anything you want to make publicly accessible you'll reference here

#here's your display routes, these simply display your html files

#home page
@app.route("/", methods=["GET"])
def home():
    return render_template("/pages/home.html")

#about page
@app.route("/", methods=["GET"])
def about():
    return render_template("/pages/about.html")

#here's your api routes, you can connect these to a database or 
#just operate as a backend function. You would call these in your JS 
#file using a fetch method or ajax and simply hitting the /api/{insertroutename} url
#you can specify multiple methods as shown below so that using certain methods has different
#functionality.

#a simple get API
@app.route("/api/ip/server", methods=["GET"])
def get_server_ip():
    response = requests.get('https://api.ipify.org').json()
    return response

#A more complex API with multiple methods and a parameter
@app.route("/api/ip/geolocation", methods=["GET","POST"])
def get_geolocation():
    if request.method == "GET":
        requested_ip = request.args['IP']
        response = requests.post(f"https://coolipgeolocationapi/{requested_ip}")
        return response
    elif request.method == "POST":
        return "This does something else"
    else:
        return
    
#This runs the server locally so you can see what's happening at http://localhost 
#note, if you wanted to test a separate API server so your app is more modular and not
#monolithic you can change the port on your second app repo and run it at the same time
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80) #if you wanted to change the port you would 
                                     #simply select another port here usually over 3000

