import React from 'react';

class ShowDriverTrips extends React.Component {

    state = { edit: false, car: {} }

    componentDidMount() {
    }

    toggleEdit = () => {
        this.setState({ edit: !this.state.edit });
    }

    edit = () => {
        let trip = this.state
        return (
            <div>Edit Driver Trip</div>
        )
    }

    show = () => {
        let trip = this.props.location.state.trip;
        if(Object.keys(trip).length) {
            return (
                <div>
                    <div><button onClick={ () => {this.toggleEdit()}}>Edit This Trip</button></div>
                    <hr />
                <h1>Trip Details</h1>
                <h4>Departure Date: {trip.departure_date}</h4>
                <h4>Return Date: {trip.return_date}</h4>
                <h4>Start Location: {trip.start_location}</h4>
                <h4>End Location: {trip.end_location}</h4>
                <h4>Driver ID: {trip.driver_id}</h4>
                <h4>Trip ID: {trip.trip_id}</h4>
                </div>
            )
        }
        else {
            return (<h3>You Have No Created Trips, Please Create One</h3>)
        }
    }

    render() {
        return (
            this.state.edit ? this.edit() : this.show ()
        )
    }
}

export default ShowDriverTrips;