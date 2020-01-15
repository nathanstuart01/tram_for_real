import React from 'react';

class ShowDriverTrips extends React.Component {

    state = { edit: false, car: {} }

    componentDidMount() {
    }

    edit = () => {
        return (
            <div>Edit Driver Trip</div>
        )
    }

    show = () => {
        let trip = this.props.location.state.trip;
        console.log(trip);
        if(Object.keys(trip).length) {
            return (
                <div>
                <h1>Trip Details</h1>
                <h4>{trip.departure_date}</h4>
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