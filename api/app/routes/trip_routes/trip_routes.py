from app.app import app, db, jwt
from app.models.trip import Trip
from app.models.user import User
from app.models.rider import Rider
from app.models.driver import Driver
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_claims

@app.route('/api/create_trip', methods=['POST'])
@jwt_required
def create_trip():
    current_user_info = get_jwt_claims()
    user_id = current_user_info['user_id']
    driver_id = Driver.query.filter(Driver.user_id == user_id).first()
    start_location = request.json.get('start_location')
    end_location = request.json.get('end_location')
    departure_date = request.json.get('departure_date')
    return_date = request.json.get('return_date')
    available_seats = request.json.get('available_seats')
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
                driver_id=driver_id.id,
            )
        db.session.add(trip)
        db.session.commit()
        return jsonify({'Message': 'New trip was created',
                        'Trip start location': start_location,
                        'Trip end location': end_location,
                        'Trip departure date': departure_date,
                        'Trip return date': return_date,
                        'Trip available seats': available_seats,
                        'Trip driver': driver_id.id,
                        }), 201
    except:
        return jsonify({'Message': 'New trip was not able to be created, something went wrong'}), 500
#curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS"  -d '{"start_location":"test start", "end_location":"test end", "departure_date":"2019-09-01 01:00:00", "return_date":"2019-09-01 06:00:00", "available_seats":4}' http://localhost:5000/api/create_trip

@app.route('/api/joinable_trips', methods=['GET'])
@jwt_required
def show_joinable_trips():
    trip_departure_date = request.json.get('departure_date')
    if not all([trip_departure_date]):
        message = 'Invalid trip date, please try inputting trip date again'
        abort(400, message)
    try:
        selected_trips = Trip.query.filter(Trip.departure_date >= trip_departure_date).filter(Trip.available_seats > 0).all()
        # add photo option to rider model to include here for options when joining a trip
        trips = [{'id': trip.id, 'trip_start_location': trip.start_location, 'trip_end_location': trip.end_location, 'trip_start_time': trip.departure_date, 'trip_end_time': trip.return_date, 'trip_seats': trip.available_seats, 'trip_driver': trip.driver_id, 'trip_riders': [{'rider first': rider.first_name, 'rider last': rider.last_name} for rider in trip.riders]} for trip in selected_trips]
        return jsonify({'Available Trips for Selected Date': trips}), 200
    except Exception as e:
        return jsonify({'Message': e.args}), 500
#curl -i -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS"  -d '{"departure_date":"2019-09-01"}' http://localhost:5000/api/joinable_trips

@app.route('/api/update_trip/<int:trip_id>', methods=['PUT'])
@jwt_required
def update_trip(trip_id):
    trip = Trip.query.filter(Trip.id == trip_id).first()
    start_location = request.json.get('start_location')
    end_location = request.json.get('end_location')
    return_date = request.json.get('return_date')
    available_seats = request.json.get('available_seats')
    departure_date = request.json.get('departure_date')
    if start_location:
        trip.start_location = start_location
    if end_location:
        trip.end_location = end_location
    if return_date:
        trip.return_date = return_date
    if available_seats:
        trip.available_seats = available_seats
    if departure_date:
        trip.departure_date = departure_date
    db.session.add(trip)
    db.session.commit()
    return jsonify({'updated_trip_info': {'updated_trip_start_loc': trip.start_location,
                                          'updated_trip_end_loc': trip.end_location,
                                          'updated_trip_dep_date': trip.departure_date,
                                          'updated_trip_ret_date': trip.return_date,
                                          'updated_trip_avail_seats': trip.available_seats,
                                            }
                    })
#curl -i -X PUT -H "Authorization: Bearer $ACCESS" -H "Content-Type: application/json" -d '{"return_date":"2019-08-01 16:00:00", "departure_date": "2019-08-01 07:00:00"}' http://localhost:5000/api/update_trip/5

@app.route('/api/delete_trip/<int:trip_id>', methods=['DELETE'])
@jwt_required
def delete_trip(trip_id):
    trip = Trip.query.filter(Trip.id == trip_id).first()
    try:
        db.session.delete(trip)
        db.session.commit()
        return jsonify('trip deleted successfully')
    except Exception as e:
        return jsonify({'unable to delete speficied trip with provided trip id': trip_id})

#curl -i -X DELETE -H "Authorization: Bearer $ACCESS" -H "Content-Type: application/json" http://localhost:5000/api/delete_trip/4