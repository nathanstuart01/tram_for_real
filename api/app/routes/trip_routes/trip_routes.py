from app.app import app, db, jwt
from app.models.trip import Trip
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required

@app.route('/api/create_trip', methods=['POST'])
@jwt_required
def create_trip():
    start_location = request.json.get('start_location')
    end_location = request.json.get('end_location')
    departure_date = request.json.get('departure_date')
    return_date = request.json.get('return_date')
    available_seats = request.json.get('available_seats')
    driver_id= request.json.get('driver_id')
    if not all([start_location, end_location, departure_date, return_date, available_seats, driver_id]):
        message = 'Invalid trip inputs, please fill in all inputs correctly'
        abort(400, message)
    try:
        trip = Trip(
                start_location=start_location,
                end_location=end_location,
                departure_date=departure_date,
                return_date=return_date,
                available_seats=available_seats,
                driver_id=driver_id,
            )
        db.session.add(trip)
        db.session.commit()
        return jsonify({'Message': 'New trip was created',
                        'Trip start location': start_location,
                        'Trip end location': end_location,
                        'Trip departure date': departure_date,
                        'Trip return date': return_date,
                        'Trip available seats': available_seats,
                        'Trip driver': driver_id,
                        }), 201
    except:
        return jsonify({'Message': 'New trip was not able to be created, something went wrong'}), 500

@app.route('/api/joinable_trips', methods=['POST'])
@jwt_required
def show_joinable_trips():
    trip_departure_date = request.json.get('departure_date')
    if not all([trip_departure_date]):
        message = 'Invalid trip date, please try inputting trip date again'
        abort(400, message)
    try:
        selected_trips = Trip.query.filter(Trip.departure_date >= trip_departure_date).filter(Trip.available_seats > 0).all()
        return jsonify({'Available Trips for Selected Date': selected_trips[0].id}), 200
    except:
        return jsonify({'Message': "Specified trips were not able to be returned, something went wrong"}), 500