from flask.views import MethodView,View
from flask import render_template,redirect,url_for,request
from db import db 
from model import Post

class ViewAllPosts(MethodView):
    def get(self):
        posts = Post.query.all()
        return render_template("index.html",posts=posts,title="Home")

class add_post(MethodView):
    def get(self):
        return render_template('AddPost.html')
    def post(self):
        title = request.form["title"]
        content = request.form["content"]
        author = request.form["author"]
        new_post=Post(title=title,content=content,author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("index"))
class UpdetePost(MethodView):
    def get(self,id):
        post=Post.query.get_or_404(id)
        return render_template('updatePost.html',post=post)
    def post(self,id):
        post=Post.query.get_or_404(id)
        post.title = request.form["title"]
        post.content = request.form["content"]
        post.author = request.form["author"]
        
        db.session.commit()
        return redirect(url_for("index"))
class DetailsPost(MethodView):
    def get(self,id):
        post=Post.query.get_or_404(id)
        return render_template("postDetails.html",title="post details",post=post)

class DeletePost(MethodView):
    def post(self,id):
         post=Post.query.get_or_404(id)
         db.session.delete(post)
         db.session.commit()
         return redirect(url_for("index"))

