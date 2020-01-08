import React from 'react';

class RiderTrips extends React.Component {

    constructor(props) {
        super(props);
    }

        render() {
            let trips = this.props.riderTrips.map( (trip) => {
                return (
                    <ul key={trip.trip_id}>
                        <li>
                            <h6>Trip Date: {trip.departure_date}</h6>
                        </li>
                    </ul>
                );
            })
            if(trips.length !==0) {
                return (
                    <div>
                        <h3>My Trips As Rider:</h3>
                        {trips}
                    </div>
                );
            } else {
                return (
                    <h5>You Haven't Joined Any Rides</h5>
                );
            }
        }
    }   

export default RiderTrips;