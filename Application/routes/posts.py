from Application import app, db
from Application.models.postModel import Post
from Application.forms.postForms import *
from flask import render_template, redirect, url_for
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