from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Web:web@localhost/flaskmusic'
db = SQLAlchemy(app)
app.debug = True

@app.route('/')
def index():
    artist = models.Artist.query.order_by().all()
    return render_template('index.html', artist=artist)

@app.route('/<int:artist_id>/')
def detail(artist_id):
    album = models.Album.query.filter_by(artistid= artist_id).order_by(models.Album.release_year).all()
    artist = models.Artist.query.get(artist_id)
    return render_template('detail.html', album=album, artist=artist)

@app.route('/success/<user>')
def success(user):
    return render_template('success.html', user=user)
    #return "%s You have successfully submitted an entry" % user

@app.route('/post_user', methods=['POST'])
def post_user():
    user = models.User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('success', user = user.username))

@app.route('/table/')
def post_map():
    emailvar = models.User.query.filter(models.User.email == '32').all()
    id = models.User.query.filter(models.User.id == 1).all()

    return render_template('map.html', email= emailvar, id=id)




if __name__ == "__main__":
    app.run()