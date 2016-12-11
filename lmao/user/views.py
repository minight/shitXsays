from flask import render_template, request, current_app, redirect, session, url_for, jsonify, abort
from random import sample
from . import blueprint
from .models import Post
from ..main import db

HISTORY_MAX = 1
ADMIN_KEY = 'holyshitballs'

def is_admin():
    if session.get('admin') != ADMIN_KEY:
        return False
    return True

def check_admin():
    if session.get('admin') != ADMIN_KEY:
        abort(400)

@blueprint.before_request
def init_session():
    if 'viewed' not in session:
        session['viewed'] = []

@blueprint.errorhandler(400)
def error400(e):
    if e.description == '':
        e.description = 'nothing to see here'
    return render_template('error.html', errno='400', message=e.description)

@blueprint.errorhandler(404)
def error404(e):
    e.description = 'nothing to see here'
    return render_template("error.html", errno='404', message=e.description)

@blueprint.route('/delete/<post_id>', methods=['POST'])
def delete(post_id):
    check_admin()
    post = Post.query.filter(Post.id == post_id).first()
    post.deleted = True
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('.admin'))

@blueprint.route('/undelete/<post_id>', methods=['POST'])
def undelete(post_id):
    check_admin()
    post = Post.query.filter(Post.id == post_id).first()
    post.deleted = False
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('.admin'))

@blueprint.route('/<post_id>', methods=['GET', 'DELETE', 'UNDELETE'])
def post(post_id):
    post = Post.query.filter(Post.id == post_id).first()
    quote = post.content
    if post is None:
        return abort(404)
    if post.deleted == True:
        quote = 'deleted'

    session['viewed'].append(post_id)
    session.modified = True
    return render_template("quote.html", quote=quote)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('secret') == ADMIN_KEY:
            session['admin'] = request.form.get('secret')
            return redirect(url_for('.admin'))
    return render_template("login.html")

@blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    if is_admin():
        if request.method == 'POST':
            content = request.form.get('data')
            if content == '' or content == None:
                abort(400, 'Expecting \'data\' parameter')
            new_post = Post(content=content)
            db.session.add(new_post)
            db.session.commit()
        posts = Post.query.all()
        return render_template("admin.html", posts=posts)
    else:
        return redirect(url_for('.login'))

@blueprint.route('/', methods=['GET', 'POST'])
def home():
    # select some random entry that hasn't occured in the previous HISTORY_MAX
    readable_posts = [str(a[0]) for a in Post.query.with_entities(Post.id).filter(Post.deleted == False).all()]
    print 'readable posts', readable_posts
    viewed_posts = len(session['viewed'])
    if (viewed_posts >= len(readable_posts)):
        session['viewed'] = session['viewed'][-HISTORY_MAX:]
        session.modified = True

    unviewed = set(readable_posts) - set(session['viewed'])
    return redirect(url_for('.post', post_id=sample(unviewed, 1)[0]))
