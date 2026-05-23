from flask import Flask,render_template,url_for,redirect,request
from config import POSTGRES_URL
from model import Post,Comment
from form import CommentForm
from db import db
from views.postViews import ViewAllPosts,add_post,UpdetePost,DetailsPost,DeletePost
import os
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]=POSTGRES_URL
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")
db.init_app(app)
with app.app_context():
    db.create_all()


#------------------------lab 2
@app.route("/")
def index():
    posts = Post.query.all()
    form=CommentForm()

    return render_template("index.html",posts=posts,title="Home",form=form)
# all_post=ViewAllPosts.as_view('index')
# app.add_url_rule('/',view_func=all_post, methods=['GET'])

 #add post 
add_post=add_post.as_view('add_post')
app.add_url_rule('/add-post',view_func=add_post, methods=['GET','POST'])

# @app.route("/add-post", methods=["POST","GET"])
# def add_post():
#     if request.method=='POST':
#         title = request.form["title"]
#         content = request.form["content"]
#         author = request.form["author"]
#         new_post=Post(title=title,content=content,author=author)
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect(url_for("index"))
#     return render_template('AddPost.html')


 # update post
updatepost=UpdetePost.as_view("update_post")
app.add_url_rule('/update-post/<int:id>',view_func=updatepost, methods=['GET','POST'])
# @app.route("/update-post/<int:id>", methods=["POST","GET"])
# def update_post(id):
#     post=Post.query.get_or_404(id)
#     if request.method=='POST' or request.method == "PUT":
#         post.title = request.form["title"]
#         post.content = request.form["content"]
#         post.author = request.form["author"]
        
#         db.session.commit()
#         return redirect(url_for("index"))
#     return render_template('updatePost.html',post=post)

# delete pos
deletepost=DeletePost.as_view("delete_post")
app.add_url_rule("/delete-post/<int:id>",view_func=deletepost)

# @app.route("/delete-post/<int:id>", methods=["POST","GET"])
# def delete_post(id):
#     post=Post.query.get_or_404(id)
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for("index"))

# details post 

detailspost=DetailsPost.as_view("details_post")
app.add_url_rule('/details-post/<int:id>',view_func=detailspost,methods=["GET"])

# @app.route("/details-post/<int:id>", methods=["POST","GET"])
# def details_post(id):
#     post=Post.query.get_or_404(id)
  
#     return render_template("postDetails.html",title="post details",post=post)

@app.route("/add-comment/<int:post_id>",methods=["POST","GET"])
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form=CommentForm()
    if request.method == "POST":
        content = request.form["content"]
        author = request.form["author"]
        new_comment = Comment(content=content,author=author,post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("addcomment.html",title='comment page',form=form,post=post)




#  <!-- <button
#       class="btn btn-secondaty mt-2"
#       data-bs-toggle="collapse"
#       data-bs-target="#commentForm{{post.id}}"
#     >
#       Comment
#     </button>
#     <div class="collapse" id="commentForm{{post.id}}">
#       <form action="{{ url_for('add_comment', post_id=post.id) }}" method="post">
#          {{ form.hidden_tag() }}
#     {% for field in form if field.type != "CSRFTokenField" %}
#         <div class="form-group">
#             {{ field.label }}
#             {{ field(class="form-control") }}
#         </div>
#     {% endfor %}
#     <button type="submit" class="btn btn-primary">Submit</button>
#       </form>
#     </div>
   # <div> -->















# ---------------------------lab 1

# @app.route('/home')
# def home():
#     return '<h1> welcome home</h1>'
# @app.route('/about')
# def about():
#     return '<h1> about page</h1>'
# @app.route('/contact')
# def contact():
#     return '<h1> contact page</h1>'


# @app.route('/user/<username>')
# def diplayname(username):
#     print(type (username))
#     return f'username :{username}'

# @app.route('/user/<username>/<int:age>')
# def use_details(username,age):
#      return f'username :{username} age:{age}'

# users = [
# {"id":1,"name":"ali","age":20},
# {"id":2,"name":"ahmed","age":30},
# ]

# @app.route("/users")
# def all_users():
#     result = "<ul>"

#     for user in users:
#         result += f"<li>{user['name']} - {user['age']}</li>"

#     result += "</ul>"

#     return result
# @app.route('/add-users/<name>/<int:age>')
# def addUser(name, age):

#     new_user = {
#         "id": len(users) + 1,
#         "name": name,
#         "age": age
#     }
#     users.append(new_user)
#     return users
# @app.route('/delete-user/<int:id>')
# def deleteUser(id):
#     for user in users:
#        if user['id'] ==id:
#         users.remove(user)
#     return users
# # @app.route('/update-user/<int:id>/edit/<name>')
# # def updetuser(id,name):
# #      for user in users:
# #         if user['id'] ==id:
# #             user['name']=name
            
# #      return redirect(url_for('index'))


# @app.route('/')
# def index():
#     return render_template('index.html',users=users)
# #---------------------------------------------------------------add using form
# @app.route("/add-user", methods=["POST","GET"])
# def add_user():
#     if request.method=='POST':
#         name = request.form["name"]
#         age = request.form["age"]
#         new_user={'id':len(users)+1,'name':name,'age':age}
#         users.append(new_user)
#         return redirect(url_for("index"))
#     return render_template('add-user.html')


# #---------------------------------------------------------------update using form
# @app.route("/update-user/<int:id>", methods=["POST","PUT","GET"])
# def update_user(id):

#     current_user = None

#     for user in users:
#         if user["id"] == id:
#             current_user = user
#             break

#     if request.method == "POST":
#         current_user["name"] = request.form["name"]
#         current_user["age"] = request.form["age"]

#         return redirect(url_for("index"))

#     return render_template("updete-user.html",title="Update User",user=current_user)

if __name__=="__main__":
    app.run(debug=True)