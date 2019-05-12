from app.app import db

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    trips = db.relationship("Trip", backref="driver", lazy=True)
    #car = # foreign key referencing car table
    #rating = db.Column(db.Integer) this will eventually need to be added in as a rating to sort drivers by rating


