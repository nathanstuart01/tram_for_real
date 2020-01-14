import React from 'react';

class ShowDriverTrips extends React.Component {

    state = { edit: 'False', car: {} }

    componentDidMount() {
        const { trip } = this.props;
        console.log(trip);
    }

    edit = () => {
        return (
            <div>Edit Driver Trip</div>
        )
    }

    show = () => {
        return (
            <div>Show Driver Trip</div>
        )
    }

    render() {
        return (
            this.state.edit ? this.edit() : this.show ()
        )
    }
}

export default ShowDriverTrips;