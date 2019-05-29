from app.app import db
import datetime
from app.models.riders import trip_riders 

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(255), nullable=False)
    end_location = db.Column(db.String(255), nullable=False)
    departure_date = db.Column(db.DateTime(timezone=True), nullable=False)
    return_date = db.Column(db.DateTime(timezone=True), nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    riders = db.relationship('Rider', secondary=trip_riders, lazy='subquery',
    	backref=db.backref('riders', lazy=True))
