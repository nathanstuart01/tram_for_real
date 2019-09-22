from app.app import app, db, jwt
from app.models.rider import Rider
from app.models.trip import Trip
from app.models.driver import Driver
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_claims

@app.route('/api/create_rider', methods=['POST'])
@jwt_required
def create_rider():
    current_user_info = get_jwt_claims()
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    user_id = current_user_info['user_id']
    if first_name is None or last_name is None:
        message = 'Invalid rider inputs, please fill in both a first and last name'
        abort(400, message)
    try:
        rider = Rider(first_name=first_name, last_name=last_name, user_id=user_id)
        db.session.add(rider)
        db.session.commit()
        return jsonify({'Message': 'New rider was created',
                        'Rider first name': first_name,
                        'Rider last name': last_name
                        }), 201
    except:
        return jsonify({'Message': 'New rider was not able to be created, something went wrong'}), 500

#curl -i -X POST -H "Authorization: Bearer $ACCESS" -H "Content-Type: application/json" -d '{"first_name": "test_rider_1", "last_name": "test_rider_last_2"}' http://localhost:5000/api/create_rider

@app.route('/api/join_trip', methods=['PUT'])
@jwt_required
def join_trip():
    trip_id = request.json.get('trip_id')
    current_user = get_jwt_claims()
    current_user_id = current_user['user_id']
    if not all([trip_id]):
        message = 'Invalid trip id format, please try inputting trip id again'
        abort(400, message)
    try:
        trip_to_join = Trip.query.filter(Trip.id == trip_id).first()
        rider = Rider.query.filter(Rider.user_id == current_user_id).first()
        trip_to_join.add_rider_to_trip(rider)
        return jsonify({'This user joined selected trip': rider.id, 'trip available seats': trip_to_join.available_seats}), 200
    except:
        return jsonify({'Message': 'Specified trip id was not able to be joined, something went wrong'}), 500

#curl -i -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS"  -d '{"trip_id":36}' http://localhost:5000/api/join_trip

@app.route('/api/show_rider_trips', methods=['GET'])
@jwt_required
def show_my_trips():
    current_user = get_jwt_claims()
    current_user_id = current_user['user_id']
    rider = Rider.query.filter(Rider.user_id == current_user_id).first()
    rider_trips = rider.trips
    trips_info = []
    try:
        for trip in rider_trips:
            driver = Driver.query.filter(Driver.id == trip.driver_id).first()
            trip_details = {'trip id': trip.id, 'trip_start': trip.start_location, 'trip_end': trip.end_location, 'trip_start_time': trip.departure_date, 'trip_end_time': trip.return_date, 'trip_seats': trip.available_seats, 'trip_driver_first': driver.first_name, 'trip_driver_last': driver.last_name}
            trips_info.append(trip_details)
        return jsonify({'rider_trips': trips_info}), 200
    except Exception as e:
        error = e.args
        return jsonify({'Request failed': error }), 500
#curl -i -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS" http://localhost:5000/api/show_rider_trips

@app.route('/api/cancel_rider_trip/<int:trip_id>', methods=['PUT'])
@jwt_required
def cancel_rider_from_trip(trip_id):
    current_user = get_jwt_claims()
    current_user_id = current_user['user_id']
    rider = Rider.query.filter(Rider.user_id == current_user_id).first()
    rider_id = rider.id
    trip_to_remove_rider = Trip.query.filter(Trip.id == trip_id).first()
    trip_to_remove_rider.remove_rider_from_trip(rider_id)
    try:
        return jsonify({'rider was cancelled from trip': {'trip state date': trip_to_remove_rider.departure_date, 'trip end date': trip_to_remove_rider.return_date, 'trip start location': trip_to_remove_rider.start_location, 'trip end location': trip_to_remove_rider.end_location}}), 200
    except Exception as e:
        return jsonify({'unable to cancel rider from trip': e.args})
# rider is removed from trip.riders but rider with selected trips still shows up, why??