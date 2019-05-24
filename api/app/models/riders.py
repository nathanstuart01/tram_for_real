from app.app import db

trip_riders = db.Table('riders',
	db.Column('rider_id', db.Integer, db.ForeignKey('rider.id'), primary_key=True),
	db.Column('trip_id', db.Integer, db.ForeignKey('trip.id'), primary_key=True)
	)