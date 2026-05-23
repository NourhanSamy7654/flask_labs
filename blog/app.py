from config import POSTGRES_URL
from flask import Flask
from db import db
from api.postApi import allUser,allposts,AddPost,PostDetailsView
import os
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=POSTGRES_URL
db.init_app(app)
with app.app_context():
    db.create_all()

viewuser=allUser.as_view('home')
app.add_url_rule('/users',view_func=viewuser,methods=["GET"])

allPosts=allposts.as_view("allposts")
app.add_url_rule('/posts',view_func=allPosts,methods=["GET"])

addpost=AddPost.as_view('addpost')

app.add_url_rule('/addpost',view_func=addpost,methods=["GET","POST"])



view_post_details = PostDetailsView.as_view("post_details_view")
app.add_url_rule("/posts/<int:id>",view_func=view_post_details,methods=["GET","PUT","PATCH","DELETE"])

if __name__=="__main__":
    app.run(debug=True)