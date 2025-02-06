from Application import app, db
from Application.models.postModel import Post
from Application.forms.postForms import *


@app.route('/new_blog', methods=['GET', 'POST'])
def newBlog():
    pass