import React from 'react';
import { BASE_URL } from './Url';

const endpoint = 'show_driver_trips';

const handleTrips = (trips) => {
    var trips = trips['Current active driver trips'];
    var i;
    for (i = 0; i < trips.length; i++) {
        console.log(trips[i]);
    }
}

const getDriverTrips = (token) => {
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

const DriverTrips = () => {

    var trips = getDriverTrips(localStorage.getItem('access_token'))

    return (
    <div><h3>Driver Trips</h3></div>
    );
}

export default DriverTrips;
