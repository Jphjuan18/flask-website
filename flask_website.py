
#!/bin/python

from flask import Flask,render_template
import requests
import json

app = Flask(__name__)

def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    response = json.loads(requests.request("GET", url).text)
    x = str(response)
    r = x.split()
    cat_pic = r[3].replace(",",'')
    cat_pic = cat_pic.replace("'","")
    return cat_pic

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_pic = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_pic, subreddit

@app.route("/")

def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/cats.html")

def cats():
    cat_pic = get_cat()
    return render_template("cats.html", cat_pic=cat_pic)

app.run(host="0.0.0.0", port=80)

