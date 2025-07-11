from flask import Flask, render_template
from random import *
from datetime import datetime as dt
import requests

app = Flask(__name__)

year = dt.now().year
blog_url = "https://api.npoint.io/"
response_blog = requests.get(blog_url).json()
posts_list = []
for post in response_blog:
    posts_list.append(post)


@app.route('/')
def blog_page():
    return render_template("index.html",  this_year=year, all_posts=response_blog)


@app.route('/<int:index>')
def post_page(index):
    requested_post = None
    for p in posts_list:
        if p['id'] == index:
            requested_post = p

    return render_template("post.html", the_post=requested_post)

app.run()




