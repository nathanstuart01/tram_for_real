from app.app import db
import datetime

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_location = db.Column(db.String(255), nullable=False)
    end_location = db.Column(db.String(255), nullable=False)
    departure_date = db.Column(db.DateTime(timezone=True), nullable=False)
    return_date = db.Column(db.DateTime(timezone=True), nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    #rider_id = db.Column(db.Integer, db.ForeignKey('Rider.id'), nullable=False)
