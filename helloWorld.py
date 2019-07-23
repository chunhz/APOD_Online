from flask import Flask
import json
import requests
from flask import render_template

app = Flask(__name__, template_folder=r'./templates')

@app.route('/')
def apod():
    url = 'https://api.nasa.gov/planetary/apod?'
    # mykey = 'api_key=i5PuOllfkxjxChjX1ltpqMmZk9Xf4rt5cnRYf8Rr'
    mykey = 'api_key=DEMO_KEY'
    apiurl = url + mykey  # concatenates url with api key

    response = requests.get(apiurl)         # requests to the url
    data = response.text                    # save the result
    parsed = json.loads(data)               # read the information
    date = parsed["date"]                   # extract the information
    explanation = parsed["explanation"]
    image = parsed["url"]
    hdURL = parsed["hdurl"]

    return render_template('html.html',parsed = parsed) # use html file as a render template
                                                        # assign 'parsed' in html equal to 'parsed' in python file


