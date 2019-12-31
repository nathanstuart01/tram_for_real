import React from 'react';
import { BASE_URL } from './Url';

const endpoint = 'show_rider_trips';

const handleTrips = (trips) => {
    var trips = trips['rider_trips'];
    var i;
    for (i = 0; i < trips.length; i++) {
        console.log(trips[i]);
    }
}

const getRiderTrips = (token) => {
    fetch(`${BASE_URL}/${endpoint}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
        }).then(res => res.json())
            .then( result => {
                handleTrips(result)
            })
            .catch( error => {
                console.log(error.message);
            })
        }

const RiderTrips = () => {

    //var trips = getRiderTrips(localStorage.getItem('access_token'))

    return (
    <div><h3>My Rider Trips</h3></div>
    );
}

export default RiderTrips;