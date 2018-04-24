
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Artist(db.Model):

    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(200))
    website = db.Column(db.String(300))
    logo = db.Column(db.String(300))
    youtube = db.Column(db.String(300))
    album = db.relationship('Album', backref='user', cascade='all, delete-orphan', lazy='dynamic')

    def __init__(self, name, website, logo, youtube):
        self.name = name
        self.website = website
        self.logo = logo
        self.youtube = youtube

    def __repr__(self):
        return '<%r>' % self.name

class Album(db.Model):

    __tablename__ = 'album'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    release_year = db.Column(db.Integer)
    cover = db.Column(db.String(300))
    youtube = db.Column(db.String(300))
    artistid = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable = False)

    def __init__(self, name, release_year, cover, youtube):
        self.name = name
        self.release_year = release_year
        self.cover = cover
        self.youtube = youtube

    def __repr__(self):
        return '<User %r>' % self.name



'''class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chart = models.IntegerField(default=0, blank=True, null=True)
    award = models.CharField(max_length=200, blank=True, null=True)
    chart_date = models.DateField(blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    votes = models.IntegerField(default=0, blank=True, null=True)'''