from app.app import db
from app.models.riders import trip_riders

class Rider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="rider")
    trips = db.relationship("Trip", secondary=trip_riders, lazy='subquery', back_populates="riders")
    #eventually add in a photo column, perhaps make this come from a photos table joined on rider/driver id
    #photo
    #rating. eventually add in this column, make it come from the ratings table

# adding a construct here will better show each indiviudal rider object