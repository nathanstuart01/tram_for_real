import React from 'react';

class DriverTrips extends React.Component {

    constructor(props) {
        super(props);
    }

        render() {
            let trips = this.props.driverTrips.map( (trip) => {
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
                        <h3>My Trips As Driver:</h3>
                        {trips}
                    </div>
                );
            } else {
                return (
                    <h5>You Haven't Created Any Rides</h5>
                );
            }
        }
    }   

export default DriverTrips;
