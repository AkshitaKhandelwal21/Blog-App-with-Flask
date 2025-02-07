from Application import app
from flask import render_template, request
from Application.models.postModel import Post
from sqlalchemy import desc

@app.route('/', methods=['GET'])
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = session.query(Ticker).order_by(desc('updated')).first()
    posts = Post.query.order_by(desc('date')).limit(3).all()
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")
