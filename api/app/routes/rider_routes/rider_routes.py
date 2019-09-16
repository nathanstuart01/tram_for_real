from app.app import app, db, jwt
from app.models.rider import Rider
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


