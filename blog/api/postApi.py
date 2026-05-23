from flask.views import  MethodView
from db import db
from flask import jsonify,request
from model import User,Post



class allUser(MethodView):
    def get(self):
        users=User.query.all()
        for user in users:
            data=[]
            data.append({
                'id':user.id,
                'name':user.name,
                'email':user.email

            })
        return jsonify(data)
class allposts(MethodView):
    def get(self):
        posts=Post.query.all()
        data=[]
        for post in posts:
            data=[]
            data.append({
                'id':post.id,
                'title':post.title,
                'content':post.content,
                'user_id':post.user_id
                })
        return jsonify(data)
    
class AddPost(MethodView):

    def get(self):

        posts = Post.query.all()

        data = []

        for post in posts:

            data.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'user_id': post.user_id
            })

        return jsonify(data)

    def post(self):

        data = request.get_json()

        new_post = Post(
            title=data["title"],
            content=data['content'],
            user_id=data['user_id']
        )

        db.session.add(new_post)
        db.session.commit()

        return jsonify({
            "message": "add success",
            "post": {
                "id": new_post.id,
                "title": new_post.title,
                "content": new_post.content,
                "user_id": new_post.user_id
            }
        })
class PostDetailsView(MethodView):

    def get(self, id):

        post = Post.query.get_or_404(id)

        return jsonify({
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "user_id": post.user_id
        })

    def put(self, id):

        post = Post.query.get_or_404(id)

        data = request.get_json()

        post.title = data["title"]
        post.content = data["content"]
        post.user_id = data["user_id"]

        db.session.commit()

        return jsonify({
            "message": "Post updated",
            "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "user_id": post.user_id
            }
        })

    def patch(self, id):

        post = Post.query.get_or_404(id)

        data = request.get_json()

        if "title" in data:
            post.title = data["title"]

        if "content" in data:
            post.content = data["content"]

        if "user_id" in data:
            post.user_id = data["user_id"]

        db.session.commit()

        return jsonify({
            "message": "Post partially updated",
            "post": {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "user_id": post.user_id
            }
        })