from app.app import app, db, jwt
from app.models.trip import Trip
from app.models.user import User
from app.models.rider import Rider
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_claims

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
        trips = [{'id': trip.id, 'trip_start_location': trip.start_location, 'trip_end_location': trip.end_location, 'trip_start_time': trip.departure_date, 'trip_end_time': trip.return_date, 'trip_seats': trip.available_seats, 'trip_driver': trip.driver_id, 'trip_riders': trip.riders} for trip in selected_trips]
        return jsonify({'Available Trips for Selected Date': trips}), 200
    except:
        return jsonify({'Message': "Specified trips were not able to be returned, something went wrong"}), 500

@app.route('/api/join_trip', methods=['POST'])
@jwt_required
def join_trip():
    trip_id = request.json.get('trip_id')
    current_user_info = get_jwt_claims()
    if not all([trip_id]):
        message = 'Invalid trip id format, please try inputting trip id again'
        abort(400, message)
    try:
        trip_to_join = Trip.query.filter(Trip.id == trip_id).first()
        rider = Rider.query.filter(Rider.user_id == current_user_info['user_id']).first()
        trip_to_join.add_rider_to_trip(rider)  
        return jsonify({'This user joined selected trip': rider.id, 'trip available seats': trip_to_join.available_seats}), 200
    except:
        return jsonify({'Message': 'Specified trip id was not able to be joined, something went wrong'}), 500

@app.route('/api/show_driver_trips', methods=['GET'])
@jwt_required
def show_driver_trips():
    pass