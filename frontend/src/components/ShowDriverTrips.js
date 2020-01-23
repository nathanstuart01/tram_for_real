import React from 'react';
import { BASE_URL } from './Url';

class ShowDriverTrips extends React.Component {

    state = { edit: false, car: {} }

    componentDidMount() {
    }

    toggleEdit = () => {
        this.setState({ edit: !this.state.edit });
    }

    updateTrip = (departureDate, returnDate, startLocation, endLocation, availableSeats) => {
        let tripId = this.props.location.state.trip.trip_id;
        let token = localStorage.getItem('access_token');
        fetch(`${BASE_URL}/${'update_trip'}/${tripId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({start_location: startLocation})
        }).then(res => res.json())
            .then( result => {
                console.log(result);
                // flash message via react??
                // state is not updated and as such need to do a refresh, which is unacceptable. Need to figure something out here
                this.props.history.push('/user_home_page');
            })
            .catch( error => {
                console.log(error.message);
            })

        this.props.history.push('/user_home_page');
    }

    handleSubmit = (e) => {
        e.preventDefault();
        let departureDate = this.refs.departureDate.value;
        let returnDate = this.refs.returnDate.value;
        let startLocation = this.refs.startLocation.value;
        let endLocation = this.refs.endLocation.value;
        let availableSeats = this.refs.availableSeats.value;
        this.updateTrip(departureDate, returnDate, startLocation, endLocation, availableSeats);
    }

    edit = (edit_trip) => {
        let trip = edit_trip;
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <h1>Edit Driver Trip</h1>
                    <h6>Trip Name:</h6>
                    <h6>(Update Trip Model to Include Trip Name)</h6>
                    <h6>Date:</h6>
                    <input ref='departureDate' type='text' required placeholder='Trip Departure Date' defaultValue={trip.departure_date} />
                    <br />
                    <h6>Return Date:</h6>
                    <input ref='returnDate' type='text' required placeholder='Trip Return Date' defaultValue={trip.return_date} />
                    <br />
                    <h6>Start Location:</h6>
                    <input ref='startLocation' type='text' required placeholder='Trip Start Location' defaultValue={trip.start_location} />
                    <br />
                    <h6>End Location:</h6>
                    <input ref='endLocation' type='text' required placeholder='Trip End Location' defaultValue={trip.end_location} />
                    <br />
                    <h6>Available Seats:</h6>
                    <input ref='availableSeats' type='text' required placeholder='Trip Available Seats' defaultValue={trip.avaiable_seats} />
                    <br />
                    <input type='submit' />
                </form>
            </div>
        )
    }

    show = (show_trip) => {
        let trip = show_trip || {};
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
            this.state.edit ? this.edit(this.props.location.state.trip) : this.show(this.props.location.state.trip)
        )
    }
}

export default ShowDriverTrips;