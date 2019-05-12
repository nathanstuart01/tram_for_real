from app.app import db

class Rider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    #eventually add in a photo column, perhaps make this come from a photos table joined on rider/driver id
    #photo
    #rating. eventually add in this column, make it come from the ratings table
