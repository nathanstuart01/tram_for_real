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
    	back_populates='trips')
    
    def remove_rider_from_trip(self, rider_id):
        new_riders = [rider for rider in self.riders if rider != rider_id]
        self.riders = new_riders
        self.available_seats = self.available_seats + 1
        db.session.commit()
    
    def add_rider_to_trip(self, rider_id):
        self.riders.append(rider_id)
        self.available_seats = self.available_seats - 1
        db.session.commit()

