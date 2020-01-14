from app.app import app, db, jwt
from app.models.driver import Driver
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_claims

@app.route('/api/create_driver', methods=['POST'])
@jwt_required
def create_driver():
    current_user_info = get_jwt_claims()
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    user_id = current_user_info['user_id']
    if first_name is None or last_name is None:
        message = 'Invalid driver inputs, please fill in both a first and last name'
        abort(400, message)
    try:
        driver = Driver(first_name=first_name, last_name=last_name, user_id=user_id)
        db.session.add(driver)
        db.session.commit()
        return jsonify({'Message': 'New driver was created',
                        'Driver first name': first_name,
                        'Driver last name': last_name
                        }), 201
    except:
        return jsonify({'Message': 'New driver was not able to be created, something went wrong'}), 500

#curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS" -d '{"first_name":"driver_first_1", "last_name":"driver_last_1"}' http://localhost:5000/api/create_driver

@app.route('/api/show_driver_trips', methods=['GET'])
@jwt_required
def show_driver_trips():
    current_user_info = get_jwt_claims()
    driver_id = current_user_info['user_id']
    try:
        driver = Driver.query.filter(Driver.user_id == driver_id).first()
        trips = [{'start_location':trip.start_location, 'end_location': trip.end_location, 'departure_date': trip.departure_date, 'return_date': trip.return_date, 'avaiable_seats': trip.available_seats, 'driver_id': trip.driver_id, 'trip_id': trip.id} for trip in driver.trips]

        return jsonify({'Current active driver trips': trips}), 200
    except:
        return jsonify({'Message': 'unable to return selected driver trips'}), 500

@app.route('/api/show_driver_trip/<int:trip_id>', methods=['POST'])
@jwt_required
def show_driver_trip():
    current_user_info = get_jwt_claims()
    driver_id = current_user_info['user_id']
    try:
        driver = Driver.query.filter(Driver.user_id == driver_id).first()
        trip = {'start_location':trip.start_location, 'end_location': trip.end_location, 'departure_date': trip.departure_date, 'return_date': trip.return_date, 'avaiable_seats': trip.available_seats, 'driver_id': trip.driver_id, 'trip_id': trip.id}

        return jsonify({'Current active driver trips': trip}), 200
    except:
        return jsonify({'Message': 'unable to return selected driver trips'}), 500



#curl -i -X GET -H "Authorization: Bearer $ACCESS" -H "Content-Type: application/json" http://localhost:5000/api/show_driver_trips

@app.route('/api/show_driver', methods=['GET'])
@jwt_required
def show_driver_info():
    current_user_info = get_jwt_claims()
    driver_id = current_user_info['user_id']
    try:
        driver = Driver.query.filter(Driver.user_id == driver_id).first()
        return jsonify({'driver first name': driver.first_name, 'driver last name': driver.last_name, 'driver id': driver.id}), 200
    except Exception as e:
        return jsonify({'error': e.args}), 500

#curl -i -X GET -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS" http://localhost:5000/api/show_driver

@app.route('/api/update_driver/<int:driver_id>', methods=['PUT'])
@jwt_required
def update_driver(driver_id):
    driver = Driver.query.filter(Driver.id == driver_id).first()
    driver_first_name = request.json.get('driver_first_name')
    driver_last_name = request.json.get('driver_last_name')
    if driver_first_name:
        driver.first_name = driver_first_name
    if driver_last_name:
        driver.last_name = driver_last_name
    db.session.add(driver)
    db.session.commit()
    return jsonify({'updated_driver_info': {'updated_driver_first_name': driver.first_name,
                                          'updated_driver_last_name': driver.last_name,
                                            }
                    })
#curl -i -X PUT -H "Authorization: Bearer $ACCESS" -H "Content-Type: application/json" -d '{"driver_first_name":"testy little updated driver first name", "driver_last_name": "testy little updated driver last name"}' http://localhost:5000/api/update_driver/1