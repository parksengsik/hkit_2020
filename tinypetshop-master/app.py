from flask import Flask, render_template, request
from dao import post_dao

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPosts.html')
def getPosts():
    posts = post_dao.select_posts()    
    return render_template('getPosts.html', posts=posts)

@app.route('/getPost.html')
def getPost():
    no = request.args.get('no')
    post = post_dao.select_post(no)
    return render_template('getPost.html', post=post)



app.run(port="5105", host="0.0.0.0", debug=True)
