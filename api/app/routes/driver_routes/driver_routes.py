from app.app import app, db, jwt
from app.models.driver import Driver
from flask import request, jsonify, abort
from flask_jwt_extended import jwt_required

@app.route('/api/create_driver', methods=['POST'])
@jwt_required
def create_driver():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    if first_name is None or last_name is None:
        message = 'Invalid driver inputs, please fill in both a first and last name'
        abort(400, message)
    try:
        driver = Driver(first_name=first_name, last_name=last_name)
        db.session.add(driver)
        db.session.commit()
        return jsonify({'Message': 'New driver was created',
                        'Driver first name': first_name,
                        'Driver last name': last_name
                        }), 201
    except:
        return jsonify({'Message': 'New driver was not able to be created, something went wrong'}), 500

#curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS" -d '{"first_name":"driver_first_1", "last_name":"driver_last_1"}' http://localhost:5000/api/create_driver