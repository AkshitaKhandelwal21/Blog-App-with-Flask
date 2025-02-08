from Application import app, db
from Application.models.postModel import Post
from Application.models.userModel import User
from Application.forms.postForms import *
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required


@app.route('/new_blog', methods=['GET', 'POST'])
@login_required
def newBlog():
    form = NewBlog()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("create_post.html", form=form)


@app.route('/blogs')
def getBlog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page=page, per_page=10)
    return render_template("blog.html", posts=posts)


@app.route('/blogs/<int:post_id>')
def onePost(post_id):
    post = Post.query.get(post_id)
    form = DummyForm()  
    return render_template('post.html', post=post, form=form)


@app.route('/blogs/<username>')
def userPost(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user).paginate(page=page, per_page=10)
    return render_template('user_post.html', posts=posts)


@app.route('/blogs/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def updateBlog(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        return redirect(url_for('home'))
    form = NewBlog()

    if request.method=='GET':
        form.title.data = post.title
        form.content.data = post.content
            
    else:
        if form.validate():
            post.title = form.title.data
            post.content = form.content.data
            db.session.commit()
            return redirect(url_for('home', post_id=post.id))
    
    return render_template("update_post.html", form=form)


@app.route('/blogs/<int:post_id>/delete', methods=['POST', 'DELETE'])
@login_required
def deleteBlog(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        print("Not authorized")
        return redirect(url_for('home'))
        
    db.session.delete(post)
    db.session.commit()
    print("Deleted successfully")
    return redirect(url_for('home'))