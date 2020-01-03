import React from 'react';
import {withRouter} from 'react-router-dom';
import { logout } from './Auth';
import { authenticatedUser } from './Auth';
import DriverTrips  from './DriverTrips';
import RiderTrips from './RiderTrips';
import { BASE_URL } from './Url';

class UserHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = { trips: []};
      }

    getDriverTrips = (token) => {
        fetch(`${BASE_URL}/${'show_driver_trips'}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
            }).then(res => res.json())
                .then( result => {
                    this.setState({trips: result['Current active driver trips']});
                })
                .catch( error => {
                    console.log(error.message);
                })
            }
    
    componentDidMount() {
        var token = localStorage.getItem('access_token');
        this.getDriverTrips(token);
    }
    
    render(){

        return (
            <div>Authenticated User Home Page
                <DriverTrips driverTrips={this.state.trips} />
                <div id='riderTrips'><RiderTrips /></div>
                <button onClick={ (history) => {logout(); this.props.history.push('/')}}>Logout</button>
            </div>
            
        )
    }
}

export default withRouter(UserHomePage);